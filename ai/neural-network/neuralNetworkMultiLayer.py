import numpy
# scipy.special for the sigmoid function expit()
import scipy.special

# neural network class definition
class neuralNetwork:
    
    # initialise the neural network
    def __init__(self, inputnodes, hiddenlayers, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.hiddenlayers = hiddenlayers
        self.weights = []
        self.nodes = [inputnodes]
        self.nodes.extend(hiddennodes)
        self.nodes.extend([outputnodes])
        
        for i in range(0, hiddenlayers + 1):
            self.weights.append(numpy.random.normal(0.0, pow(self.nodes[i], -0.5), (self.nodes[i+1], self.nodes[i])))

        #   Set learning rate.
        self.lr = learningrate

        #   Define sigmoid activation function.
        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    
    # train the neural network
    def train(self, inputs_list, targets_list):
        nodeValues = [numpy.array(inputs_list, ndmin=2).T]
        targets = numpy.array(targets_list, ndmin=2).T

        #   Calculate for each layer. Add one to account for output layer.
        for i in range(1, self.hiddenlayers + 2):
            nodeValues.append(numpy.dot(self.weights[i - 1], nodeValues[i - 1]))
            nodeValues[i] = self.activation_function(nodeValues[i])

        # output layer error is the (target - actual)
        output_errors = targets - nodeValues[i]

        #   Iterate back through hidden layers.
        for i in range(self.hiddenlayers + 1, 0, -1):
            self.weights[i - 1] += self.lr * numpy.dot((output_errors * nodeValues[i] * (1.0 - nodeValues[i])), numpy.transpose(nodeValues[i - 1]))
            output_errors = numpy.dot(self.weights[i - 1].T, output_errors)

        pass

    
    # query the neural network
    def query(self, inputs_list):
        nodeValues = [numpy.array(inputs_list, ndmin=2).T]

        #   Calculate for each layer.
        for i in range(1, self.hiddenlayers + 2):
            nodeValues.append(numpy.dot(self.weights[i - 1], nodeValues[i - 1]))
            nodeValues[i] = self.activation_function(nodeValues[i])

        return nodeValues[i]

    