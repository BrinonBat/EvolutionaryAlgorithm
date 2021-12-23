# EvolutionaryAlgorithm
Evolutionary Algorithm used to solve the one-max problem. It can be used for any problem which data structure is a binary vector

### TODO
 - [x] basic structure
 - [x] save manager
 - [x] plot generator
 - [x] end conditions
 - [x] fitness functions
 - [ ] selection functions
 - [ ] cross functions
 - [x] mutation functions
 - [ ] insertion functions
 - [x] 30 random seeds
 - [x] launch instances with all the seed, and THEN make a graph (mean of the means)
 - [x] print only the time spent and remaining
 - [x] loop of the current seed end when the goal is reached
 - [x] list configurations to be tested
 - [x] add V2.0.0
 - [ ] make a new version with evolutive changes on mutations
 - [ ] tests on it

 ### About versions

 Versions have the following pattern: 
 
 for X.Y.Z
 X = structure version
 Y = set of functions used version
 Z {0,5} : 0 = ordered by fitness , 5 = ordered by age (youngest first)

 V1.0.0 is used to chose a configuration manually and test it
 V2.0.0 will test every configuration possible and return the best one (average quicker)
 V3.0.0 will change the configuration during the execution to chose the one that fit the best to the moment