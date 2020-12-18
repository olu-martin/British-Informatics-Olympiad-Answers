class stack(): #use a stack to store trail
    def __init__(self, n):
      self.stack = [None]*n
      self.max = n
      self.top = n-1
        
    def push(self,item):
      self.stack[self.top]=item
      self.top = (self.top+1)%self.max
    
      
class Explorer():
  def __init__(self,t ,i,m):
      self.t = t; self.i = i; self.m = m
      self.pos = [0,0]; self.direction = 0 #0,1,2,3 for N,E,S,W
      self.dir = {0:[0,1], 1:[1,0], 2:[0,-1], 3:[-1,0]} #if direction is north, increase y-coordinate by 1 e.t.c.
      self.trail = stack(t)
      self.trail.push(self.pos)
      
  def change_position(self,inst):
      attempts = 0
      if inst == "L":
          self.direction = (self.direction - 1)%4 
      elif inst == "R":
          self.direction = (self.direction + 1)%4
          
      while attempts < 4:
          new_pos = [self.pos[0]+self.dir[self.direction][0], self.pos[1]+self.dir[self.direction][1]]
          if new_pos in self.trail.stack:
              attempts += 1
              self.direction = (self.direction + 1) % 4 #Go right
          else:
              self.pos = new_pos
              self.trail.push(self.pos)
              return True
      return False
          
  
  def move(self):
      move_count = 0
      while True:
          for i in self.i:
              if self.change_position(i):
                  move_count +=1
                  '''print("{}: {},{}".format(move_count, self.pos[0],self.pos[1]))''' #Uncomment to see each step
                  if move_count >= self.m: return self.pos
              else:
                  return self.pos
      
              
      
def main():
    while True:
    	inp = input("> ").split(" ")
    	tracker = Explorer(int(inp[0]), str(inp[1]), int(inp[2]))
    	print(tracker.move())
    
if __name__ == "__main__":
    main()

