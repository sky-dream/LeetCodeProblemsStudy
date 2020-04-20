# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.9 MB 
# Time:  O(n)
# Space: O(1)
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/traffic-light-controlled-intersection.py
import threading
class TrafficLight(object):    
    def __init__(self):
        self.__lock = threading.Lock()
        self.__light = 1

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        """
        :type roadId: int --> // ID of the car
        :type carId: int --> // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        :type direction: int --> // Direction of the car
        :type turnGreen: method --> // Use turnGreen() to turn light to green on current road
        :type crossCar: method --> // Use crossCar() to make car cross the intersection
        :rtype: void
        """
        with self.__lock:
            if self.__light != roadId:
                self.__light = roadId
                turnGreen()
            crossCar()