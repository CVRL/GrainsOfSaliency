import sys
import torch
import torchvision.models as models
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import glob
import os
import csv
import numpy as np
import argparse
from tqdm import tqdm
import matplotlib.pyplot as plt
sys.path.append("../")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    device = torch.device('cuda')
    print(device)
    parser.add_argument('-imageFolder', default='',type=str)
    parser.add_argument('-modelPath',  default='',type=str)
    parser.add_argument('-csv',  default="",type=str)
    parser.add_argument('-output_scores',  default="",type=str)
    parser.add_argument('-network',  default="resnet",type=str)
    args = parser.parse_args()

    os.makedirs(args.output_scores,exist_ok=True)

    # Load weights of single binary DesNet121 model
    weights = torch.load(args.modelPath, map_location = device)

    # Definition of model architecture
    if args.network == "resnet":
        im_size = 224
        model = models.resnet50(pretrained=True)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, args.nClasses)
        model = model.to(device)
        model.layer4[-1].conv3.register_forward_hook(getActivation('features'))
    elif args.network == "inception":
        im_size = 299
        #model = models.inception_v3(pretrained=True)
        #model = models.inception_v3(pretrained=True,aux_logits=False)
        model = models.inception_v3(pretrained=True)
        model.aux_logits = False
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, args.nClasses)
        model = model.to(device)
        model.Mixed_7c.register_forward_hook(getActivation('features'))
    elif args.network == "densenet":
        im_size = 224
        model = models.densenet121(pretrained=True)
        num_ftrs = model.classifier.in_features
        model.classifier = nn.Linear(num_ftrs, args.nClasses)
        model = model.to(device)
    else:
        print("Invalid selection...exiting.")
        sys.exit()


    else:
        print("Invalid model selection...exiting")
        sys.exit()
    
    model.load_state_dict(weights['state_dict'])
    model = model.to(device)
    model.eval()

    if args.network == "xception":
        # Transformation specified for the pre-processing
        transform = transforms.Compose([
                    transforms.Resize([im_size, im_size]),
                    transforms.ToTensor(),
                    transforms.Normalize([0.5]*3, [0.5]*3)
                ])
    else:
        # Transformation specified for the pre-processing
        transform = transforms.Compose([
                    transforms.Resize([im_size, im_size]),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
                ])
    sigmoid = nn.Sigmoid()

    #File,PAScore,TRUE,Model,Training_Type,Dataset

    # imageFiles = glob.glob(os.path.join(args.imageFolder,'*.jpg'))
    imagesScores = []
    for file in glob.glob(args.csv):
        #imagesScores=[]
        Dataset = file
        Dataset = Dataset[:-3]
        imageCSV = open(file,"r")
        with open(file) as _file:
            for entry in _file:
                TRUE = entry.split(",")[1]
                tokens = entry.split(",")
                if tokens[0] != 'test':
                    continue
                upd_name = tokens[-1].replace("\n","")
                imgFile = args.imageFolder + upd_name

                # Read the image
                image = Image.open(imgFile).convert('RGB')
                # Image transformation
                tranformImage = transform(image)
                image.close()

                ## START COMMENTING HERE

                tranformImage = tranformImage[0:3,:,:].unsqueeze(0)
                tranformImage = tranformImage.to(device)

                # Output from single binary CNN model
                with torch.no_grad():
                    output = model(tranformImage)
                PAScore = sigmoid(output).detach().cpu().numpy()[:, 1]
                imagesScores.append([imgFile, PAScore[0], TRUE, Dataset])

    # Writing the scores in the csv file
    save_directory = args.output_scores + "all.csv"
    with open(save_directory,'w',newline='') as fout:
        writer = csv.writer(fout)
        writer.writerows(imagesScores)
