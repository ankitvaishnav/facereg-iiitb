# facereg-iiitb
This repository is for tracking iiitb face recognition project

 faiss1.pynb:
 
 used google colab(with gpu enabled)

training images are in   face_recognition/faces folder,
query images are in      face_recognition/test folder

1. for installing faiss

!wget https://anaconda.org/pytorch/faiss-gpu/1.2.1/download/linux-64/faiss-gpu-1.2.1-py36_cuda9.0.176_1.tar.bz2
!tar xvjf faiss-gpu-1.2.1-py36_cuda9.0.176_1.tar.bz2
!cp -r lib/python3.6/site-packages/* /usr/local/lib/python3.6/dist-packages/
!pip install mkl

2. for installing mtcn

!pip install mtcnn

3. facenet_keras.h5  downloaded from
https://drive.google.com/drive/folders/12aMYASGCKvDdkygSv1yQq8ns03AStDO_

4. Here three query images are used. If none of the query images are invalid, then we can run the cells as it is. If there are any Invalid images we have to manually take care of the last three cells which displays the query images along with predicted name.

If we display the indices returned by index.search

array([[ 0],       indices[0][0]  index of nearest neighbor for query image1
       [22],       indices[1][0]  index of nearest neighbor for query image2
       [14]])      indices[2][0]  index of nearest neighbor for query image3

For suppose if query image 1 is invalid then

#query image2
dist2 = euclid_distance(1)---------->changes to euclid_distance(0) 
if dist2 < 10:
name2 = file_names[indices[1][0]]---->changes to indices[0][0]
else:
name2 = "unknown"
show_image(q_image2, name2) 


apart from this everything is well commented.

references
https://github.com/ageitgey/face_recognition/blob/master/face_recognition/api.py       refered compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):  function for including euclidean distance between face encodings.
