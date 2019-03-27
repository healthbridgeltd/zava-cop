import numpy
# scipy.special for the sigmoid function expit()
import scipy.special

# neural network class definition
class neuralNetwork:
    
    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, hiddenlayers, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.hiddenlayers = hiddenlayers
        
        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc 
        self.wih = []
        self.who = []
        for i in range(0, hiddenlayers):
            if i == 0:
                w = self.inodes
            else:
                w = self.hnodes
            self.wih.append(numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, w)))
            self.who.append(numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, w)))

        # learning rate
        self.lr = learningrate
        
        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)
        
        pass

    
    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        
        # calculate signals into hidden layer
        #hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        #hidden_outputs = self.activation_function(hidden_inputs)
        hidden_outputs = self.queryHiddenLayers(inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who[self.hiddenlayers - 1], hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        # output layer error is the (target - actual)
        output_errors = targets - final_outputs

        # update the weights for the links between the hidden and output layers
        for layerIndex in range(self.hiddenlayers - 1, -1, -1):
            # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
            hidden_errors = numpy.dot(self.who[layerIndex].T, output_errors) 

            self.who[layerIndex] += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
            
            # update the weights for the links between the input and hidden layers
            self.wih[layerIndex] += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        
        pass
    
    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        
        # calculate signals into hidden layer
        #hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        #hidden_outputs = self.activation_function(hidden_inputs)
        hidden_outputs = self.queryHiddenLayers(inputs)
        
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        
        return final_outputs

    def queryHiddenLayers(self, inputs):
        for layerWeights in self.wih:
            hidden_inputs = numpy.dot(layerWeights, inputs)
            hidden_outputs = self.activation_function(hidden_inputs)
            print(str(len(inputs)))
            inputs = hidden_inputs
            print(str(len(inputs)))

        return hidden_outputs
    