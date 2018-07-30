# a = ["a", "b", "c", "d", "e"]
# for idx, item in enumerate(a[:]):
#     print item
#     if item == "b":
#         a.remove(item)
# print(a)
# x = []
# print(len(x))
import itertools

a = [1,1,2,3,4,4,3,1]
# clusterList = []
# for idx, num in enumerate(a):
#     clusterList.append([])
#     for idx1, otherNum in enumerate(a):
#         if (num == otherNum):
#             clusterList[idx].append(otherNum)

# clusterList = list()
# clusterList2 = list()
# arr = list()
# for idx, num in enumerate(a):
#     clusterList.append([])
#     if not num in arr:
#         print(str(a) + "~~~~~~~~~~~")
#         for idx1, otherNum in enumerate(a):
#             if (num == otherNum):
#                 arr.append(otherNum)
#                 clusterList[idx].append(otherNum)
#                 # a.remove(a[idx1])
#             else:
#                 # clusterList.append([])
#                 print("printed")
#
#     print(str(a) + "Down~~~~")
#
# print(clusterList)
# clusterList.sort()
#
# print(list(clusterList for clusterList,_ in itertools.groupby(clusterList)))

# distinctList = list(clusterList for clusterList,_ in itertools.groupby(clusterList))

# import cv2
# import numpy as np
# from PIL import Image
#
# img = cv2.imread("images/face_12.jpg")
#
# # You may need to convert the color.
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# im_pil = Image.fromarray(img)
# # cv2.imshow(im_pil)
# # print(im_pil)
# im_pil.save('/1.jpg')
# faces = []
# faces.append({'face':'hello', 'number':'121'})
# print(faces[0]['face'])

arr = ['D:\\shubham\\facenet_face_recognition\\unsupervised-clustering-faces-tensorflow-master/my_img/face_150.jpg',
'D:\\shubham\\facenet_face_recognition\\unsupervised-clustering-faces-tensorflow-master/my_img/face_151.jpg',
'D:\\shubham\\facenet_face_recognition\\unsupervised-clustering-faces-tensorflow-master/my_img/face_150.jpg',
'D:\\shubham\\facenet_face_recognition\\unsupervised-clustering-faces-tensorflow-master/my_img/face_151.jpg',
'D:\\shubham\\facenet_face_recognition\\unsupervised-clustering-faces-tensorflow-master/my_img/face_29.jpg',
'D:\\shubham\\facenet_face_recognition\\unsupervised-clustering-faces-tensorflow-master/my_img/face_817.jpg']

if not 'D:\\shubham\\facenet_face_recognition\\unsupervised-clustering-faces-tensorflow-master/my_img/face_29.jpg' in arr:
    print('hello')
else:
    print('bye')
