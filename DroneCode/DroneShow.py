from djitellopy import TelloSwarm

#swarm = TelloSwarm.fromIps([
    
 #   "192.168.194.85",
  #  "192.168.194.124",
   # "192.168.194.208"
  
    
#])

one = TelloSwarm.fromIps([
    "192.168.194.85",
    "192.168.194.119"
])

two = TelloSwarm.fromIps([
    "192.168.194.124"#,
    #"192.168.194.105"
])

three = TelloSwarm.fromIps([
    "192.168.194.85",
    "192.168.194.119",
    "192.168.194.124"#,
])


one.connect()
two.connect()
#one.takeoff()
#two.takeoff()
three.connect()
three.takeoff()
#swarm.connect()
#swarm.takeoff()

one.flip("f")
two.flip("b")
two.move_up(60)
three.land()
#one.land()
#two.land()
#one.end()
#two.end()
three.end()


#swarm.land()
#swarm.end()