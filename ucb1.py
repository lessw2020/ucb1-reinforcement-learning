#3/1/19 - Implementation of UCB1 based on Jeremy Kun's implementation...
import math

def UpperConfidenceBound(step, numVisits):
    upper = math.sqrt(2 * math.log(numVisits+1)/numVisits)
    #print("Upper Bounds for {} step with {} visits".format(step,numVisits))
    return upper

def ucb1(numChoices, reward):
    payoffSums= [0] * numChoices
    numPlays = [1] * numChoices
    ucbs = [0] * numChoices
    
    #initialize sums
    for t in range(numChoices):
        payoffSums[t] = reward(t,t)
        yield t, payoffSums[t], ucbs
        
    t = numChoices
    
    while True:
        ucbs = [payoffSums[i] / numPlays[i] + UpperConfidenceBound(t,numChoices[i]) for i in range(numChoices)]
        selection = max(range(numChoices),key = lambda i:ucbs[i])
        theReward = reward(selection,t)
        numPlays[selection]+=1
        payoffSums[selection] += theReward
        
        yield selection,theReward,ucbs
        t +=1
        
        