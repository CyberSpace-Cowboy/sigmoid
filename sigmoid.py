# Imports
import matplotlib.pyplot as plt
import numpy as np
import math
#To center output in the terminal
import shutil
columns = shutil.get_terminal_size().columns

def Sigmoid_Fun():
	x = float(input("Enter the value on the X axis: "))
	y = 1/(1 + np.exp(-x))
	print("The corresponding value on the Y axis is " + str(y))

def Sigmoid_Plot():
	x = np.linspace(-10, 10, 100)
	z = 1/(1 + np.exp(-x))
	plt.plot(x, z)
	plt.xlabel("x")
	plt.ylabel("Sigmoid(X)")
	plt.show()

def Choose_Action():
	print("\n" + "SIGMOID FUNCTION".center(columns) + "\n")

	while(True):

		ask = input("\n Choose between Play Around mode (1) and Plot mode (2)? (1/2): ")
		if ask.lower() == "1":
			while True:
				for i in range(3):
					Sigmoid_Fun()
				ask = input("\n Wanna Continue Playing Around With Sigmoid? (y/n): ")
				if ask.lower() == "y":
					continue
				elif ask.lower() == "n":
					break
		elif ask.lower() == "2":
			Sigmoid_Plot()

		ask = input("\n Wanna Continue Running the App? (y/n): ")
		if ask.lower() == "y":
			continue
		elif ask.lower() == "n":
			exit()

if __name__ == "__main__":
	Choose_Action()




