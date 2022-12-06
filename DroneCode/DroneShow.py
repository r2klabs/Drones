from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    
    "Insert IP 1",
    "Insert IP 2",
    "Insert IP 3",
    "Insert IP 4"
    
])


swarm.connect()
swarm.takeoff()

swarm.parrallel(lambda i, tello: tello.move(up, 20))
swarm.parrallel(lambda i, tello: tello.move(down, 20))


swarm.land()
swarm.end()