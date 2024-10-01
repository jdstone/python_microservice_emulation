# AUTHOR: JD Stone
# Date: 9/28/2024
# FILENAME: image.py

import random, os


path = os.getcwd()

image_file = "image-service.txt"

if not os.path.isfile(image_file):
    f = open(image_file, 'w')
    f.close()

while True:
    f = open(image_file, 'r+')
    body = f.read()

    num = round(random.uniform(1,5))

    if body.isdigit():
        f = open(image_file, 'w')
        f.write("")
        for file in os.listdir(path):
            if file.endswith(f"{body}.svg"):
                f.truncate(0) # erase file
                f.write(f"{path}/{file}")
                f.close()
                print("Process completed")
