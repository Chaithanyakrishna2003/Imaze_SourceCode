from controller import Robot, Motor, DistanceSensor
from controller import Robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())
left_motor=robot.getDevice("left wheel motor")
right_motor=robot.getDevice("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
max_speed=6.27
prox_sensor = []
for i in range(8):
    name = "ps" + str(i)
    prox_sensor.append(robot.getDevice(name))
    prox_sensor[i].enable(timestep)
def frontreading():
    return (prox_sensor[0].getValue() + prox_sensor[7].getValue())
def leftreading():
    return prox_sensor[5].getValue()
def rightreading():
    return prox_sensor[2].getValue() 
def forward(speed):
    if(speed > 100):
      speed=100
    speed = (max_speed/100)*speed	
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)
def right(speed):
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    if speed >100 :
        speed=100
    speed = (max_speed/100)*speed
    left_motor.setVelocity(speed)
    right_motor.setVelocity(-speed/2)
    
while robot.step(timestep) != -1:
    if(frontreading() < 160):
        forward(150)
    else:
        right(120)    
		
		
    pass


