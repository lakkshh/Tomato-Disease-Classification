# Tomatify - Tomato Disease Classification
There are many disease classification systems available for various crops like potato, cotton, etc. Even though India is the second-largest tomato-producing country globally and tomato is the most cultivated crop in India, I could not find a disease classification system for tomato leaves. Global production of tomato exceeds 180 million tons and is an important nutrition and calorie provider.

Tomato prooduction is threatened by deveral diseases resulting in considerable yield losses, causing decrease in the quality and increase in the price of tomatoes. An early disease detection system can aid in avoiding such cases. Moreover, it can provide the management of crop and can further prevent the further spread of diseases. Manually detecting and sorting tomatoes is difficuly, costly and time consuming, while computerized inspection may be more efficient and cost effective. 

Many plant diseases have distinct visual symptoms which can be used to identify and classify them correctly. In this project, I have developed a tomato disease classification algorithm which leverages these distinct appearances and the recent advances in computer vision made possible by deep learning. The algorithm uses a deep CNN, training it to classify the diseases into the following four disease classes:
- Early Blight
- Late Blight
- Septoria Leaf Spot
- Yellow Leaf Curl Virus

and a healthy tomato class. 

The dataset of images used in this project, containing tomato leaves of different shapes, sizes and diseases, can be viewed [here](https://www.kaggle.com/arjuntejaswi/plant-village). Apart from this, I have added more images from Google to each of the disease classes to make the model more efficient and robust. In the proposed CNN Architecture, there are six convolution layers with 32 filters in first layer and 64 filters in the remaining layers and six max-pool layers. The model took around 50K seconds (~12 hours) to train. The training accuracy is obtained to be 97.50% and testing accuracy is 97.17%.

### CNN Model Architecture
![CNN Model](https://i.ibb.co/X595PQR/nn.png "CNN Model")

### Python Notebook
The .ipynb notebook can be accessed [here](https://nbviewer.jupyter.org/github/lakkshh/Tomato-Disease-Classification/blob/main/training.ipynb)

### Novelty
There are many disease classification systems available for various crops like potato, cotton, etc. Even though India is the second-largest tomato-producing country globally and tomato is the most cultivated crop in India, I could not find a disease classification system for tomato leaves. The diseases can cause considerable yield losses, decrease in the quality and increase in the price of tomatoes.. Hence, I have built this project which will help in early disease detection and prevent the further spread of diseases.

- Built the CNN Model from scratch and Hyper-Parameter Tuning
    - Built the CNN model from scratch using trial and error for the number of convolution layers and max-pool layers, train-test split ratio, filter size, epochs etc. thus, achieving a test accuracy of 97.17%.
- Optimizations
    - Downloaded and added images to the existing dataset to make it more robust
    - Built a tensorflow input pipeline and created equal sized 32 batches to handle the large dataset and optimize performance
    - Used concepts of caching, shuffling and prefetching to optimize the tensorflow input pipeline performace while handling the large dataset
    - Applied Data Augmentation to generate new training examples from exisiting training set using transformations like Flipping and Roation to prevent overfitting and increase robustibility

### I/O Screenshots
- Home Page Layout
![Layout 1](https://i.ibb.co/XzwxQkm/1-Home-Page-Layout-1.png "Layput 1")
![Layout 2](https://i.ibb.co/c3CJsHR/2-Home-Page-Layout-2.png "Layput 2")

- Upload Image
![Upload Image](https://i.ibb.co/sHPcddn/3-Upload-Image.png "Upload Image")

- Predictions
![Prediction 1](https://i.ibb.co/h92FZB8/4-Prediction-1.png "Prediction 1")
![Prediction 2](https://i.ibb.co/yP4DzWG/5-Prediction-2.png "Prediction 2")
![Prediction 3](https://i.ibb.co/Pxd95SV/6-Prediction-3.png "Prediction 3")
![Prediction 4](https://i.ibb.co/ZBh87Xz/7-Prediction-4.png "Prediction 4")


### Methodology Flow Chart
![Methodology](https://i.ibb.co/dM3ZPDx/Add-a-heading-1.png "Methodology")

### Mobile Android Application
[Click here](https://youtu.be/6HXnuD_sHyU) to watch the video.
