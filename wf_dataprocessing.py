# Author : Manohar Akula
# Date: 10/25/22
# Project - Data Munging and Visualisation Assignment


from xml.dom import minidom
import glob
import os
import matplotlib.image as mpimg
import csv
import random


def convert(box):
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (box[0],box[3]-h,w,h)



def pre_process(lut):
    print("Pre Processing will take 2 to 3 minutes.......")
    red_pixels_dirt = []
    green_pixels_dirt = []
    blue_pixels_dirt = []
    red_pixels_water = []
    green_pixels_water = []
    blue_pixels_water = []
    for imgpath in glob.glob("data_original/img/*.png"):
        #print(imgpath)
        fname = "data_original/xmls/"+imgpath.split("\\")[1].split(".")[0] +".xml" 
        #print(imgpath)
        img = mpimg.imread(imgpath)
        R_channel = img[:,:,0]
        G_channel = img[:,:,1]
        B_channel = img[:,:,2]
        #print(R_channel.dtype)
        if os.path.isfile(fname): 
            xmldoc = minidom.parse(fname)
            fname_out = (fname[:-4] + '.txt')
            with open(fname_out, "w") as f:
                itemlist = xmldoc.getElementsByTagName('object')
                size = xmldoc.getElementsByTagName('size')[0]
                width = int((size.getElementsByTagName('width')[0]).firstChild.data)
                height = int((size.getElementsByTagName('height')[0]).firstChild.data)

                for item in itemlist:
                    # get class label
                    classid = (item.getElementsByTagName('name')[0]).firstChild.data
                    if classid in lut:
                        label_str = str(lut[classid])
                    else:
                        label_str = "-1"
                        print("warning: label '%s' not in look-up table" % classid)

                    # get bbox coordinates
                    xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                    ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                    xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                    ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data

                    if random.randint(0, 20) ==  2:
                        if classid =="Water":
                            red_pixels_water.append(R_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            blue_pixels_water.append(B_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            green_pixels_water.append(G_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
                        else:
                            red_pixels_dirt.append(R_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            blue_pixels_dirt.append(B_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            green_pixels_dirt.append(G_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
    with open("data_processing\\cropped_water\\red_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(red_pixels_water)
    with open("data_processing\\cropped_water\\blue_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(blue_pixels_water)
    with open("data_processing\\cropped_water\\green_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(green_pixels_water)
    with open("data_processing\\cropped_dirt\\red_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(red_pixels_dirt)
    with open("data_processing\\cropped_dirt\\blue_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(blue_pixels_dirt)
    with open("data_processing\\cropped_dirt\\green_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(green_pixels_dirt)