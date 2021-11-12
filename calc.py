import re
import numpy as np
import json 

payments_Text = "./payments.JSON"
people_Text = "./people.txt"

def readPeopleIn():
    with open(people_Text) as f:
        content = f.readlines()
    temp = []
    for line in content:
        temp.append(line)
    new_items = [x[:-1] for x in temp]
    return new_items

def readPaymentsIn():
    with open('payments.JSON', 'r') as myfile:
        data = myfile.read()
    output = json.loads(data)
    return output
        
def addShitUp(people, payments):
    tallies = {}
    for i in range(len(people)):
        name = people[i]
        tallies[name] = 0

    for pay in payments:
        extract = payments[pay]
        tallies[extract[0]] += extract[1]
    return tallies


def mathShit(tallies, people):
    totalCost = 0
    returnDict = {}
    for ele in tallies:
        totalCost += tallies[ele]
    even = totalCost / len(people)
    for person in tallies:
        if tallies[person] < even:
            owes = even - tallies[person]
            print(person + " owes €" + (str)(owes))
            returnDict[person] = owes
        else:
            returnDict[person] = even - tallies[person]

    return returnDict

def findPayer(owings):
    for person in owings:
        if owings[person] > 0:
            return person
def findPayee(owings):
    for person in owings:
        if owings[person] < 0:
            return person


def balanceItOut(owings):
    q = True
    while (q):
        payer = findPayer(owings)
        payee = findPayee(owings)
        if ((owings[payee] > -0.01) or (owings[payer] < 0.01)):
            break
        
        if (owings[payee] * (-1)) >= owings[payer]:
            print(payer + " pays €" + "{:.2f}".format((owings[payer])) + " to " + payee)
            temp = owings[payer]
            owings[payer] -= owings[payer]
            owings[payee] += temp
        else:
            print(payer + " pays €" + "{:.2f}".format((owings[payee] * (-1))) + " to " + payee)
            temp = owings[payee]
            owings[payee] -= owings[payee]
            owings[payer] += temp
        bal = 0
        for person in owings:
            if owings[person] != 0:
                break
            else:
                bal += 1
        if (bal == len(owings)):
            q = False


def main():
    people = readPeopleIn()
    payments = readPaymentsIn()
    tallies = addShitUp(people, payments)
    owings = mathShit(tallies, people)
    print("")
    balanceItOut(owings)

if __name__ == "__main__":
    main()
