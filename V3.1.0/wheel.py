import random

def init(functions_list):
    value=float(100.00/len(functions_list))
    proba_list=[]
    for elem in functions_list:
        proba_list.append(value)
    return proba_list

def update(list_proba,proba_min, pos, improvement,reward_factor):

    #count how many operators are still viable (above the min)
    size=0
    for elem in list_proba:
        if elem!=proba_min:size+=1

    #get the percentages without the one we used (so we can modify them accordingly)
    ratios=list_proba.copy()
    total=0.0
    for i in range(0,len(list_proba)): # get the max
        if i!=pos: total+=list_proba[i]
    for i in range(0,len(list_proba)): # generate ratios
        if i!=pos:ratios[i]=list_proba[i]/total
    ratios[pos]=0.0
    
    if improvement>0:
        if size>1: #only if there's an operator which we can decrease the probability
            reward=float(improvement*reward_factor)
            change=float(reward/(size-1))
            diff=0.0
            for i in range(0,len(list_proba)):
                if(i!=pos):
                    list_proba[i]=list_proba[i]-change
                    #if an error goes below the limit, we push it to the limit and decrease the gain of the rewarded operator
                    if(list_proba[i]<proba_min):
                        diff+=proba_min-list_proba[i]
                        list_proba[i]=proba_min
            list_proba[pos]+=reward-diff
    else :
        # calculate the changes to be made
        if (list_proba[pos]-(2*reward_factor*(len(list_proba)-1)))>=proba_min: 
            reward=2*reward_factor
        else : 
            reward = (2*reward_factor)-(proba_min-(list_proba[pos]-(2*reward_factor*(len(list_proba)-1)))) # if the next value is below the min, we adjust the reward
            
       #apply the changes to the probabilities
        for i in range(0,len(list_proba)):
            if(i==pos): list_proba[i]=list_proba[i]-(reward*(len(list_proba)-1))
            else: list_proba[i]+=reward
    
    #verification & correction if ther's some round error
    sum_proba=sum(list_proba)
    if(sum_proba!=100.0):list_proba[pos]+=100.0-sum_proba

def pick(list_proba):
    generated=random.randint(1,100)
    sum=0.0
    for i in range(0,len(list_proba)):
        sum=sum+list_proba[i]
        if generated<=sum : return i

    return 1 #default operator is noFlip, 1 is his position
