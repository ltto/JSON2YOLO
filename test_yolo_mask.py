import cv2
import matplotlib.pyplot as plt
import numpy as np


def load_yolo_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    yolo_data = []
    for line in lines:
        line_data = line.strip().split()
        class_id = int(line_data[0])
        box_data = list(map(float, line_data[1:]))
        yolo_data.append({
            "class_id": class_id,
            "box_data": box_data
        })

    return yolo_data


yolo_data = load_yolo_data('/Users/ltt/ltto/PycharmProjects/JSON2YOLO/new_mask/test/labels/191.txt')

# 图像的宽度和高度
image_width = 1024
image_height = 768

# YOLO数据集的标注点（归一化坐标）
# yolo_contours = [0, 0.705078, 0.598958, 0.703125, 0.601562, ...]  # 使用你实际的数据替换这个列表
yolo_contours = yolo_data[0]["box_data"]  # 使用你实际的数据替换这个列表

# 将YOLO标注点的归一化坐标转换为像素坐标
contours = []
for i in range(0, len(yolo_contours), 2):
    x = int(yolo_contours[i] * image_width)
    y = int(yolo_contours[i + 1] * image_height)
    contours.append([x, y])

# 创建一个空的掩码
mask = np.zeros((image_height, image_width), dtype=np.uint8)

# 用标注点填充掩码
cv2.fillPoly(mask, np.array([contours], dtype=np.int32), 255)

# 显示掩码
plt.imshow(mask, cmap='gray')
plt.show()
