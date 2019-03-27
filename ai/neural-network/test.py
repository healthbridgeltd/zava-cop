from neuralNetworkMultiLayer import neuralNetwork
from array import *
import numpy

input_nodes = 784
hidden_layers = int(input("How many hidden layers? [1]") or "1")
hidden_nodes = int(input("How many hidden nodes? [100]") or "100")
output_nodes = int(input("How many output nodes? [10]") or "10")
learning_rate = float(input("Please enter a learning rate [0.3]") or "0.3")

input_nodes = int(input("How many input nodes? [784] ") or "784")
hidden_layers = int(input("How many hidden layers? [1] ") or "1")
hidden_nodes = []
for i in range(0, hidden_layers):
  hidden_nodes.append(int(input("How many nodes in hidden layer " + str(i) + "? [100] ") or "100"))
output_nodes = int(input("How many output nodes? [10] ") or "10")
learning_rate = float(input("What is the required learning rate? [0.3] ") or "0.3")

n = neuralNetwork(input_nodes, hidden_layers, hidden_nodes, output_nodes, learning_rate)

scorecard = []
for i in range(0, 10):
  scorecard.append([0, 0])
  pass

# Import training data.
print("Opening training file and reading data...")
training_data_file = open("mnist_dataset/mnist_train.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# Train network.
print("Training the network...")
for record in training_data_list:
  # Split by commas.
  all_values = record.split(',')

  # Scale and shift inputs.
  inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01

  # Create target output values (all 0.01 except target output, which is 0.99).
  targets = numpy.zeros(output_nodes) + 0.01

  # all_values[0] holds the target label for the record.
  targets[int(all_values[0])] = 0.99
  n.train(inputs, targets)
  pass

# Test network.
print("Opening test file and reading data...")
test_data_file = open("mnist_dataset/mnist_test.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

correct = 0
incorrect = 0
for record in test_data_list:
  # Split record by commas.
  all_values = record.split(',')
  correct_label = int(all_values[0])
  inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
  outputs = n.query(inputs)
  label = numpy.argmax(outputs)
  if (label == correct_label):
    scorecard[correct_label][1] += 1
    correct += 1
  else:
    scorecard[correct_label][0] += 1
    incorrect += 1
    pass
  pass


print("Correct: ", correct)
print("Incorrect: ", incorrect)
print("Performance: ", (correct / (correct + incorrect)) * 100, '%')

for i in range(0, 10):
  denominator = (scorecard[i][0] + scorecard[i][1])
  if denominator > 0:
    pc = round(scorecard[i][1] / denominator, 4) * 100
  else:
    pc = 0

  print(i, ": ", scorecard[i][1], " correct, ", scorecard[i][0], " incorrect (", pc, "%).")
