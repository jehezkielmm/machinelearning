import math
import random
import numpy as np
import matplotlib.pyplot as plt

error1 =[]
error2 =[]
d_bias = []
d_theta = []
learningrate = 0.8

file = open('Assignment2.csv','r').read()
file = (file.split('\n'))[1:151]

for i in range(0,150):
    file[i] = file[i].split(',')
    for j in range(0,4):
        file[i][j] = float(file[i][j])

category = {
    "Iris-setosa": [0,0],
    "Iris-versicolor": [0,1],
    "Iris-virginica": [1,1]
}

theta = [
    [0.594518077,0.371617486,0.649179784,0.401515039],
    [0.751045864, 0.785152025, 0.400418549, 0.252745197],
]

bias = [
	0.250473594, 0.088775294
]

error1all = []
error2all = []
accuracyall = []
counter = 0

for epak in range (0,100):
	error1 = []
	error2 = []

	accuracy = 0
	for row in file:
	    counter = counter + 1

	    target1 = 0
	    target2 = 0
	    row = file[0]

	    for i in range (0,4):
	    	target1 = target1 + float(theta[0][i]) * float(row[i])

	    target1 =  target1 + float(bias[0])

	    for i in range(0,4):
	        target2 = target2 + theta[1][i] * row[i]
	    target2 = target2 + bias[1]


	    sigmoid = [
	        (1 / (1 + math.exp(-target1))),
	        (1 / (1 + math.exp(-target2)))
	    ]

	    prediction = [
	        np.round(sigmoid)
	    ]

	    guess = int(prediction[0][0])
	    guess1 = int(prediction[0][1])
	    correct = np.asfarray(category[row[4]][0])
	    correct1 = np.asfarray(category[row[4]][1])

	    if ((guess == correct) and (guess1 == correct1)):
	    	accuracy += 1
	    # print(prediction)

	    error1.append((sigmoid[0] - category[row[4]][0]) ** 2)

	    error2.append((sigmoid[1] - category[row[4]][1]) ** 2)
	    # print("error", error)

	    d_theta = []

	    for i in range (0,2):
	        temp = []

	        for varinput in row[0:4]:
	            temp.append(2*(sigmoid[i] - category[row[4]][i]) * (1-sigmoid[i]) * sigmoid[i] * varinput)
	        d_theta.append(temp)

	    for i in range(0,2):
	        for j in range(0,4):
	            theta[i][j] = theta [i][j] - learningrate * d_theta[i][j]
	    #print(counter, theta)

	    d_bias = []

	    for i in range (0,2):
	        d_bias.append(2*(sigmoid[i] - category[row[4]][i]) * (1-sigmoid[i]) * sigmoid[i] * 1) 
	    #print(counter, d_bias)

	    for i in range(0,2):
	        bias[i] = bias [i] - learningrate * d_bias[i]
	    #print(counter, bias)

	error1all.append(sum(error1)/150)
	error2all.append(sum(error2)/150)
	accuracyall.append(accuracy/150)

plt.plot(error2all)
plt.show()