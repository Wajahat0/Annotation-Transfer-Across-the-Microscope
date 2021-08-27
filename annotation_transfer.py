import sys
import cv2
#import cv2 as cv
import argparse
import numpy as np
import pandas as pd
from yattag import Doc, indent
from homography_cal import homography_cal
from coordinates import tranfer_annoation

print('Done')
surf = cv2.xfeatures2d.SURF_create(400)
#surf = cv.SIFT_create()
parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("-h_d", "--h_data_dir", help="Enter Path to expensive microscope data folder.", default="expensive")
parser.add_argument("-l_d", "--l_data_dir", help="Enter Path to low cost microscope data folder.", default="low_cost")
parser.add_argument("-s", "--slidenumber", help="Enter the slide number.", default="CM1")
parser.add_argument("-m", "--mode", help="across the microscope: o2c, o2o,c2c.", default="o2o")
parser.add_argument("-d", "--direction", help="1000xto1000x,1000xto400x, 400xto100x .", default="1000xto400x")
args = parser.parse_args()


if args.mode=='o2o':
	if args.direction=='1000xto400x':
		print('Code is running........')
		tranfer_annoation(args.h_data_dir,args.h_data_dir,args.slidenumber,'1000x','400x',surf)
	elif args.direction== '400xto100x':
		print('code is working')
		tranfer_annoation(args.h_data_dir,args.h_data_dir,args.slidenumber,'400x','100x',surf)
	else:
		print('mode not available')		
	
elif args.mode=='o2c':
	if args.direction=='100xto100x':
		print('code is working')
		tranfer_annoation(args.h_data_dir,args.l_data_dir,args.slidenumber,'100x','100x',surf)	
	else:
		print('mode not available')


elif args.mode=='c2c':

	if args.direction=='400xto1000x':
		print('code is running.......')
		tranfer_annoation(args.l_data_dir,args.l_data_dir,args.slidenumber,'400x','1000x',surf)	
	elif args.direction== '100xto400x':
		print('code is running.......')
		tranfer_annoation(args.l_data_dir,args.l_data_dir,args.slidenumber,'100x','400x',surf)
	else:
		print('mode not available')


else:

	print('Please enter a proper mode: e.g. -m o2c, o2o, c2c')	







    
