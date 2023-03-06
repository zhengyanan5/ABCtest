import base.base_util
from time import sleep
import cv2
import ddddocr
from selenium.webdriver.common.by import By
from PIL import Image


class imagepro(object):
    def __init__(self,driver):
        self.Image=Image
        self.driver = driver

    def cro(self):
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[3]/div/span/img')
        # element.screenshot("element.png")
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = left + element.size['width']
        bottom = top + element.size['height']
        # print(left, top, right, bottom)

        im = self.Image.open('screen.png')
        im = im.crop((left, top, right, bottom))
        im.save('screen.png')

    # def reco(self):
        img = cv2.imread('screen.png')

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if (img[i, j, 0] / (float(sum(img[i, j, :]))) < 0.36):
                    img[i, j, :] = 255

        cv2.imwrite('screen.png', img)

        # cv2.waitKey(0)
        Image = cv2.imread('screen.png')

        gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('result3.png',gray)
        # cv2.waitKey(0)
        cv2.imwrite('screen.png', gray)

        # cv2.waitKey(0)
        image1 = cv2.imread("screen.png")

        # 灰度化处理
        image1_1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

        cv2.imwrite("screen.png", image1_1)

        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    # def save(self):
        # 识别保存的图片
        det = ddddocr.DdddOcr()
        with open('screen.png', 'rb') as f:
            image = f.read()
        # poses = det.detection(image)
        result = det.classification(image)
        # print(result)
        return result


if __name__=='__main__':
    imagepro().cro()
