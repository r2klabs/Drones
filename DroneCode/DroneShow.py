from djitellopy import TelloSwarm

twos = TelloSwarm.fromIps([
    "192.168.194.85",
    "192.168.194.119"
    
##Drones one and two are in this group
])

ones = TelloSwarm.fromIps([
    "192.168.194.124"#,
    #"192.168.194.105"
    
## Drone three is in this group
])

threes = TelloSwarm.fromIps([\
    "192.168.194.85",
    "192.168.194.119",
    "192.168.194.124"#,
])


one = TelloSwarm.fromIps([
    "192.168.194.85"
])


two = TelloSwarm.fromIps([
    "192.168.194.119"
])


three = TelloSwarm.fromIps([
    "192.168.194.124"
])


## Setup:
## Drone 1, Drone 3, Drone 2


##Drones Connection
ones.connect()
twos.connect()
threes.connect()
one.connect()
two.connect()
three.connect()

##Takeoff (In unison)
threes.takeoff()

##Preformance act one
ones.flip("f")
twos.flip("b")


one.move_up(100)
three.move_up(50)
one.move_right(200)
two.move_left(200)
one.move_down(50)
two.move_up(50)
threes.move_down(25)

##Current Drone Positions (2, 3, 1)
threes.flip("f")
threes.flip("b")


##Landing/Ending Sequence
threes.land()
threes.end()

