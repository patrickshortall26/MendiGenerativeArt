from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt

MENDI_CORAL = (242,166,127)

def read_in(folder_name):
    """
    Read in each screenshot and return a list of image arrays
    """
    image_arrays = []
    for image_fp in os.listdir(folder_name):
        image = Image.open(folder_name + image_fp)
        image_arrays.append(np.array(image))
    return image_arrays

def find_coral_bar(image):
    """
    Find the y-position of the top of the coral bar
    """
    # Get Y coordinates of all coral coloured pixels
    y_s, __ = np.where(np.all(image==MENDI_CORAL,axis=2))
    y_top = np.min(y_s)
    return y_top


def crop(image_arrays):
    """
    Crop the graph section of each image array
    """
    cropped_image_arrays = []
    for image_array in image_arrays:
        # Find the position of coral bar
        y_cb = find_coral_bar(image_array)
        # Crop the graph from the array
        cropped_image_array = image_array[y_cb+240:y_cb+560,80:665,:]
        cropped_image_arrays.append(cropped_image_array)
    return cropped_image_arrays

def arrs_2_imgs(image_arrays):
    """
    Convert image_arrays back to images
    """
    images = []
    for image_array in image_arrays:
        image = Image.fromarray(image_array)
        images.append(image)
    return images

def save_cropped_images(images):
    """
    Saved cropped images to a new folder
    """
    folder_name = "Cropped_graphs/"
    os.makedirs(folder_name, exist_ok=True)
    for idx, image in enumerate(images):
        image.save(f"{folder_name}graph{idx}.png")

def main():
    # Read in all the images from the screenshot folder
    image_arrays = read_in("Screenshots/")
    # Crop the graph section of each image
    graph_image_arrays = crop(image_arrays)
    # Convert the arrays back into image objects
    graph_images = arrs_2_imgs(graph_image_arrays)
    # Save images of graphs into new folder
    save_cropped_images(graph_images)

if __name__ == "__main__":
    main()

