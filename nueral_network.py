import numpy


#add the images and labels here
#make this entirely class dependant
#link to the main, and create connect between draw and train

class NueralNetwork():
#The "squish" function choosen for this particular Nueral Network is the sigmoid (logistic) curve
    pic_size = 28  # The size of the original grayscale picture
    lay1_size = pic_size ** 2  # Size of the first layer (28x28)
    lay2_size = 5  # Size of the second layer (5)
    lay3_size = 1  # Size of the third layer (1))


    # HYPERPARAMTER
    learn_rate = .01
    def __init__(self):
        # Activations -- All Activations of nuerons are held here
        self.layer1A = numpy.zeros((NueralNetwork.lay1_size), dtype=float)
        self.layer2A = numpy.zeros((NueralNetwork.lay2_size), dtype=float)
        self.layer3A = numpy.zeros((NueralNetwork.lay3_size), dtype=float)

        # Weights -- All weights are stored here
        self.weight21 = numpy.zeros((NueralNetwork.lay2_size, NueralNetwork.lay1_size), dtype=float)
        self.weight32 = numpy.zeros((NueralNetwork.lay2_size), dtype=float)

        # Biases -- All biases are stored here
        self.bias21 = numpy.zeros((NueralNetwork.lay2_size), dtype=float)
        self.bias32 = numpy.zeros((NueralNetwork.lay3_size), dtype=float)

        self.costs = []

        # Randomizes all biases and weights in layers 1-2
        for i in range(NueralNetwork.lay2_size):
            self.bias21[i] = numpy.random.randn()
            for y in range(NueralNetwork.lay1_size):
                self.weight21[i][y] = numpy.random.randn()

        # Randomizes all biases and weights in layers 2-3
        for i in range(5):
            self.weight32[i] = numpy.random.randn()

        self.bias32[0] = numpy.random.randn()

    def sigmoid(self, x):
        return 1/(1+numpy.exp(-x))

    #This is the derivative of the sigmoid curve
    def sigmoid_p(self, x):
        return self.sigmoid(x) * (1- self.sigmoid(x))


    def img_to_activation(self, image):
        scale = 1 / 255

        for i in range(NueralNetwork.lay1_size):
            self.layer1A[i] = image[i] * scale

    def find_activation(self):

        self.layer2A = numpy.matmul(self.weight21, self.layer1A)

        for i in range(NueralNetwork.lay2_size):
            self.layer2A[i] = self.layer2A[i] + self.bias21[i]

        for i in range(NueralNetwork.lay2_size):
            self.layer2A[i] = self.sigmoid(self.layer2A[i])

        self.layer3A = numpy.matmul(self.weight32, self.layer2A)
        self.layer3A = self.layer3A + self.bias32
        self.layer3A = self.sigmoid(self.layer3A)

    def deriv_fill(self, actual):
        # Change Matrices

        cweightL1 = numpy.zeros((NueralNetwork.lay2_size, NueralNetwork.lay1_size), dtype=float)
        cweightL2 = numpy.zeros((NueralNetwork.lay2_size), dtype=float)

        cbiasL1 = numpy.zeros((NueralNetwork.lay2_size), dtype=float)
        cbiasL2 = numpy.zeros((NueralNetwork.lay3_size), dtype=float)

        # Constants needed to compute derivatives
        pred = self.layer3A
        z = 0
        for i in range(NueralNetwork.lay2_size):
            z = self.layer2A[i] * self.weight32[i]
        z = z + self.bias32

        num_w_2 = NueralNetwork.lay2_size
        num_w_1 = NueralNetwork.lay1_size * NueralNetwork.lay2_size
        # --------------------------------------- Derivatives

        dc_dsig = 2 * (pred - actual)
        dsig_dz = self.sigmoid_p(z)

        # dz_d(any layer 2 weight) = activation, bias = 1

        for i in range(NueralNetwork.lay2_size):
            dz_dw0i = self.layer2A[i]
            cweightL2[i] = dc_dsig * dsig_dz * dz_dw0i
        cbiasL2[0] = dc_dsig * dsig_dz

        for i in range(NueralNetwork.lay2_size):
            cbiasL1[i] = 1
            dz_da2i = self.weight32[i]
            for y in range(NueralNetwork.lay1_size):
                da2i_dwiy = self.layer1A[y]
                cweightL1[i][y] = dc_dsig * dsig_dz * dz_da2i * da2i_dwiy

        return cweightL1, cweightL2, cbiasL1, cbiasL2


    def update_val(self, cweightL1, cweightL2, cbiasL1, cbiasL2):
        # updates weights connecting layers 1-2
        for i in range(NueralNetwork.lay2_size):
            for y in range(NueralNetwork.lay1_size):
                self.weight21[i][y] = self.weight21[i][y] - (NueralNetwork.learn_rate * cweightL1[i][y])

            # updates weights connected layers 2-3
        for i in range(NueralNetwork.lay2_size):
            self.weight32[i] = self.weight32[i] - (NueralNetwork.learn_rate * cweightL2[i])

            # updates biases in layer 2 nuerons
        for i in range(NueralNetwork.lay2_size):
            self.bias21[i] = self.bias21[i] - (NueralNetwork.learn_rate * cbiasL1[i]) ########### LOOK FOR ERRORS IN ORIGINAL CODE

            # updates biases in layer 3 nuerons
        self.bias32[0] = self.bias32[0] - (NueralNetwork.learn_rate * cbiasL2[0])


    def test(self, image):
        self.img_to_activation(image)
        self.find_activation()

    def train(self, index, images_t, labels_t):

        self.img_to_activation(images_t[index])
        self.find_activation()
        cweightL1, cweightL2, cbiasL1, cbiasL2 = self.deriv_fill(labels_t[index])
        self.update_val(cweightL1, cweightL2, cbiasL1, cbiasL2)
        if (index%50 == 0):
            self.costs.append((self.layer3A - labels_t[index])**2)





