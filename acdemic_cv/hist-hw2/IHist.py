import cv2
import numpy as np
from matplotlib import pyplot as plt


class HistogramProcess(object):

    def __init__(self, img):
        self.img = img
        self.hist, self.bins = np.histogram(img.flatten(), 256, [0, 256])
        self.cdf = self.hist.cumsum()

    def addNormalizedCDFOnPlot(self):
        cdf_normalized = self.cdf * self.hist.max() / self.cdf.max()
        plt.plot(cdf_normalized, color='b')

    def showHistogram(self, img=None):
        self.addNormalizedCDFOnPlot()
        if img == None:
            img = self.img
        plt.hist(img.flatten(), 256, [0, 256], color='r')
        plt.xlim([0, 256])
        plt.legend(('cdf', 'histogram'), loc='upper right')
        plt.show()

    def histogramEqualization(self):
        cdf_m = np.ma.masked_equal(self.cdf, 0)
        cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
        cdf = np.ma.filled(cdf_m, 0).astype('uint8')
        return cdf[self.img]


hp = HistogramProcess(cv2.imread('600px-Unequalized_Hawkes_Bay_NZ.jpg', 0))
hp.showHistogram()

img2 = hp.histogramEqualization()
hp.showHistogram(img2)
