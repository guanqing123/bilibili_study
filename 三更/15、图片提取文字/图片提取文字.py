# 图像处理! opencv-python
import cv2
# 文字处理 OCR
# Tesseract-OCR
import pytesseract

# 车牌识别 灰度图 二值化!
# 读取图片
image = cv2.imread(r'img.png')
# cv2.imwrite('src.png', image)

# 灰度图 把彩色去掉,把图片只剩下 黑白灰
# 颜色：自己想要掌控 32位的数据 00000000 00000000 00000000 00000000 像素点
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray.png', gray_image)

# 二值化
_, binary_iamge = cv2.threshold(gray_image, 10, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
cv2.imwrite('binary.png', binary_iamge)

# 识别
pytesseract.pytesseract.tesseract_cmd = r'D:\program files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(binary_iamge, lang='chi_sim')

print(text)



