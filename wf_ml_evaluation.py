
# Author : Manohar Akula
# Date: 11/21/22
# Project - Machine Learning Analysis


"""This will contain code that splits your data into test and training sets (which
be stored in the "models" folder)trains a model (by calling functions in wf_training.py), and then
evaluates it by performing prediction on the test set (by calling functions in wf_prediction.py). This file provides a secondary entry point to running your workflow. It should be assumed that wf_core.py
has previously executed to populate the data_processe folder"""

import sys
import os

print("Please select the model (CPU or GPU) before training")
print("Yolov7 Model training started it may take around 5 hours to train the model")
print("I personally used Nvidia Tesla GPU & it took me around 5 hours on google cloud with batch size 10 and 100 epochs")


#Model-1
# Cuda Supported code - requires GPU support

#os.system("python wf_ml_training.py --workers 1 --device 0 --batch-size 10 --epochs 100 --img 640 640 --data data_processing/train_test/custom_data.yaml --hyp data_processing/train_test/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name Data_Munging_visualisation --weights data_processing/cfg/yolov7_pretarined_weights.pt")

#os.system("python wf_ml_training.py --workers 1 --device 0 --batch-size 10 --epochs 10 --img 640 640 --data data_processing/train_test/custom_data.yaml --hyp data_processing/train_test/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name Data_Munging_visualisation --weights data_processing/cfg/yolov7_pretarined_weights.pt")



# Uncomment if the machine doesn't support the CUDA or GPU
os.system("python wf_ml_training.py --workers 1 --batch-size 10 --epochs 150 --img 640 640 --data data_processing/train_test/custom_data.yaml --hyp data_processing/train_test/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name Data_Munging_visualisation --weights data_processing/cfg/yolov7_pretarined_weights.pt")


#Model - 2 Reducing the epoch size and evaluating the accuracies

#os.system("python wf_ml_training.py --workers 1 --batch-size 10 --epochs 50 --img 640 640 --data data_processing/train_test/custom_data.yaml --hyp data_processing/train_test/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name Data_Munging_visualisation --weights data_processing/cfg/yolov7_pretarined_weights.pt")

#Model - 3 Reducing the batch size and epochs for evaluating the accuracies

#os.system("python wf_ml_training.py --workers 1 --batch-size 4 --epochs 10 --img 640 640 --data data_processing/train_test/custom_data.yaml --hyp data_processing/train_test/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name Data_Munging_visualisation --weights data_processing/cfg/yolov7_pretarined_weights.pt")

#Model - 4 Using YoloV7_tiny pretrained model and evaluating the accuracies

#os.system("python wf_ml_training.py --workers 1 --batch-size 10 --epochs 100 --img 640 640 --data data_processing/train_test/custom_data.yaml --hyp data_processing/train_test/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name Data_Munging_visualisation --weights data_processing/cfg/yolov7-tiny_pretarined_weights.pt")

print("Training is sucessful!!")

os.system("python wf_ml_prediction.py --weights trained_models/best.pt --conf 0.5 --img-size 640 --source data_processing/prediction_samples/video.mp4")