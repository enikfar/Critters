import critter
import constants

class Sloth(critter.Critter):
  """Defines a Sloth."""
  
  def get_color(self):
    return constants.BROWN


  def get_char(self):
    return 'S'


  def get_move(self, self_info):
    return constants.CENTER


  def fight(self, opp_info):
    return constants.ROAR

