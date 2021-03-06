import pylab as plt
import numpy as np
from random import uniform

def newCompany(staffCount, minPay, maxPay):
    salaryList = []
    minP = np.log10(minPay)
    maxP = np.log10(maxPay)
    for staffMember in range (0, staffCount):
        tempPay = pow(10,uniform(minP, maxP))
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

def gini(salaryList):
    n = len(salaryList)
    salaryList.sort()
    ginisum = 0
    for index in range(len(salaryList)):    
        ginisum = ginisum+ (n+1-index-1)*salaryList[index]
    giniValue = (1/n)*(n+1-2*((ginisum)/(sum(salaryList))))
    return (giniValue)

def plotter(salaryList):
    year = 0
    y = salaryList
    N = len(y)
    x = range(N)
    width = 1/1.5
    plt.ion()
    graph = plt.bar(x, y, width, color="blue")#[0]
    while min(salaryList)/max(salaryList) < 0.9:
        salaryList = payrise (salaryList, 0.02, 1)
        g = gini(salaryList)
        print (year, g)
        year = year + 1
        #print (salaryList)
        for rect, h in zip(graph, x):
            rect.set_height(salaryList[h])
        #y[0] = y[0]*1.01
        #graph.set_height(y[0])
        axes = plt.gca()
        axes.set_ylim([0,max(salaryList)*1.2])
        plt.draw()
        plt.pause(0.1)
    print ("Final Salaries:")
    print (salaryList)


def main():
    salaryList = newCompany(10, 10000, 1000000)
    print(salaryList)
    plotter(salaryList)

main()
    