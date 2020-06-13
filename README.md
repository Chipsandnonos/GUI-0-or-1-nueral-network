# GUI-0-or-1-nueral-network
#By Rahul Gudise
#This program is a GUI which will let a user train a nueral network which can recognize a 1 or 0. This is built with the nueral 
#network which I have previously posted. 
#In the code there is a commented out section which will display a graph of the cost of each traning session, just uncomment to see
#Additionaly, this program will train the network with all of the MNIST data, which will take a while
#During this time the GUI will not respond, just wait for it to finish before trying to interact with the UI
#If it is taking too long, feel free to edit the code to make the loop run for shorter, anything past like 1000 training examples
#should be enough for the network to be decent at identifying digits

#Features
#You can train the Neural Network, as well as test it, and see the % accuracy of the network
#Due to the weights and biases being randomized, you might get varying accuracies, I have personnaly seen from 93%-99% accuracte
#You can also draw your own 1 or 0 and test the nueral network

#Limitations with the Nueral Network
#In essence this network can ONLY decide between 1 or 0, and can not recoginize when it is neither, as such random inputs will 
#still lead to the network giving a confident answer, as it has been training (due to cost function being squared) to be very certain
#this can be imporved with more modern algorithms for nueral networks
