from neuralNetwork import neuralNetwork
import numpy

input_nodes = 784
hidden_nodes = 100
output_nodes = 10
learning_rate = 0.3

n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

scorecard = []
for i in range(0, 10):
  scorecard.append([0, 0])
  pass

# Import training data.
training_data_file = open("mnist_dataset/mnist_train.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# Train network.

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
  pc = (scorecard[i][1] / (scorecard[i][0] + scorecard[i][1])) * 100.0
  print(i, ": ", scorecard[i][1], " correct, ", scorecard[i][0], " incorrect (", pc, "%).")
