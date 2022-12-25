#!/usr/bin/python3

import sys
from os import listdir
import numpy as np
import operator

def CreateDataSet(dirname):
	labels = []
	trainingFileList = listdir(dirname)
	m = len(trainingFileList)
	matrix = np.zeros((m, 1024))

	for i in range(m):
		fileNameStr = trainingFileList[i]
		answer = int(fileNameStr.split('_')[0])
		labels.append(answer)
		matrix[i, :] = getVector(dirname + '/' + fileNameStr)
	return matrix, labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}

	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

def getVector(filename):
	vector = np.zeros((1, 1024))
	with open(filename) as fp:
		for i in range(32):
			line = fp.readline()
			for j in range(32):
				vector[0, 32 * i + j] = int(line[j])
		return vector


trainingFileDirName = sys.argv[1]
testFileDirName = sys.argv[2]

testFileList = listdir(testFileDirName)
length = len(testFileList)

matrix, labels = CreateDataSet(trainingFileDirName)

for k in range (1, 21):
	count = 0
	errorCount = 0

	for i in range(length):
		answer = int(testFileList[i].split('_')[0])
		testData = getVector(testFileDirName + '/' + testFileList[i])
		classifiedResult = classify0(testData, matrix, labels, k)

		count += 1
		if answer != classifiedResult :
			errorCount += 1
	
	print(int(errorCount / count * 100))
