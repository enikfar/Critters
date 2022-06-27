import critter
import constants


class Chameleon(critter.Critter):
  PounceCount = 0
  ScratchCount = 0
  RoarCount = 0
  win_count = 0
  lose_count = 0
  

  
  
  def __init__(self):
    
    self.defaultAttacak = constants.SCRATCH
    
    self.color = constants.GREEN
    
  

    
  
    
    
    
   
    


  def get_color(self):
    return self.color
    



  def get_char(self):
    return 'C'


  def get_move(self,self_info):
    directions = [constants.NORTH,
                  constants.SOUTH,
                  constants.WEST,
                  constants.EAST]

    a = [self.neighbor_threat(self_info, direction) for direction in directions]
      

    if Chameleon.win_count <= Chameleon.lose_count: 


      minn = min(a)

      if minn == a[0]:
        return directions[0]
      if minn == a[1]:
        return directions[1]
      if minn == a[2]: 
        return directions[2]
      if minn == a[3]:
        return directions[3]



    if Chameleon.win_count > Chameleon.lose_count: 
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
    self.color = opp_info.get_color()
  

    return self.defaultAttacak

  
  def recover(self,won,attack_st):
    if attack_st == constants.POUNCE:
      Chameleon.PounceCount +=1
    if attack_st == constants.ROAR:
      Chameleon.RoarCount +=1
    if attack_st == constants.SCRATCH:
      Chameleon.ScratchCount +=1

    maxx = max(Chameleon.PounceCount,Chameleon.RoarCount,Chameleon.ScratchCount)  

    if maxx == Chameleon.PounceCount:
      self.defaultAttacak = constants.SCRATCH
    if maxx == Chameleon.RoarCount:
      self.defaultAttacak = constants.POUNCE
    if maxx == Chameleon.ScratchCount:
      self.defaultAttacak = constants.ROAR

    if won == True:
      Chameleon.win_count += 1
    if won == False:
      Chameleon.lose_count += 1

      


    



    




