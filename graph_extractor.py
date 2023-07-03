from PIL import Image
import os
import numpy as np
import json

MENDI_CORAL = (242,166,127)

def read_in(folder_name):
    """
    Read in each screenshot and return a list of image arrays
    """
    image_arrays = []
    for image_fp in os.listdir(folder_name):
        image = Image.open(folder_name + image_fp)
        image_arrays.append(np.array(image,dtype=np.int16))
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

def graph_mask(graph_images):
    """
    Extract the underlying data from the image of the graph
    """
    graph_data = []
    for graph_image in graph_images:
        # Filter image to select only the curve showing neural activity
        jumble_graph_image = graph_image[:,:,[2,0,1]]
        filt_image = np.abs(graph_image - jumble_graph_image)
        gscale = np.dot(filt_image[...,:3], [0.2989, 0.5870, 0.1140])
        finito = np.where(gscale > 10, 255, 0)
        # Get the indexes of all the non zero pixels (the line)
        x_idxs, y_idxs = np.nonzero(np.rot90(finito, 3, (0,1)))
        split_idxs = np.nonzero(np.insert(x_idxs, 0, 0)-np.append(x_idxs,0))[0][1:-1]
        y_pixels = np.split(y_idxs, split_idxs)
        # Take the median to reduce the data to just 1 value of neural activity for each timestep
        data = np.array([])
        for arr in y_pixels:
            data = np.append(data, np.median(arr))
        data -= np.min(data)
        graph_data.append(data)
    
    return graph_data

def save_data(graph_data):
    for i, data in enumerate(graph_data):
        with open(f'Data/data{i}.json', 'w') as f:
            json.dump(list(data), f)


def main():
    # Read in all the images from the screenshot folder
    image_arrays = read_in("Screenshots/")
    # Crop the graph section of each image
    graph_image_arrays = crop(image_arrays)
    # Extract data 
    graph_data = graph_mask(graph_image_arrays)
    # Save as json
    save_data(graph_data)

if __name__ == "__main__":
    main()