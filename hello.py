#!/usr/bin/env python
# coding: utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

class DetectFace():
    '''
    This class will detect the face in an image.
    '''
    def __init__(self, cascade='asset/haarcascade_frontalface_default.xml'):
        '''
        NOTE: you need to create the 'asset' directory.
        
        Params:
            cascade: the haarcascade xml file path.
        '''
        self.xml = cascade
        self.detector = cv2.CascadeClassifier(self.xml)
    
    def detect(self, imgs):
        '''
        Params:
            imgs : numpy ndarray (m, h, w, c)
        Return:
            list: list of ndarray or None
        '''
        # Check if the image is None.
        if imgs is None : return None

        # Check if the img is 3 dims.
        assert img.ndim == 4

        # Create the results list
        face_list = []

        for img in imgs:

            # Convert RGB to GRAY
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Detect face
            faces = self.detector.detectMultiScale(gray)

            # Check if there is any face.
            if faces.any():
                x, y, w, h = faces[0]
                face = img[y:y+w, x:x+h]
                # Resize to 128X128
                face128 = cv2.resize(face, (128,128))
                face_list.append(face128)
            else:
                face_list.append(None)
        
        return face_list
