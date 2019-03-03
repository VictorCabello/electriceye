# -*- coding: utf-8 -*-
import cv2
from skimage.measure import compare_ssim

"""Main module."""
def image_diff(pathA, pathB):
    """
    Returns the diffferences of two images based on
    the mean structural similarity index between them.

    Prameters
    ---------
    pathA, pathB : ndarray
        Image.


    Returns
    ---------
    mssim : float
        The mean structural similarity over the image.
    S : ndarray
        The full SSIM image.
    """
    imgA = cv2.imread(pathA)
    imgB = cv2.imread(pathB)

    grayA = to_gray(imgA)
    grayB = to_gray(imgB)

    (mssim, full_ssim) = compare_ssim(grayA, grayB, full=True)

    thresh = cv2.threshold(full_ssim, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(imgA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imgB, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("diffs", imgB)
    cv2.waitKey(0)


def to_gray(img):
    """
    Retruns the image taken as agrument but in a gray scale
    """
    gray = cv2.ctvColor(img, cv2.COLOR_BGR2GRAY)
