# Author : Manohar Akula
# Date: 10/25/22
# Project - Data Munging and Visualisation Assignment


def data_gen():
    """This is a dummy function. But I'd want to show my peers how my data was generated into the xml file. I started with a raw data set of 2172 images.
    Which is made up of floor images with dirt and water. I annotated each image using https://www.makesense.ai/ to identify the dirt and water on the floor.
    I began manually labeling each image with two separate classifications, such as Water and Dirt. There is no automated tool that can appropriately categorize it  
    to obtain the best accuracy.

    I spent around three days labeling each image with a boundary box on the water and dirt. Later, I transformed the detection region into an XML file and 
    later, I used the extracted xml file to preprocess the raw dataset. 
    With a boundary box and label name, it highlights the dirt and water on the image. The findings may be found in the detection folder. """

    pass