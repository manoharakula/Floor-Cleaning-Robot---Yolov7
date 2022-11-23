#### SERX94: Machine Learning Evaluation
#### Dirt and Object Detection for floor cleaning Robots  
#### Manohar Akula
#### 11/22/2022

## Evaluation Metrics
### Metric 1

**Name:** mean Average Precision or mAP score

**Choice Justification:** The mean Average Precision or mAP score is calculated by taking the mean AP over all classes and/or overall IoU thresholds, depending on different detection challenges that exist.

### Metric 2
**Name:** Recall

**Choice Justification:** Recall is the ratio of the number of true positives to the total number of actual (relevant) objects. For example, if the model correctly detects 75 dirt or water labels in an image, and there are actually 100 labels in the image, the recall is 75 percent. F1 score—The F1 score is a weighted average of the precision and recall.


## Alternative -1
**Construction:** Changing the hyperparameters for the training model 1 = --batch-size 10 --epochs 100 --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-custom --weights yolov7.pt

**Evaluation:** Here the whole dataset was used and achieved highest mAP for model prediction. After looking at the results the dirt and water was predicted accurately with high confidence. Please refer to the video in evaluations/video.mp4

The mAP@0.5 started at 0.0002746 and map@0.5:0.95 started at 4.554e-05 intially after training the 100 epochs the map@0.5 achieved 0.6775 and the map@:0.5:0.95 achieved 0.2541. After testing this model with a raw video input the model is able to detect the dirt and water accurately. Please refer to the video in the evaluations folder

## Alternative -2
**Construction:** Changing the hyperparameters for the training model  = --batch-size 2 --epochs 100 --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-custom --weights yolov7.pt

**Evaluation:** Here the model was trained with the 10 percent of data and achieved highest mAP as compared to the previous model. But while predicting the dirt and water on the floor the model fails to detect accurately as well as decline in confidence. please refer to the video in evaluations/model_2/video.mp4

The mAP@0.5 started at 0.00022 and map@0.5:0.95 started at 3.324e-05 intially after training the 100 epochs the map@0.5 achieved 0.8827 and the map@:0.5:0.95 achieved 0.4958 . After testing this model with a raw video input the model is not able to detect the dirt and water accurately. Please refer to the video in the evaluations folder

## Alternative -3
**Construction:** Changing the hyperparameters for the training model  = --batch-size 8 --epochs 100 --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-custom --weights yolov7_tiny.pt

**Evaluation:** Here the model was trained with the 50 percent of data with the yolov7_pretrained weights and achieved highest mAP as compared to the previous model. But while predicting the dirt and water on the floor the model detected them moderatly with a less confidence. Please refer to the video in evaluations/model_3/video.mp4

The mAP@0.5 started at 0.0002 and map@0.5:0.95 started at 5.324e-05 intially after training the 100 epochs the map@0.5 achieved 0.7827 and the map@:0.5:0.95 achieved 0.3958 . After testing this model with a raw video input the model is not able to detect the dirt and water accurately. Please refer to the video in the evaluations/model_3/video.mp4



## Visualization
### Visual 1
**Analysis:** 
The initial values for the mAP@0.5 and map@0.5:0.95 in the model one are 0.0002746 and 4.554e-05, respectively. After training for 100 epochs, the map@0.5 attained 0.6775 and the map@:0.5:0.95 obtained 0.2541. This model can detect the wetness and dirt with accuracy after being tested with a raw video input. Refer to the evaluations folder's video for further information.

Please see the training models/result.png file for the outcome analysis graph. Additionally, I have examined many metrics for the models, including the test and train ratio graphs, the labels ratio, the confusion matrix, the P curve, and the R curve in the same folder.

### Visual -2
**Analysis:** 
In the model two, the mAP@0.5 started at 0.00022 and the map@0.5:0.95 started at 3.324e-05. After 100 epochs of training, the map@0.5 achieved 0.8827 and the map@0.5:0.95 obtained 0.4958. When tested with raw video input, the model is unable to identify dirt and wetness reliably. Please see the video in the evaluations folder for further information.

Please see training models/result.png for the outcome analysis graph. In addition, I examined many metrics for the models in the same folder, including P curve, R curve, labels ratio, test and train ratio graphs.

### Visual -3
**Analysis:** 
After training for 100 epochs, the map@0.5 reached 0.7827 and the map@:0.5:0.95 obtained 0.3958 for the model three, which had mAP@0.5 began at 0.0002 and map@0.5:0.95 started at 5.324e-05 initially. This model cannot properly identify the dirt and wetness after being tested using a raw video input. Refer to the video in evaluations/model 3/video.mp4 for further information.

Please see training models/result.png for the outcome analysis graph. Additionally, I have examined many metrics for the models, including graphs of the test and train ratios, labels ratio, P curve, and R curve in the same folder.

## Best Model

**Model:** The model with the highest accuracy and confidence level for forecasting the dirt and water class on the floor is model 1.. 