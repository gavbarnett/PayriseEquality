import pylab as plt
import numpy as np
from random import uniform

def newCompany(staffCount, minPay, maxPay):
    salaryList = []
    minP = pow(minPay,1/4)
    maxP = pow(maxPay,1/4)
    for staffMember in range (0, staffCount):
        tempPay = pow(uniform(minP, maxP),4)
        salaryList.append(tempPay)
    salaryList.sort()
    return (salaryList)

def payrise (salaryList, rise, p):
    TotalSalary = sum(salaryList)
    k = min(len(salaryList)-1, (TotalSalary/max(salaryList)))
    pk = k*p
    for index in range(len(salaryList)):
        tempSalary = salaryList[index]+rise*((TotalSalary - salaryList[index]*pk)/(len(salaryList)-pk))
        salaryList[index] = tempSalary
    salaryList.sort()
    return (salaryList)

def plotter(salaryList):
    y = salaryList
    N = len(y)
    x = range(N)
    width = 1/1.5
    plt.ion()
    graph = plt.bar(x, y, width, color="blue")#[0]
    while min(salaryList)/max(salaryList) < 0.9:
        salaryList = payrise (salaryList, 0.02, 0.9)
        print (salaryList)
        for rect, h in zip(graph, x):
            rect.set_height(salaryList[h])
        #y[0] = y[0]*1.01
        #graph.set_height(y[0])
        axes = plt.gca()
        axes.set_ylim([0,max(salaryList)*1.2])
        plt.draw()
        plt.pause(0.1)

def main():
    salaryList = newCompany(1000, 10000, 100000)
    print(salaryList)
    plotter(salaryList)

main()
    