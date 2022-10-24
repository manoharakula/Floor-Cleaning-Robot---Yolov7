from xml.dom import minidom
import glob
from matplotlib import image
from matplotlib import pyplot
import matplotlib.pyplot as plt
import os
import matplotlib.patches as patches
import matplotlib
import matplotlib.image as mpimg
from wf_core import convert
import numpy as np
import csv
import random
import re


lut={}
lut["Dirt"] = 0
lut["Water"] = 1


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
print(images)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot

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

            fig, ax = plt.subplots()
            plt.axis('off')
            ax.imshow(img)
            #print(fname)
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
                        rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor='none')
                        ax.add_patch(rect)
                        ax.text(x,y, classid)
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
            plt.close(fig)
            print("wrote %s" % fname_out) 
xml_converter(lut)


def plot_3d():
    
    fig = plt.figure()
    plt.title("Scatter plot for Water")
    axis = fig.add_subplot(1, 1, 1, projection="3d") # 3D plot with scalar values in each axis
    axis.scatter(red_pixels_water, green_pixels_water, blue_pixels_water, color =np.array(colors_water), marker="o")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")
    fig.savefig("data_visuals/scatter_plot_water.png" , dpi=90, bbox_inches='tight')
    plt.tight_layout()
    # plt.show()
    plt.close(fig)

    fig = plt.figure()
    plt.title("Scatter plot for Dirt")
    axis = fig.add_subplot(1, 1, 1, projection="3d") # 3D plot with scalar values in each axis
    axis.scatter(red_pixels_dirt, green_pixels_dirt, blue_pixels_dirt, color =np.array(colors_dirt), marker="o")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")
    fig.savefig("data_visuals/scatter_plot_dirt.png" , dpi=90, bbox_inches='tight')
    plt.tight_layout()
    # plt.show()
    plt.close(fig)
plot_3d()

def plot_hist():
    green_pixels = green_pixels_water 
    blue_pixels = blue_pixels_water
    red_pixels =  red_pixels_water

    #print(green_pixels[0][0].split(" "))
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
    axes = axes.ravel()

    for pix, color, ax in zip([red_pixels, green_pixels, blue_pixels], ['red', 'green', 'blue'], axes):
        n, bins = np.histogram(pix)
        mids = 0.5*(bins[1:] + bins[:-1])
        mean = np.average(mids, weights=n)
        minh = np.min(mids)
        maxh = np.max(mids)
        median = np.median(mids)
        var = np.average((mids - mean)**2, weights=n)

        print("MEAN = ",mean,var)
        ax.hist(pix, bins=256, density=False, color=color, alpha=0.5)

        # set labels and ticks
        ax.set_xticks(ticks=np.linspace(0, 1, 17))
        ax.set_xticklabels(labels=range(0, 257, 16), rotation=90)

        # limit the y range if desired
        # ax.set_ylim(0, 10000)

        # set the scale to log
        ax.set_yscale('log')

        # Cosmetics
        ax.set_title(f'Histogram from channel {color} for Water Class \n Min =  {minh*256} \n Max = {maxh*256} \n Median = {median*256}')
        ax.set_ylabel('Counts')
        ax.set_xlabel('Intensity')
    fig.savefig("data_visuals/histogram_water.png" , dpi=90, bbox_inches='tight')
    plt.tight_layout()
    plt.show()
    plt.close(fig)

    green_pixels = green_pixels_dirt 
    blue_pixels = blue_pixels_dirt
    red_pixels =  red_pixels_dirt
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
    axes = axes.ravel()

    for pix, color, ax in zip([red_pixels, green_pixels, blue_pixels], ['red', 'green', 'blue'], axes):
        n, bins = np.histogram(pix)
        mids = 0.5*(bins[1:] + bins[:-1])
        mean = np.average(mids, weights=n)
        minh = np.min(mids)
        maxh = np.max(mids)
        median = np.median(mids)
        var = np.average((mids - mean)**2, weights=n)


        ax.hist(pix, bins=256, density=False, color=color, alpha=0.5)
        ax.set_xticks(ticks=np.linspace(0, 1, 17))
        ax.set_xticklabels(labels=range(0, 257, 16), rotation=90)
        ax.set_yscale('log')
        ax.set_title(f'Histogram from channel{color} for Dirt Class\n Min =  {minh*256} \n Max = {maxh*256} \n Median = {median*256}')
        ax.set_ylabel('Counts')
        ax.set_xlabel('Intensity')

    fig.savefig("data_visuals/histogram_dirt.png" , dpi=90, bbox_inches='tight')
    plt.tight_layout()
    plt.show()
    plt.close(fig)


plot_hist()

def plot_kxk():
    image_water = glob.glob("data_preprocessed/cropped_water/*.png")
    image_dirt = glob.glob("data_preprocessed/cropped_dirt/*.png")
    cnt = 0
    k = 10
    fig, axarr = plt.subplots(k,k)
    plt.axis('off')
    for i in range(k):
        for j in range(k):
            axarr[i,j].imshow(mpimg.imread(image_water[cnt]))
            axarr[i,j].set_axis_off()

            cnt+=1

    plt.show()
    fig.savefig("data_visuals\\water 10x10.png" , dpi=90, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

    cnt = 0
    fig, axarr = plt.subplots(k,k)
    plt.axis('off')
    for i in range(k):
        for j in range(k):
            axarr[i,j].imshow(mpimg.imread(image_dirt[cnt]))
            axarr[i,j].set_axis_off()
            cnt+=1

    plt.show()
    fig.savefig(f"data_visuals\\dirt 10x10.png" , dpi=90, bbox_inches='tight', pad_inches=0)
    plt.close(fig)


plot_kxk()
# Author : Manohar Akula
# Date: 10/23/22
# Project - Data Munging Assignment

def aspect_ratio_plotter(lut):
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
    print(aspect_dirt,aspect_water)
    fig = plt.figure(figsize =(10, 7))
    plt.bar(range(len(aspect_dirt)), aspect_dirt)
    plt.title("Aspect Ratio of Dirt across Dataset")
    fig.savefig("data_visuals/aspect_ratio_dirt.png" , dpi=90, bbox_inches='tight')
    plt.tight_layout()
    plt.show()
    plt.close(fig)

    fig = plt.figure(figsize =(10, 7))
    plt.bar(range(len(aspect_water)), aspect_water)
    plt.title("Aspect Ratio of Water across Dataset")
    fig.savefig("data_visuals/aspect_ratio_water.png" , dpi=90, bbox_inches='tight')
    plt.tight_layout()
    plt.show()
    plt.close(fig)

    fig = plt.figure(figsize =(10, 7))
    plt.bar(range(2), [times_dirt,times_water])
    plt.xticks(range(2) , ["Occurances of Dirt" , "Occurances of Water"])
    lfc = min(times_dirt,times_water)
    mfc = max(times_dirt,times_water)
    plt.title(f"Occurances of Class across dataset \n least frequent = Water, {lfc} times \n most frequent = dirt, {mfc} times \n no of classes = 2 ")
    fig.savefig("data_visuals/class_distribution.png" , dpi=90, bbox_inches='tight')
    plt.tight_layout()
    plt.show()
    plt.close(fig)


aspect_ratio_plotter(lut)

