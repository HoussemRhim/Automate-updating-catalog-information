#!/usr/bin/env/ python3

import requests, os
# URL to ulpoad the images
url = "http://localhost/upload/"
# To get username from environment variable
USER = os.getenv('USER')
# The directory which contains all the images
image_directory = '/home/{}/supplier-data/images/'.format(USER)
#Listing all the files in images directory
files = os.listdir(image_directory)
# Parsing through all the images
for image_name in files:
    # accepting files that has jpeg extension and ignoring hidden files
    if not image_name.startwith('.') and 'jpeg' in image_name:
        # creating absolute path for each image
        image_path = image_directory + image_name
        # uploading jpeg files
        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
