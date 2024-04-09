## A project to convert PointCloud into FE Models

#### LJF's personal graduation project

## Log
### 2024/2/20
- Finish the Clustering of PointCloud (into 3 parts, after coordinate changing process)
 
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/clustering_result.png#pic_center)


- Finish the Plane-Fitting

![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/output.png#pic_center)  


- Finish the coordinate changing

![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/cloud_compare.jpg#pic_center)   

  - upper is the unchanging one, while the other one is the pointclouds after coordinate processing


### 2024/2/21
- Find the intersection line of 2 planes (plane1 & plane2 / plane2 & plane3)

![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/intersection_line.png#pic_center)

- Slicing the surface

![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/surface_slicing.png#pic_center)  
  - the upper one is the example of slicing the whole model, but somehow, in this project, we tried to slice the planes individually.  

![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/parts.png#pic_center)  
  - this one is the model after sliced in 2 different directions (use plane3 as the example)

- TRY to find the centroid point of three planes
  - FAILED when the slicing densely, since may caused by the pointclouds are a little bit sparse when we trying to slice in a short distance. 

### 2024/2/22
- Finally, we get the centroid point of each parts.
 - With some small tricks (Group by the points by using pandas)
 - Here is the comparison between the org model (after rotated) and the centroid points (the gap_distance is 0.5m, not too dense because it takes plenty of time for matching the org.csv file with the splitted.csv file ----> 30m' each)
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/centroid_shu.png#pic_center)
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/org_point.png#pic_center)

- Also, we add some points in the intersection points to made 3 parts undivided  
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/add_extra_points.png#pic_center)

- In the end, we can use meshlab to convert the pointclouds into the mesh
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/meshlab.png#pic_center)

#### However, a serious problem is how to change the mesh(.obj/.stl) into the FE-Model??????

### 2024/2/27
#### FINALLY, WE MADE SOME ARTS (LOL)
- Based on the fact that it's a hard task for converting the .stl file into the .sat file or other kinds of types which can be read in ANSYS APDL, I finally made the decision that to mesh the model in ansys. lol
- We create a folder "generate_FE_model", which we mainly to the following steps based on the centroid points we found before.
 - 1) Add id columns for each centroid point of the 3 planes
 - 2) Reconstruct the plane by using "Ball Pivoting Algorithm" (BPA), so damn cool (in python)
 - 3) Refind which 3 nodes construct into a full “triangle mesh patch” ----> use another .csv file to store the information
 - 4) Write the above inf. to ANSYS APDL (USE PLANE63 to simulate)

- THE RESULTS ARE AS FOLLOWING:
 - the meshing model:
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/ansys_model_after_meshing.png#pic_center)
 - Comparison between the model after calculation & the former one:
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/ansys_all_result.png#pic_center)


## By this, we finish the Pt2FE model_v1

### 2024/2/28
- we can add the beam section into our model, like the following shows:
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/add_beam_0.png#pic_center)
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/add_beam_1.png#pic_center)

### 2024/2/29
- In addition, we can cpoy the single part into several parts to combine into a real status, here is what we got.
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/8kua.png#pic_center)  
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/8kua_2.png#pic_center)  
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/demo_version1/pictures/8kua_fu.png#pic_center)

- P.S. : the hardware that I use in this project is MSI-z790+intel 13700kf+Nvidia 4060ti(16g). Also gpu is useless in this work, but somehow, a single run with in ansys would cost about 10 min.


## Now, I am going to write an automatic version. (Starts from 2024/3/28)
### 2024/4/2 (v4.1)
- First version of demo.ipynb has finished.

### 2024/4/3 (v6)
- We change the idea of the coordinate transformation step
    - we use the PCA to find the main direction of the point clouds
    - define which point in the org_data is going to move to the (0,0,0)
    - Execute the transformation step with the above rules
 
