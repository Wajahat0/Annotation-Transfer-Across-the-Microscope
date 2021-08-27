
#######

#python xml2csv.py --dir Images -s CM2 -r 1000x

#######

import argparse
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("-dir", "--data_dir", help="Enter Path to data folder .", default="data")
parser.add_argument("-s", "--slidenumber", help="Enter the slide number.", default="CM1")
parser.add_argument("-r", "--resolution", help="1000x,400x,100x", default="1000x")

args = parser.parse_args()
print(args.resolution)

print(args.slidenumber + '/' + args.resolution)



def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df




image_path = os.path.join(os.getcwd(), args.data_dir + '/'+ args.slidenumber + '/' + args.resolution)
print(image_path)
xml_df = xml_to_csv(image_path)
print(image_path + '/'+ args.slidenumber + '_'  + args.resolution + '_' + 'labels.csv')
xml_df.to_csv((image_path + '/' + args.resolution + '_' + 'labels.csv'), index=None)
print('Successfully converted xml to csv.')





