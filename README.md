## A project to convert PointCloud into FE Models

#### LJF's personal graduation project

## Log
#### 2024/2/20
- Finish the Clustering of PointCloud (into 3 parts, after coordinate changing process)
 
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/pictures/clustering_result.png#pic_center)


- Finish the Plane-Fitting

![image](https://github.com/StonecoldLi/Pt2FE/blob/master/pictures/output.png#pic_center)  


- Finish the coordinate changing

![image](https://github.com/StonecoldLi/Pt2FE/blob/master/pictures/cloud_compare.jpg#pic_center)   

  - upper is the unchanging one, while the other one is the pointclouds after coordinate processing


#### 2024/2/21
- Find the intersection line of 2 planes (plane1 & plane2 / plane2 & plane3)

![image](https://github.com/StonecoldLi/Pt2FE/blob/master/pictures/intersection_line.png#pic_center)

- Slicing the surface

![image](https://github.com/StonecoldLi/Pt2FE/blob/master/pictures/surface_slicing.png#pic_center)  
  - the upper one is the example of slicing the whole model, but somehow, in this project, we tried to slice the planes individually.  

![image](https://github.com/StonecoldLi/Pt2FE/blob/master/pictures/parts.png#pic_center)  
  - this one is the model after sliced in 2 different directions (use plane3 as the example)

- TRY to find the centroid point of three planes
  - FAILED when the slicing densely, since may caused by the pointclouds are a little bit sparse when we trying to slice in a short distance. 

#### 2024/2/22
- Finally, we get the centroid point of each parts.
 - With some small tricks (Group by the points by using pandas)
 - Here is the comparison between the org model (after rotated) and the centroid points (the gap_distance is 0.5m, not too dense because it takes plenty of time for matching the org.csv file with the splitted.csv file ----> 30m' each)
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/pictures/centroid_shu.png#pic_center)
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/pictures/org_point.png#pic_center)

<<<<<<< HEAD
- Also, we add some points in the intersection points to made 3 parts undivided  
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/pictures/add_extra_points.png#pic_center)

- In the end, we can use meshlab to convert the pointclouds into the mesh
![image](https://github.com/StonecoldLi/Pt2FE/blob/master/pictures/meshlab.png#pic_center)

#### However, a serious problem is how to change the mesh(.obj/.stl) into the FE-Model??????
=======
>>>>>>> 7e6a5e8116cb40e58dd8824f9e436868afd27a97
