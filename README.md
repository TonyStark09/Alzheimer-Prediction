# AD-Prediction

Convolutional Neural Networks for Alzheimer's Disease Prediction Using Brain MRI Image

## How to run the code

#### 1. train the model:
```
python main_alexnet.py --optimizer Adam --learning_rate 1e-4 --save AlexNet-fine-tune-fc-last-conv-lr1e-4 --batch_size 16 --epochs 200 --gpuid 0
or
python main_autoencoder.py --batch_size 32 --num_classes 2 --epochs 200 --gpuid 0