###########
# python csv2xml.py -dir Images -s CM2 -r 400x  
#
#
#
#
#############

import pandas as pd
from yattag import Doc, indent
import argparse
import os

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("-dir", "--data_dir", help="Enter Path to data folder .", default="data")
parser.add_argument("-s", "--slidenumber", help="Enter the slide number.", default="CM1")
parser.add_argument("-r", "--resolution", help="1000x,400x,100x", default="1000x")

args = parser.parse_args()
print(args.resolution)


def create_xml(fname, box,path):
	#path = './'

	doc, tag, text = Doc().tagtext()

	with tag('annotation'):
	    with tag('folder'):
	    	text('LabelledImages')
	    with tag('filename'):
	    	text(fname)
	    with tag('path'):
	    	text(path + fname)
	    with tag('source'):
	    	with tag('database'):
	    		text('Unknown')
	    #with tag('size'):
	        #with tag('width'):
	         #   text(width)
	        #with tag('height'):
	        #    text(height)
	        #with tag('depth'):
	        #    text(3)
	    #with tag('segmented'):
	    #	text(0)

	    for b in box:
	    	with tag('size'):
	        	with tag('width'):
	            		text(int(b[1]))
	        	with tag('height'):
	            		text(int(b[2]))
	        	with tag('depth'):
	            		text(3)
	    	with tag('segmented'):
	    		text(0)

	    	with tag('object'):
		    	with tag('name'):
		    		text(b[3].lower())
		    	with tag('pose'):
		    		text('Unspecified')
		    	with tag('truncated'):
		    		text(0)
		    	with tag('difficult'):
		    		text(0)
		    	with tag('bndbox'):
		    		with tag('xmin'):
		    			text(int(b[4]))
		    		with tag('ymin'):
		    			text(int(b[5]))
		    		with tag('xmax'):
		    			text(int(b[6]))
		    		with tag('ymax'):
		    			text(int(b[7]))
	result = indent(
	    doc.getvalue(),
	    indentation = ' '*4,
	    newline = '\r\n'
	)
	fname = path+fname[:-4] + '.xml' #.split('.')[0] + '.xml'
	#print(fname)
	myfile = open(fname, "w")  
	myfile.write(result)
	myfile.close()

# ***************************************************
# Main function
# ***************************************************
image_csv = os.path.join(os.getcwd(), args.data_dir + '/'+ args.slidenumber + '/' + args.resolution+ '/')
print('path to csv:',image_csv)
df = pd.read_csv(image_csv+ args.resolution + '_' + 'labels.csv')

box = []
old_file = df.iloc[0,0]
print(len(df))
for i in range(0, len(df)):
	fname = df.iloc[i,0]
	if fname == old_file:
		box.append([df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4], df.iloc[i,5], df.iloc[i,6], df.iloc[i,7]])
	else:
		create_xml(old_file, box,image_csv)
		#print('done:',i,old_file)
		box = []
		box.append([df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4], df.iloc[i,5], df.iloc[i,6], df.iloc[i,7]])
	old_file = fname
create_xml(old_file,box,image_csv)
print('done: Kill the waves')
