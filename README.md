# Pneu-UFO
<p align='center'>
<img src='https://images-2018.spaceappschallenge.org/team-photos/0-2STD6RzuMnRZwtpO4sh5NoWR8=/11913/width-800/'/>
</p>

As a part of the Nasa Space Apps Challenges 2018, I participated in a challenge to **design an effective and efficient solution using mother nature to build an autonomous operations sequence for imaging and controlling a free-flyer to detect and characterize MMOD (Micrometeoroid and Orbital Debris) damage on spacecraft surface.**

My contribution to a solution is an autonomous free flyer that uses pneumatic thrust forces for motion to orbit the spaceship while transmitting a live feed of the surface that is analyzed for surface damage using deep learning neural networks. You can inspect the mother nature aspect in this as it’s analogous to an eagle looking for a prey. We call it “Pneu-UFO” !

We use **transfer learning** to build an image classification model that analyzes frames feed from the camera for damage severity. Transfer learning is a machine learning technique that utilizes a pre-trained model. While there are a lot of pre-trained models to work with out there, we chose to work with **RESNET18 model.**
This network is 18 layers deep (hence the name) and can classify images into 1000 general object classes. To generalize this model to our task we remove the last classifier layer (the one with 1000 neurons, i.e. softmax layer) and add instead a layer that classifies images into **4 classes only (No damage, Low damage, Medium damage, High damage).** 


## Dataset
The main challenge that we faced was the dataset itself, where the competition didn’t provide any specific dataset for the problem, so we had to collect and build our own dataset by utilizing other surface defect datasets we found. The one we chose to use is the **NEU surface defect database.** We found four types of surface damage that is of interest to us from the dataset:  Crazing, Inclusion, Patches and Pitted. Then, using these images we built the dataset for our four classes taking care of class balance while generating them.

We **open-source** this modified dataset version from NEU DET dataset here as well.

## Results 
Used accuracy as our metric, achieved a **test total accuracy (overall classes) of 96.8%.**

## Team Acknolwedgments
- Omar Mohamed Swidan [Github](https://github.com/oswidan97)
- Rami Mohamed Khafagi [Github](https://github.com/ramikhafagi96)
- Abdallah Amr Elmaradny [Github](https://github.com/abdallahmaradny)
- Mahmoud Saeed Ibrahim

## References
1. *K. Song and Y. Yan, “A noise robust method based on completed local binary patterns for hot-rolled steel strip surface defects,” Applied Surface Science, vol. 285, pp. 858-864, Nov. 2013.(paper)*

2. *Yu He, Kechen Song, Qinggang Meng, Yunhui Yan, “An End-to-end Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features,” IEEE Transactions on Instrumentation and Measuremente,  2019.(paper)*

3. *Hongwen Dong, Kechen Song, Yu He, Jing Xu, Yunhui Yan, Qinggang Meng, “PGA-Net: Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection,” IEEE Transactions on Industrial Informatics,  2020.(paper)*

4. *[Transfer Learning for Computer Vision Tutorial with PyTorch](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)*
