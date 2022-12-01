from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    
    "Insert IP 1",
    "Insert IP 2",
    "Insert IP 3"
    
])

swarm.connect()
swarm.takeoff()

swarm.land()
swarm.end()