from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
   x,y,z=mc.player.getTilePos()
   mc.postToChat('X:' + str(x) + 'Y:' + str(y) + 'Z:' + str(z))
   

x,y,z=mc.player.getTilePos() 
mc.setBlock(x,y,z,1)
mc.setBlock(x+1,y,z,1)
mc.setBlock(x+2,y,z,1)
mc.setBlock(x+3,y,z,1)
mc.setBlock(x+4,y,z,1)
mc.setBlock(x,y,z+1,1)
mc.setBlock(x,y,z+2,1)
mc.setBlock(x,y,z+3,1)
mc.setBlock(x,y,z+4,1)
mc.setBlock(x,y,z+5,1)

x,y,z=mc.player.getTilePos() 
mc.setBlock(x+1,y,z,1,1)
mc.setBlock(x+1,y,z+1,1,1)
mc.setBlock(x+1,y,z-1,1,1)
mc.setBlock(x-1,y,z,1,1)
mc.setBlock(x-1,y,z+1,1,1)
mc.setBlock(x-1,y,z-1,1,1)
mc.setBlock(x,y,z+1,1,1)
mc.setBlock(x,y,z-1,1,1)

import random
import time
x,y,z=mc.player.getTilePos() 
while True:
    r=random.randrange(0,16)
    mc.setBlocks(x+5,y,z+5,x-5,y,z-5,35,r)
    time.sleep(0.5)
