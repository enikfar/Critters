# repeater.py
# This file containing the definition of the Repeater class. The goal of the Repeater class is to store a sequence of values and, whenever asked, return the next value in the sequence.
import random
class Repeater:
  def __init__(self, seq):
    self.seq = seq
    self.current = 0
    

  def next(self):
    x =  self.seq[self.current]
    self.current = self.current + 1
    if self.current == len(self.seq):
      self.current = 0
    return x 
        



    # Implement the method for returning the next element of the sequence 
class OppositeRepeater(Repeater):
  def __init__(self,seq):
    self.seq = seq
    self.current = len(self.seq) - 1
  def next(self):
    
    x = self.seq[self.current]
    self.current = self.current - 1
    if self.current == -1 :
      self.current = len(self.seq) -1
    return x 

class FancyRepeater(Repeater):
  def __init__(self,seq,period=1):
    self.seq = seq
    self.period = period
    self.elt = random.choice(seq)
    self.current = 0
    # self.index = 0
     

  
  def next(self):
    
    
    x = self.elt
    self.current +=1
    if self.current == self.period :
      self.current = 0
      self.elt = random.choice(self.seq)
    return x 
    
class FanRepeater(Repeater):
  def __init__(self,seq,period=4):
    self.seq = seq
    self.period = period
    
    self.current = 0
    self.index = 0
     

  
  def next(self):
    
    
    
    
    if self.index == len(self.seq):
      self.index = 0
    x = self.seq[self.index]  
    if self.current == self.period :
      self.current = 0
      self.index +=1
    self.current += 1  

    return x 







def main():
 # Write a test for your Repeater implementation
  p2 = FancyRepeater(["a","b","c"],5)
  for i in range(12): 
    print(p2.current, p2.next())
  p2 = FanRepeater(["a","b","c"],)
  for i in range(36): 
    print(p2.current, p2.next(),p2.index)


if __name__ == '__main__':
  main()



#p1 = OppositeRepeater([2,4,6])

#print(p1.current,p1.next())
#print(p1.current,p1.next())
#print(p1.current,p1.next())
#print(p1.current,p1.next())
#print(p1.current,p1.next())




