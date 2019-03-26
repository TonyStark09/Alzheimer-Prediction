import shutil
import os 

for d in os.listdir('C:/Users/kavita yadav/Desktop/AD_Prediction-master/images'):
    if d[0] != '.':
        print('C:/Users/kavita yadav/Desktop/AD_Prediction-master/images' + d)
        for f in os.listdir('C:/Users/kavita yadav/Desktop/AD_Prediction-master/images/'):
            print (f)
            if f[-3:] == 'nii':
                shutil.move("C:/Users/kavita yadav/Desktop/AD_Prediction-master/images" + d + '/' + f, 'C:/Users/kavita yadav/Desktop/AD_Prediction-master/images' + d)
shutil.rmtree('C:/Users/kavita yadav/Desktop/AD_Prediction-master/images')