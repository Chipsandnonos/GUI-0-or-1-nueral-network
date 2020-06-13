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

from graphics import *
from mnist import MNIST
import nueral_network
import MNIST_utils
import button
import displayboard
import drawboard
import screens
import matplotlib.pyplot as plt
import trainbox
import testbox
import drawbox


mndata = MNIST('samples')
images, labels = mndata.load_training()
train_labels, train_images = MNIST_utils.filter_mnist (labels, images)

images, labels = mndata.load_testing()
test_labels, test_images = MNIST_utils.filter_mnist (labels, images)


pic_size = 28
quit = False
win = GraphWin("0 or 1 Detector Nueral Network", 610, 800)
win.setBackground("black")

screen = screens.Screens(win)
model = nueral_network.NueralNetwork()

trainbox = trainbox.TrainBox(win)
testbox = testbox.TestBox(win)
drawbox = drawbox.DrawBox(win)



def main():

    screen.display_screen()
    trainbox.draw()

    while (screen.quit != True):
        click_point = win.getMouse()
        clicked(click_point)
    win.close()

def clicked(Pointc):
    max = len(train_images)
    if (screen.display_screen_on == True):

        if (screen.trainb.is_pressed(Pointc)):
            screen.trainlable.setText("Training... Please wait")
            screen.trainlable.setTextColor("yellow")
            for i in range(max):
                model.train(i, train_images, train_labels)

                if (trainbox.activation == False):
                    trainbox.draw()

                trainbox.update(model.layer3A, train_labels[i])
                cost = (model.layer3A - train_labels[i])**2
                screen.costlabel.setText(f"Cost: {cost}")

                if (i % 50 == 0):
                    screen.displayboard.colour_board(train_images,i)

                    #plt.plot(model.costs)
                    #plt.ylabel('Cost per training session')
                    #plt.xlabel('Training sessions')
                    #plt.ion()
                   # plt.show()
                    #plt.pause(.001)
                if (i == max-1):
                    screen.trainlable.setText("Machine is trained")
                    screen.trainlable.setTextColor("green")

        elif (screen.testb.is_pressed(Pointc)):
            count = 0

            if(testbox.activation != True):
                testbox.draw()
                trainbox.undraw()
            for i in range(len(test_labels)):
                model.test(test_images[i])
                cost = (model.layer3A - test_labels[i]) ** 2
                screen.costlabel.setText(f"Cost: {cost}")

                numguess = 0
                if (model.layer3A > .5):
                    numguess = 1

                if (numguess == test_labels[i]):
                    count = count +1

                accuracy = 100 * (count/(i+1))
                screen.displayboard.colour_board(test_images,i)

                testbox.update(model.layer3A,test_labels[i], accuracy)


        elif (screen.drawb.is_pressed(Pointc)):
            screen.draw_screen()
            if(trainbox.activation == True):
                trainbox.undraw()
            else:
                testbox.undraw()
            drawbox.draw()




        elif (screen.quitb.is_pressed(Pointc)):
            screen.quit = True


    elif (screen.draw_screen_on == True):
        if (screen.backb.is_pressed(Pointc)):
            drawbox.undraw()
            screen.display_screen()
            trainbox.draw()


        elif (screen.checkb.is_pressed(Pointc)):
            num_board = screen.drawboard.transfer()
            model.test(num_board)
            screen.drawboard.clear()
            drawbox.update(model.layer3A)
        elif (screen.eraseb.is_pressed(Pointc)):
            screen.drawboard.clear()
        elif (screen.drawboard.is_click(Pointc)):
            screen.drawboard.click(Pointc)


def draw_num(draw):
    stop = False
    while stop != True:
        click_point = win.getMouse()
        draw.click(click_point)

        if (quitb.is_pressed(click_point)):
            t = draw.transfer()
            model.test(t)
            print(model.layer3A)

            stop = True



#-----------------------------------------------------------------
main()



