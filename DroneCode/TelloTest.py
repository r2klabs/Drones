from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

#tello.command()
tello.flip('b')
tello.flip ('f')
tello.flip('l')
tello.flip('r')

#tello.move_left(100)
#tello.rotate_counter_clockwise(90)
#tello.move_forward(100)

tello.land()