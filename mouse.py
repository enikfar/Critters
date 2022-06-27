import critter
import constants
from repeater import Repeater

class Mouse(critter.Critter):
  def __init__(self,color):
    self.color = color
    self.se = [constants.EAST,constants.SOUTH]
    self.direction = Repeater(self.se)


  def get_color(self):
    return constants.BLUE


  def get_char(self):
    return 'M'


  def get_move(self, self_info):
    return self.direction.next()


  def fight(self, opp_info):
    return constants.SCRATCH

