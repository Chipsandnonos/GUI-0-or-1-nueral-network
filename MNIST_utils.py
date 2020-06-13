
#Takes in a list of numbers which need to be isolated from the MNIST data set
def filter_mnist (labels, images):
    num_shift = 0
    for i in range(len(labels)):

        if not (labels[i - num_shift] == 0 or labels[i - num_shift] == 1):
            images.pop(i - num_shift)
            labels.pop(i - num_shift)
            num_shift = num_shift + 1


    return labels, images


# A function which will take all grayscale pixel values in an original MNIST data piece and transfer into the activations
# of the first layer nuerons
# The value "scale", is there simply to convert the grayscale value (0-255), into a number which can be inputted into the nueron
# Nueron domain is 0-1

def img_to_activation(layer, image):
    scale = 1 / 255

    for i in range(len(image)):
        layer[i] = image[i] * scale

    return layer