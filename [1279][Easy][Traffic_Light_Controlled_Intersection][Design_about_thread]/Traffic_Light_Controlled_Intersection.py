## https://code.dennyzhang.com/traffic-light-controlled-intersection
## Basic Ideas: mutex
# leetcode time     cost : 68 ms
# leetcode memory   cost : 14.9 MB 
from threading import Semaphore
class TrafficLight:
    def __init__(self):
        # initialize a mutex
        self.m = Semaphore(1)
        self.light = 1 # which light

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        self.m.acquire()
        if self.light != roadId:
            turnGreen()
            self.light = roadId
        crossCar()
        self.m.release()