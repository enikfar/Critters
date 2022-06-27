import critter
import constants
from repeater import FanRepeater

class OppositeElephant(critter.Critter):

  def __init__(self,steps=6):
  
    
    
    
    self.seq = [constants.EAST,constants.NORTH,constants.WEST,constants.SOUTH]
    self.direction = FanRepeater(self.seq,steps)
    
    
    


  def get_color(self):
    return constants.GRAY
    



  def get_char(self):
    return '0'


  def get_move(self,self_info):
    
    return self.direction.next()
   

  


   
   


  def fight(self,opp_info):
    if opp_info.get_char() == "T":
      return constants.ROAR

    else:
      return constants.POUNCE


