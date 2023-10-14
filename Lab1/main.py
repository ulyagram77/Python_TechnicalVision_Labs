import cv2
import tkinter as tk
import os
from tkinter import filedialog
import matplotlib.pyplot as plt

img = None


# Функция для загрузки изображения
def load_image():
    global img
    file_path = filedialog.askopenfilename()
    if file_path:
        if os.path.isfile(file_path):
            img = cv2.imread(file_path, 1)  # Загружаем цветное изображение
            cv2.imshow('Your loaded image', img)
            show_histogram(img)


# Функция для сохранения изображения
def save_image():
    global img
    if img is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpeg")
        if file_path:
            cv2.imwrite(file_path, img)
            cv2.destroyAllWindows()
    else:
        print("Error.Image does not downloaded.")


def show_image():
    global img
    if img is not None:
        cv2.imshow('Your loaded image', img)
    else:
        print("Error.Image does not downloaded.")


def create_negative_image_first():
    global img
    if img is not None:
        # Display the original image
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()

        show_histogram(img)

        # Get height and width of the image
        height, width, _ = img.shape
        for i in range(0, height - 1):
            for j in range(0, width - 1):
                # Get the pixel value
                pixel = img[i, j]
                # Negate each channel by subtracting it from 255
                # 1st index contains red pixel
                pixel[0] = 255 - pixel[0]
                # 2nd index contains green pixel
                pixel[1] = 255 - pixel[1]
                # 3rd index contains blue pixel
                pixel[2] = 255 - pixel[2]
                # Store new values in the pixel
                img[i, j] = pixel

        # Display the negative transformed image
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()

        # Histogram plotting of the negative transformed image
        show_histogram(img)
    else:
        print("Error.Image does not downloaded.")


# Функция для создания негативной картинки через вычитание цветов
def create_negative_image_second():
    global img
    if img is not None:
        img_neg = 255 - img  # Инверсия цветов
        cv2.imshow('Your negative image', img_neg)
        show_histogram(img_neg)
    else:
        print("Error.Image does not downloaded.")


# Функция для построения гистограммы изображения
def show_histogram(image):
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
    plt.xlim([0, 256])
    plt.show()


# створення інтерфейсу
root = tk.Tk()
root.title("Загрузка и сохранение изображения")

load_button = tk.Button(root, text="Завантажити зображення", command=load_image)
save_button = tk.Button(root, text="Зберегти зображення", command=save_image)
show_button = tk.Button(root, text="Подивитись зображення", command=show_image)
create_negative_button_first = tk.Button(root, text="Створити негатив зображення циклічним методом",
                                         command=create_negative_image_first)
create_negative_button_second = tk.Button(root, text="Створити негатив зображення методом віднімання",
                                          command=create_negative_image_second)

load_button.pack()
save_button.pack()
show_button.pack()
create_negative_button_first.pack()
create_negative_button_second.pack()

root.mainloop()
