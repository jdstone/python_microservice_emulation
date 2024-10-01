# AUTHOR: JD Stone
# Date: 9/28/2024
# FILENAME: ui.py

import time


prng_file = "prng-service.txt"
image_file = "image-service.txt"

while True:
    userInput = input("Type 'r' to start or 'q' to quit: ")
    if userInput.lower() == "r":
        f = open(prng_file, 'w')
        f.write("run")
        f.close()

        time.sleep(2.0)

        f = open(prng_file, 'r')
        body = f.read()
        f.close()

        f = open(image_file, 'w')
        f.write(str(body))
        f.close()

    elif userInput.lower() == "q":
        quit()

    else:
        print("Unknown command")
