"""my_controller_project controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

timeStep=320
flag=0
motorRPC= robot.getDevice("RPC")
motorRPF= robot.getDevice("RPF")
motorRMC= robot.getDevice("RMC")
motorRMF= robot.getDevice("RMF")
motorRAC= robot.getDevice("RAC")
motorRAF= robot.getDevice("RAF")

motorLPC= robot.getDevice("LPC")
motorLPF= robot.getDevice("LPF")
motorLMC= robot.getDevice("LMC")
motorLMF= robot.getDevice("LMF")
motorLAC= robot.getDevice("LAC")
motorLAF= robot.getDevice("LAF")

while(robot.step(timeStep)!=-1):
    if(flag%10==0):
        motorRPC.setPosition(-0.3)
    elif(flag%10==2):
        motoRPF.setPosition(-0.3)
    elif(flag%10==4):
        motorRMC.setPosition(-0.3)
    elif(flag%10==6):
        motorRMF.setPosition(-0.3)
    # elif(flag%10==7):
        # leg1.setPosition(0.2)
        # leg2.setPosition(0.2)
        # leg3.setPosition(0.2)
        # leg4.setPosition(0.2)
    flag+=1