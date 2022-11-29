from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    
    "192.168.53.192",
    "192.168.53.124",
    "192.168.53.85"
    
])

swarm.connect()
swarm.takeoff()

swarm.land()
swarm.end()