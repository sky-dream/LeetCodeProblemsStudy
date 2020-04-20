// leetcode time     cost : 204 ms
// leetcode memory   cost : 8.9 MB
// Time:  O(n)
// Space: O(1)
// https://github.com/kamyu104/LeetCode-Solutions/blob/master/C++/traffic-light-controlled-intersection.cpp
#include <mutex>
using namespace std;
class TrafficLight {
public:
    TrafficLight()
     : light_{1} {
        
    }
    void carArrived(
        int carId,                   // ID of the car
        int roadId,                  // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        int direction,               // Direction of the car
        function<void()> turnGreen,  // Use turnGreen() to turn light to green on current road
        function<void()> crossCar    // Use crossCar() to make car cross the intersection
    ) {
        unique_lock<mutex> lock{m_};
        if (light_ != roadId) {
            light_ = roadId;
			turnGreen();
		}
        crossCar();
    }

private:
    mutex m_;
    int light_;
};