
import sys
import cv2
import argparse
import numpy as np
import pandas as pd
from yattag import Doc, indent
from homography_cal import homography_cal

def tranfer_annoation(data_path,t_data_path,slide_num,r_res,t_res,surf):
    load_csv_path = data_path +'/'+ slide_num+'/'+ r_res+ '/' +r_res + '_labels.csv'
    save_csv_path = t_data_path +'/'+ slide_num+'/'+ t_res+ '/' +t_res + '_labels.csv'
    
    r_image_path  = data_path +'/'+ slide_num+'/'+ r_res+ '/'
    t_image_path  = t_data_path +'/'+ slide_num+'/'+ t_res+ '/'
    
    print(load_csv_path)
    print(save_csv_path)
    print(r_image_path)
    print(t_image_path)
    
    df = pd.read_csv(data_path +'/'+ slide_num+'/'+ r_res+ '/' +r_res + '_labels.csv')  

    new_df=df

    ref_filename = str(df.iloc[0,0])
    print(ref_filename)
    ref=cv2.imread(r_image_path + ref_filename)
    xz=ref_filename.split('_')[-1]
    t_image= ref_filename.replace(xz, (t_res +'.png'))

    t_filename = t_image_path + t_image #ref_filename[:-9]+t_res+ '.png'
    print(t_filename)
    
# #     print(filename)
    target_image=cv2.imread(t_filename)
    h,w,c = target_image.shape
    
#     print('ref_image:-', ref_filename)
#     print('target_image:-', filename)
    
    h2=homography_cal(ref,target_image,surf)

    fname = ref_filename

    for i in range(0, len(df)):
        # read refrence image
        
        ref_filename = df.iloc[i,0]
            
        ref=cv2.imread(r_image_path + ref_filename)
    
#         # read target image
#         # need change here
#         xz=ref_filename.split('_')[-1]
        t_image= ref_filename.replace(xz, (t_res +'.png'))
        t_filename = t_image_path + t_image #ref_filename[:-9]+t_res+ '.png'
        target_image=cv2.imread(t_filename)
        h,w,c = target_image.shape

    
        if fname == ref_filename:
            print('skip_homograpy.....')
        else:
            print('compute homograpy.....')
            h2=homography_cal(ref,target_image,surf)

    
        points = np.float32([[df.iloc[i,4],df.iloc[i,5],df.iloc[i,6],df.iloc[i,7]]]).reshape(-1, 1, 2)
    
        t_points = cv2.perspectiveTransform(points, h2).reshape(1,4)
        new_df.iloc[i,0] = t_image
        new_df.iloc[i,1] = w 
        new_df.iloc[i,2] = h
        new_df.iloc[i,3] = df.iloc[i,3]
        new_df.iloc[i,4] = t_points[0,0]
        new_df.iloc[i,5] = t_points[0,1]
        new_df.iloc[i,6] = t_points[0,2]
        new_df.iloc[i,7] = t_points[0,3]
        fname = ref_filename
    
    new_df.to_csv(save_csv_path, index=False)
