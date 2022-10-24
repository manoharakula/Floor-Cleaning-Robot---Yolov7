# Author : Manohar Akula
# Date: 10/23/22
# Project - Data Munging Assignment
def convert(box):
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (box[0],box[3]-h,w,h)