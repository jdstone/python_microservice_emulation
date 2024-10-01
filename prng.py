# AUTHOR: JD Stone
# Date: 9/28/2024
# FILENAME: prng.py

import random, os


prng_file = "prng-service.txt"

if not os.path.isfile(prng_file):
    f = open(prng_file, 'w')
    f.close()

while True:
    f = open(prng_file, 'r+')
    body = f.read()

    num = round(random.uniform(1,5))

    if body == "run":
        f.truncate(0) # erase file
        f.close()
        f = open(prng_file, 'w')
        f.write(str(num))
        f.close()
        print("Process completed")
