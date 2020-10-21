import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt


class go_algo():
	def __init__(self, layers, activation='sigmoid'):
		self.layers = layers[0]

	def printProgress(self, x, output, y, step):
		print("Step: ", step)
		print(x)
		print(output)
		print(y)


	def find_RMS_error(self, y_actual, y_predicted):
		rmse = sqrt(mean_squared_error(y_actual, y_predicted))
		
		return rmse

	def fit(self, X, y, learning_rate=0.2, steps=100000, tol=1e-2):
		input_layer_neurons = x.shape[1] # number of features in data set
		hidden_layer_neurons = 3 # number of hidden layers neurons
		output_neurons = 1 # number of neurons at output layercls

		# initializing weight and bias
		w_hidden_layer = np.random.uniform(size=(input_layer_neurons,hidden_layer_neurons))
		b_hidden_layer = np.random.uniform(size=(1,hidden_layer_neurons))
		w_output = np.random.uniform(size=(hidden_layer_neurons,output_neurons))
		b_output = np.random.uniform(size=(1,output_neurons))

		for i in range(steps):
			#Forward Propogation
			hidden_layer_input1=np.dot(x, w_hidden_layer)
			hidden_layer_input=hidden_layer_input1 + b_hidden_layer
			hiddenlayer_activations = sigmoid(hidden_layer_input)
			output_layer_input1=np.dot(hiddenlayer_activations, w_output)
			output_layer_input= output_layer_input1 + b_output
			output = sigmoid(output_layer_input)

			#Backpropagation
			err = y - output
			rmse = self.find_RMS_error(y, output)
			slope_output_layer = sigmoid_prime(output)
			slope_hidden_layer = sigmoid_prime(hiddenlayer_activations)
			d_output = err * slope_output_layer
			Error_at_hidden_layer = d_output.dot(w_output.T)
			d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
			w_output += hiddenlayer_activations.T.dot(d_output) * learning_rate
			b_output += np.sum(d_output, axis=0,keepdims=True) * learning_rate
			w_hidden_layer += x.T.dot(d_hiddenlayer) * learning_rate
			b_hidden_layer += np.sum(d_hiddenlayer, axis=0,keepdims=True) * learning_rate


			if i % 2000 == 0: 
				self.printProgress(x, output, y, i)
				if rmse < tol: 
					print("NN training succeeded!")
					break
				else: 
					print("NN training failed.")
					print("RMSE: ", rmse)
					print()


# defining the Sigmoid Function
def sigmoid(x):
	return 1/(1 + np.exp(-x))

# derivative of Sigmoid Function
def sigmoid_prime(x):
	return x * (1 - x)

#defining the tanh functin 
def tanh(x):
	return np.tanh(x)

#derivative of tanh function
def tanh_prime(x):
	return 1.0 - x**2


nn = go_algo([2,2,1], activation='sigmoid')
x = np.array([[1,0,1,0],[1,0,1,1],[0,1,0,1]])
y = np.array([[1],[1],[0]])
nn.fit(x,y)