## Exploratory Data Munging and Visualization
#### Dirt and Object Detection for floor cleaning Robots
#### Manohar Akula
#### October 25,2022
 
## Basic Questions
**Dataset Author(s):** Flobot Perception Dataset
 
**Dataset Construction Date:** 2018-06-13
 
**Dataset Record Count:** 2174 (640*480 resolution)
 
**Dataset Field Meanings:**
Supermarket pilot location, which has dirt and water on the floor. There are 1571 images with dirt or dirt with water, and 603 images with a clean floor.

Dirt - It refers to various items on the floor, such as coffee, chips, papers, curd, milk, soda, and so on.
Water - It defines the water droplets on the floor.

Resolution: The screen resolution is a measurement of how many pixels your screen can display horizontally and vertically
 
**Dataset File Hash(es):** 
certutil -hashfile data_original.zip MD5                         
MD5 hash of data_original.zip:                                                                                          0aeba0328907c239745daf6d96c1667d         
## Interpretable Records(after pre process)
### Record 1

**Raw Data:** Image - 2.xml (Annotated xml)
<annotation>
	<folder>floor-cleaning-annotated</folder>
	<filename>2.png</filename>
	<path>/floor-cleaning-annotated/2.png</path>
	<source>
		<database>Unspecified</database>
	</source>
	<size>
		<width>640</width>
		<height>480</height>
		<depth>3</depth>
	</size>
	<object>
		<name>Water</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>270</xmin>
			<ymin>107</ymin>
			<xmax>390</xmax>
			<ymax>172</ymax>
		</bndbox>
	</object>
</annotation>
 
Interpretation:** Since I'm using the image dataset it's not possible to extract the records from the tabular data. So, I annotated each image with 2 classes such as "Water" and "Dirt". Later, converted them into the XML file. The above raw XML file points about the Water class in a 640*480 resolution image with a single boundary box contain values of xmin = 270, ymin = 107, xmax>390, and ymax = 172. In-addition, the R, G, and B channels of the specific class is extraxted to find the co-releation between them.


### Record 2

**Raw Data:** Image - 1200.xml (Annotated xml)
<annotation>
	<folder>floor-cleaning-annotated</folder>
	<filename>1200.png</filename>
	<path>/floor-cleaning-annotated/1200.png</path>
	<source>
		<database>Unspecified</database>
	</source>
	<size>
		<width>640</width>
		<height>480</height>
		<depth>3</depth>
	</size>
	<object>
		<name>Dirt</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>117</xmin>
			<ymin>107</ymin>
			<xmax>279</xmax>
			<ymax>196</ymax>
		</bndbox>
	</object>
	<object>
		<name>Dirt</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>170</xmin>
			<ymin>241</ymin>
			<xmax>294</xmax>
			<ymax>318</ymax>
		</bndbox>
	</object>
	<object>
		<name>Dirt</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>151</xmin>
			<ymin>351</ymin>
			<xmax>258</xmax>
			<ymax>471</ymax>
		</bndbox>
	</object>
	<object>
		<name>Dirt</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>50</xmin>
			<ymin>226</ymin>
			<xmax>140</xmax>
			<ymax>379</ymax>
		</bndbox>
	</object>
</annotation>
 
**Interpretation:**
The above raw XML file points about the Dirt class in a 640*480 resolution image with multiple boundary boxes contain values of 
boundary box - 1: xmin = 117, ymin = 107, xmax = 279, and ymax = 196. 
boundary box - 2: xmin = 170, ymin = 241, xmax = 294, and ymax = 318.
boundary box - 3: xmin = 151, ymin = 351, xmax = 258, and ymax = 471.
boundary box - 4: xmin = 50, ymin = 226, xmax = 140, and ymax = 379.

These 4 boundary boxes provides the R, G, B channel values of each boundary box of the specific class. This extraxted values help to find out the co-releation between them.
 
 
## Data Sources
### Transformation 1
**Description:** https://owncloud.tuwien.ac.at/index.php/s/h8ZDeypUJoRFmb4 This is an image dataset consists of dirt and water on the floor. Extracting the pixel value of each image doesn't helps to identify the differnt classes on the floor for a floor cleaning robot.

 
**Soundness Justification:**  I manually annotated the whole dataset into 2 classes such as "Water" and "Dirt" using an annotation tool  https://www.makesense.ai/ to identify the different classes on the floor, it took me around 3 days to label them. The annotation is being done on each image with multiple boundary boxes. These boundary boxes consits of either water or dirt and provides the minimum & maximum values of x, y cordinates on the whole image. Later, I converted the boundary box values of each image in to the XML file. These xml files were saved in the data original. Later, for preprocessing the xml files were used to label the raw data and saved inside the preprocessed.  


## Visualization
### Visual 1 (Aspect Ratio of dirt across the dataset)
**Analysis:** The aspect ratio of dirt across the dataset was laid from image 0 to image 1571, with the largest aspect ratio (area) existing between the 1075 to 1100 images, as seen in the graph. The dirt is absent in the images from 1571 to 2172, as shown by the graph.
 
### Visual 2 (Aspect Ratio of Water across the dataset)
**Analysis:** The aspect ratio of dirt across the dataset was laid from image 0 to image 1100, with the largest aspect ratio (area) existing between the 800 and 1156 images, as seen in the graph. The Watert is missing from images 1157 to 2172, as evidenced by the graph.

### Visual 3 (Class Distribution)
**Analysis:** As it can be seen from the plot the occurances of each class i.e., Water and Dirt across the dataset. It's clearly says that the Dirt class has the highest distribution across the dataset followed by the Water class.

### Visual 4 (Blue pixels vs Green Pixels for Dirt Class)
**Analysis:** This graph clearly demonstrating the corelation of Blue pixels & Green pixels for the Dirt class.

### Visual 5 (Red Pixels vs Blue Pixels for Dirt Class)
**Analysis:**  This graph clearly demonstrating the corelation of Red pixels & Blue pixels for the Dirt class.

### Visual 6 (Red Pixels vs Green Pixels for Dirt Class)
**Analysis:**  This graph clearly demonstrating the corelation of Red pixels & Green pixels for the Dirt class.

