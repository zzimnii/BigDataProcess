import sys
from os import listdir
import numpy as np
import operator

def createDataSet(dirname):
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
    classCount = {} # Dictionary 선언

    for i in range(k): 
        voteIlabel = labels[sortedDistIndicies[i]]  
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 
    sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), reverse=True) 
    return sortedClassCount[0][0]

def getVector(filename): # txt file을 1행 1024열 vector(list)로 변환 
    vector = np.zeros((1, 1024)) # 1024 = 32 x 32
    with open(filename) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
        return vector        

trainingFileDirName = sys.argv[1]
testFileDirName = sys.argv[2]

testFileList = listdir(testFileDirName)
length = len(testFileList)

matrix, labels = createDataSet(trainingFileDirName)

for k in range(1, 20, 2): # 1부터 20까지의 홀수만
    count = 0 # 전체 데이터 개수
    errorCount = 0 # 에러가 발생한 데이터 개수
    
    for i in range(length): 
        answer = int(testFileList[i].split('_')[0])
        testData = getVector(testFileDirName + '/' + testFileList[i])
        classifiedResult = classify0(testData, matrix, labels, k)
        
        count += 1
        if answer != classifiedResult :
            errorCount += 1
    
    #print(str(errorCount) + "/" + str(count))
    print(int(errorCount / count * 100))
