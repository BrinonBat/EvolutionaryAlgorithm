# EvolutionaryAlgorithm
Evolutionary Algorithm used to solve the one-max problem. It can be used for any problem which data structure is a binary vector

### TODO
 - [x] basic structure
 - [x] save manager
 - [x] plot generator
 - [x] end conditions
 - [x] fitness functions
 - [x] selection functions
 - [x] cross functions
 - [x] mutation functions
 - [x] insertion functions
 - [x] 30 random seeds
 - [x] launch instances with all the seed, and THEN make a graph (mean of the means)
 - [x] print only the time spent and remaining
 - [x] loop of the current seed end when the goal is reached
 - [x] list configurations to be tested
 - [x] add V2.0.0
 - [x] make a new version (V3.0.0) with evolutive changes on mutations (adaptative wheel)
 - [x] new plot to see the functions probabilities
 - [ ] improve reward_factor (automatic adjustation)
 - [ ] tests on it

 ### About versions

 V1.0.0 is used to chose a configuration manually and test it
 V2.0.0 will test every configuration possible and return the best one (average quicker)
 V3.0.0 will change the configuration during the execution to chose the one that fit the best to the moment
 V3.1.0 changes : 
 - now the mutation happen only when it doesn't decrease the population fitness
 - better repartition of percentage when some function hit the minimum

 V3.2.0 changes : (yet to be implemented)
 - adaptative reward_factor