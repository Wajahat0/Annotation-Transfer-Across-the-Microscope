import sys
import cv2
import argparse
import numpy as np
import pandas as pd
from yattag import Doc, indent


def homography_cal(img1,img3,surf):
  # Find the key points and descriptors with ORB
  img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
  img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)  
  keypoints1, descriptors1 = surf.detectAndCompute(img1, None)
  keypoints2, descriptors2 = surf.detectAndCompute(img3, None)
  bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck = False)
    
#   matches = bf.match(descriptors1, descriptors2)  
    

#   print('done')
  matches = bf.knnMatch(descriptors1, descriptors2,k=2)
#   matches = sorted(matches, key = lambda x : x.distance)

  all_matches = []
  for m, n in matches:
  # print(keypoints1[m.queryIdx].pt)

    all_matches.append(m)

  # Finding the best matches
  good = []
  for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good.append(m)

  MIN_MATCH_COUNT = 8
#   print(len(good))
  if len(good) > MIN_MATCH_COUNT:
    # Convert keypoints to an argument for findHomography
    src_pts = np.float32([ keypoints1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pts = np.float32([ keypoints2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    # print(src_pts)

    # Establish a homography
    M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)
#     print(M.shape)
    return M

  else:
    print('not enough good points')

