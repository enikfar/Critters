import critter
import constants
from repeater import FanRepeater

class Me2(critter.Critter):
  PounceCount = 0
  ScratchCount = 0
  RoarCount = 0
  win_count = 0
  lose_count = 0
  

  
  
  def __init__(self):
    self.defaultAttacak = constants.SCRATCH
    self.seq = [constants.BLACK,constants.ORANGE,constants.GREEN]
    self.color = FanRepeater(self.seq,2)
    self.co = constants.ORANGE
    
  

  def get_color(self):
    return self.co
    



  def get_char(self):
    
    return "Ha"



  def get_move(self,self_info):
    directions = [constants.NORTH,
                  constants.SOUTH,
                  constants.WEST,
                  constants.EAST]

    a = [self.neighbor_threat(self_info, direction) for direction in directions]
      

    

    if Me2.win_count <= Me2.lose_count: 


      minn = min(a)

      if minn == a[0]:
        return directions[0]
      if minn == a[1]:
        return directions[1]
      if minn == a[2]: 
        return directions[2]
      if minn == a[3]:
        return directions[3]



    if Me2.win_count > Me2.lose_count: 
      mx = max(a)
      if mx == a[0]:
        return directions[0]
      if mx == a[1]:
        return directions[1]
      if mx == a[2]: 
        return directions[2]
      if mx == a[3]:
        return directions[3]
      





    
    

  

   
   


  def fight(self,opp_info): 
    self.co = self.color.next()
    if opp_info.get_char == "T":
      return constants.POUNCE

    if opp_info.get_char == "E":
      return constants.SCRATCH

    if opp_info.get_char == "0":
      return constants.SCRATCH

    if opp_info.get_char == "M":
      return constants.ROAR
    if opp_info.get_char == "S":
      return constants.POUNCE  

    else:
      


      return self.defaultAttacak

  def recover(self,won,attack_st):
    if attack_st == constants.POUNCE:
      Me2.PounceCount +=1
    if attack_st == constants.ROAR:
      Me2.RoarCount +=1
    if attack_st == constants.SCRATCH:
      Me2.ScratchCount +=1

    maxx = max(Me2.PounceCount,Me2.RoarCount,Me2.ScratchCount)  

    if maxx == Me2.PounceCount:
      self.defaultAttacak = constants.SCRATCH
    if maxx == Me2.RoarCount:
      self.defaultAttacak = constants.POUNCE
    if maxx == Me2.ScratchCount:
      self.defaultAttacak = constants.ROAR

    if won == True:
      Me2.win_count += 1
    if won == False:
      Me2.lose_count += 1
    


    
  
 


    



    




