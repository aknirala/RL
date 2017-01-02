import random as r
import matplotlib.pyplot as plt

class Bandits:
    def __init__(self, k, mean, var, e = 0.1, initPredReward = None):
        self.k = k
        self.mean = mean
        self.var = var
        self.e = e
        self.q = list()
        #TODO: How can I do this as vec or matrix
        [self.q.append(r.normalvariate(mean, var)) for i in range(0, k)]
        self.Q = list()
        if initPredReward != None:
            self.q = self.Q
        else:
            [self.Q.append(0) for i in range(0, k)]
        self.Qn = list()
        [self.Qn.append(0) for i in range(0, k)]
        
    def getReward(self, kthArm):
        if kthArm >= self.k:
            print("ERROR. "+str(kthArm)+" requested, when only: "+str(self.k)+" are available")
            return -1000
        return r.normalvariate(self.q[kthArm], self.var)
    
    def eGreedyStep(self, e = None):
        if e == None:
            e = self.e
        #Choose which action to take
        cK = -1
        if r.uniform(0, 1) < e:
            #Non-optimal selection (making it purely random for now)
            cK = int(r.uniform(0, self.k))
        else:
            #Optimal selection
            cK = sorted(range(len(self.Q)), key=lambda i: self.Q[i])[-1:][0]
        
        #Get the reward for that
        reward = self.getReward(cK)
        
        #Upate Q, for that action
        self.Qn[cK] += 1
        self.Q[cK] += (reward - self.Q[cK])/self.Qn[cK]
        
        #return the reward
        return reward

instCount = 2000
insts = list()
k = 10
mean = 0
var = 1
stepsTot = 100


[insts.append(Bandits(k, mean, var)) for i in range(0, instCount)]
aggReward = list()
for s in range(0, stepsTot):
    print("Step: ",s)
    stepReward = 0
    for i in range(0, instCount):
        stepReward = stepReward + insts[i].eGreedyStep()
    
    aggReward.append(stepReward/instCount)

plt.figure(figsize=(10,6))
plt.plot(range(0, stepsTot) , aggReward,'r-',markersize=10)
plt.grid(True)
plt.show()
