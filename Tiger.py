import critter
import constants
# Read the repeater before grading because I used different name for my classes.

from repeater import Repeater, FancyRepeater

class Tiger(critter.Critter):

  def __init__(self,period=3):
    self.period = period
  
    
    
    
    self.seq = [constants.SOUTH,constants.WEST,constants.NORTH,constants.EAST]
    self.se = [constants.ORANGE,constants.BLACK]
    self.direction = FancyRepeater(self.seq,self.period)
    self.color = Repeater(self.se)
    self.co = constants.ORANGE
    
  


  def get_color(self):
    return self.co
    



  def get_char(self):
    return 'T'


  def get_move(self,self_info):
    self.co = self.color.next()
    
    return self.direction.next()
   

  

   
   


  def fight(self,opp_info):
    return constants.ROAR

# b = Tiger()
# for i in range(30):
#   print(b.get_color(),b.get_move())   




