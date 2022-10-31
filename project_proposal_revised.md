#### SER594: Project Revised Proposal
#### Dirt and Water Detection for floor cleaning Robots  
#### Manohar Akula
#### 10/30/2022

#### Keywords
Floor cleaning, Image Classification, Machine Learning, Neural Networks, and Deep Learning.

#### Description
For this project, I will be using FLOBOT Perception Dataset which is collected by Flobot. I will use their datset to create my a model to detect the Dirt and Water on the floor and then proposes a vision system based on the CV frameworks. Classification models will be trained to identify the water and dirt.

#### Research Questions
<ol>
    <li>
        RO1: To describe the label trends within dataset to understand labels distribution and to determine whether the dataset is balanced or imbalanced.
    </li>
    <li>
        RO2: Regression: To predict the value of the boundary box corresponding to its respective class in an image.
        Classification: To predict the label of dirt and water inside the image data.
    </li>
    <li>
        RO3: To defend the model for performing the prediction of boundary boxes, to determine the corresponding labels with the performance metrices in RO2
    </li>
    <li>
        RO4: To evaluate causal relationships implied by the RO2 model and to distinguish the dirt and water classes from the boundary boxes.
    </li>
</ol> 



#### Intellectual Merit
Creating a Dirt and Water Detection model for floor cleaning Robots can help many floor cleaning robotic companies to become more autonomous, both in terms of their navigation skills but also in their capabilities of analyzing the surrounding environment. Most robot cleaners are incapable of sanitizing floors. If the correct cleanser is not utilized, cleaning off built-up dirt and debris has minimal effect on the quantity of bacteria and viruses that live on the surface. This model can classify the floor material and provide an input to the robot to modify the disinfection and strain removal liquids. Furthermore, giving an appropriate vision detection model can guide the robot to clean the filth region rather than the entire floor. This model may considerably minimize power consumption, floor cleaning and disinfection material, as well as assist in changing correct moping bases for hard dirt and water. The publications I discovered only focused on implementing deep learning models, with little explanation. This is why I want to construct several categorization algorithms and compare them to have a better understanding.

#### Data Sourcing
The data will be source from FLOBOT (Floor cleaning Robot) an European company http://lcas.github.io/FLOBOT/. The data has 2174 sample images inside the supermarket. In-addition, the dataset provided was just the images with the water and dirt on the floor. The images between 1 to 1572 has either water or water and dirt on the floor. To specify, the images containing dirt has the coffee, ice-cream, coke, and chips spilled over the floor. Furthermore, the images containing the water has just water spilled on the floor. Rest of 600 images has the clean floor. I manually labelled each image between 1 and 1572 with dirt and water classes to predict the material on the floor.

#### Related Work
Research papers I have found useful for this problem:  
<li>
[1]https://www.mdpi.com/2227-7080/9/4/94
    A Deep Learning-Based Dirt Detection Computer Vision System for Floor-Cleaning Robots with Improved Data Collection
</li>
<li>
[2]https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7601099/
    Automatic System for Visual Detection of Dirt Buildup on Conveyor Belts Using Convolutional Neural Networks
</li>
<li>
[3]https://ieeexplore.ieee.org/abstract/document/9196559?casa_token=BaCPmAM48Z0AAAAA:6JhLUZYEz6PMHzU4_SkpeMMqHiHR4qqyitGeB3-0mGUDcb34fhunuMhlaU590pHc829rSlM
    DirtNet: Visual Dirt Detection for Autonomous Cleaning Robots
</li>
<li>
[4]https://ieeexplore.ieee.org/abstract/document/6309494
    A Visual Dirt Detection System for Mobile Service Robots
</li>
<li>
[5]https://www.hindawi.com/journals/js/2018/3035128/
    Vision-Based Dirt Detection and Adaptive Tiling Scheme for Selective Area Coverage
</li>
   