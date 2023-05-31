import random

class BoringParticle:

 def __init__(self, x, y, v_x, v_y):

  self.x = x

  self.y = y

  self.v_x = v_x

  self.v_y = v_y
  self.kleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))




 def bewegen(self, interval):

  self.x += (self.v_x * interval)

  self.y += (self.v_y * interval)




 def reset(self, breedte, hoogte):
  
 
  if (self.y < 0) or (self.y > hoogte):

   self.x, self.y = breedte//2, hoogte//2

   self.v_x = (random.random() * 2) - 1

   self.v_y = (random.random() * 2) - 1
   self.kleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


  if (self.y < 0) or (self.y > breedte):

   self.x, self.y = breedte//2, hoogte//2

   self.v_x = (random.random() * 2) - 1

   self.v_y = (random.random() * 2) - 1
   self.kleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


  if (random.random() > 0.9999):

   self.x, self.y = breedte//2, hoogte//2

   self.v_x = (random.random() * 2) - 1

   self.v_y = (random.random() * 2) - 1

   self.kleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

