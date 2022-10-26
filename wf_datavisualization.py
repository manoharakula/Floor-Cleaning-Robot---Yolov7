# Author : Manohar Akula
# Date: 10/25/22
# Project - Data Munging and Visualisation Assignment




from xml.dom import minidom
import glob
from matplotlib import image
from matplotlib import pyplot
import matplotlib.pyplot as plt
import os
import matplotlib.patches as patches
import matplotlib
import matplotlib.image as mpimg
import pandas as pd
import numpy as np
import csv
import random
import re
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot

def convert(box):
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (box[0],box[3]-h,w,h)

red_pixels_dirt = []
green_pixels_dirt = []
blue_pixels_dirt = []
red_pixels_water = []
green_pixels_water = []
blue_pixels_water = []
colors_water = []
colors_dirt  = []

images  = glob.glob("data_original/img/*.png")
images = sorted(images, key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
#print(images)



def xml_converter(lut):
    for imgpath in images:
        #print(imgpath)
        fname = "data_original/xmls/"+imgpath.split("\\")[1].split(".")[0] +".xml" 
        #print(imgpath)
        if random.randint(0, 20) ==  2:
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
                            #print("warning: label '%s' not in look-up table" % classid)

                        # get bbox coordinates
                        xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                        ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                        xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                        ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                        if classid =="Water":
                            red_pixels_water.extend([R_channel[i,j] for i in range(int(ymin),int(ymax)) for j in range(int(xmin),int(xmax))])
                            blue_pixels_water.extend([B_channel[i,j] for i in range(int(ymin),int(ymax)) for j in range(int(xmin),int(xmax))])
                            green_pixels_water.extend([G_channel[i,j] for i in range(int(ymin),int(ymax)) for j in range(int(xmin),int(xmax))])
                            colors_water.extend([(B_channel[i,j],G_channel[i,j],R_channel[i,j]) for i in range(int(ymin),int(ymax)) for j in range(int(xmin),int(xmax))])
                        else:
                            red_pixels_dirt.extend([R_channel[i,j] for i in range(int(ymin),int(ymax)) for j in range(int(xmin),int(xmax))])
                            blue_pixels_dirt.extend([B_channel[i,j] for i in range(int(ymin),int(ymax)) for j in range(int(xmin),int(xmax))])
                            green_pixels_dirt.extend([G_channel[i,j] for i in range(int(ymin),int(ymax)) for j in range(int(xmin),int(xmax))])
                            colors_dirt.extend([(B_channel[i,j],G_channel[i,j],R_channel[i,j]) for i in range(int(ymin),int(ymax)) for j in range(int(xmin),int(xmax))])






def quantitave():
    green_pixels = green_pixels_dirt 
    blue_pixels = blue_pixels_dirt
    red_pixels =  red_pixels_dirt
    cols={"red pixels":red_pixels,"blue pixles":blue_pixels,"green pixels":green_pixels}

    cols=pd.DataFrame(cols)
    cname=cols.columns
    savestr="\nQuanitative Analysis:\n"
    for i in cname:
        savestr+="For "+i+":\n"
        minv=cols[i].min()
        maxv=cols[i].max()
        medv=cols[i].median()
        savestr+="Min Value = "+str(minv)+"\nMax Value="+str(maxv)+"\nMedian="+str(medv)+"\n"
    with open("data_processing/summary.txt",'a') as f:
        f.writelines(savestr)
    corMatrix=np.zeros((3,3))
    for i in range(3):
        for j in range(i,3):
            corMatrix[i][j]=cols[cname[i]].corr(cols[cname[j]])
    print(corMatrix)
    np.savetxt("data_processing/correlation.txt",corMatrix)
    for i in range(3):
        for j in range(i+1,3):
            plt.scatter(cols[cname[i]], cols[cname[j]])
            name=cname[i]+" vs " +cname[j]+ " for Dirt class"
            plt.title(name)
            plt.xlabel(cname[i])
            plt.ylabel(cname[j])
            plt.savefig("visuals/"+name+".png" , dpi=90, bbox_inches='tight')
            plt.show()
            plt.cla()


def qualitative(lut):
    
    aspect_water = []
    aspect_dirt = []
    times_dirt = 0
    times_water = 0
    for imgpath in images:
        area_water = 0
        area_dirt = 0
        fname = "data_original/xmls/"+imgpath.split("\\")[1].split(".")[0] +".xml" 
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
                        #print("warning: label '%s' not in look-up table" % classid)

                    # get bbox coordinates
                    xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                    ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                    xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                    ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                    b = [float(xmin), float(xmax), float(ymin), float(ymax)]
                    x,y,w,h = convert(b)
                    if classid =="Water":
                        area_water+=((w*h)/(640*480))
                        times_water+=1
                    else:
                        area_dirt+=((w*h)/(640*480))
                        times_dirt+=1
        aspect_dirt.append(area_dirt*100)
        aspect_water.append(area_water*100)
    #print(aspect_dirt,aspect_water)
    fig = plt.figure(figsize =(10, 7))
    plt.bar(range(len(aspect_dirt)), aspect_dirt)
    plt.title("Aspect Ratio of Dirt across Dataset")
    fig.savefig("visuals/aspect_ratio_dirt.png" , dpi=90, bbox_inches='tight')
    plt.tight_layout()
    plt.show()
    plt.close(fig)

    fig = plt.figure(figsize =(10, 7))
    plt.bar(range(len(aspect_water)), aspect_water)
    plt.title("Aspect Ratio of Water across Dataset")
    fig.savefig("visuals/aspect_ratio_water.png" , dpi=90, bbox_inches='tight')
    plt.tight_layout()
    plt.show()
    plt.close(fig)

    fig = plt.figure(figsize =(10, 7))
    plt.bar(range(2), [times_dirt,times_water])
    plt.xticks(range(2) , ["Occurances of Dirt" , "Occurances of Water"])
    lfc = min(times_dirt,times_water)
    mfc = max(times_dirt,times_water)
    savestr="Qualitative Analysis:\n  Class across dataset :least frequent = Water, "+str(lfc)+" times \n most frequent = dirt, "+str(mfc)+" times"
    with open("data_processing/summary.txt",'w') as f:
        f.writelines(savestr)
    
    plt.title(f"Occurances of Class across dataset \n least frequent = Water, {lfc} times \n most frequent = dirt, {mfc} times \n no of classes = 2 ")
    fig.savefig("visuals/class_distribution.png" , dpi=90, bbox_inches='tight')
    plt.tight_layout()
    plt.show()
    plt.close(fig)

def visual(lut):
    print("Reading xml files")
    xml_converter(lut)
    print("Coerelation Matrix for RGB Values:")
    qualitative(lut)
    quantitave()

