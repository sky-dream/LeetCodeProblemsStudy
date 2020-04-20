// leetcode time     cost : 15 ms
// leetcode memory   cost : 40.1 MB
// use JAVA semaphore（信号量）
class TrafficLight {
    private Semaphore greenLight;//红绿灯遥控器
    private boolean road1CanGo;//表示道路1是绿灯
    private boolean road2CanGo;//表示道路2是绿灯

    public TrafficLight() {
        this.greenLight = new Semaphore(1, true);
        this.road1CanGo = true;
        this.road2CanGo = false;
    }

    public void carArrived(
            int carId,           // ID of the car
            int roadId,          // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            int direction,       // Direction of the car
            Runnable turnGreen,  // Use turnGreen.run() to turn light to green on current road
            Runnable crossCar    // Use crossCar.run() to make car cross the intersection
    ) {
        try {
            greenLight.acquire();//申请获取遥控器
            //如果当前车道已经是绿灯了，直接通过
            if ((roadId == 1 && road1CanGo) || (roadId == 2 && road2CanGo)) crossCar.run();
            else if (roadId == 1 && !road1CanGo) {//否则，如果道路1不是绿灯，用遥控器变成绿灯
                turnGreen.run();
                road1CanGo = true;
                road2CanGo = false;
                crossCar.run();
            } else if (roadId == 2 && !road2CanGo) {//如果道路2不是绿灯，用遥控器变成绿灯
                turnGreen.run();
                road2CanGo = true;
                road1CanGo = false;
                crossCar.run();
            }
            greenLight.release();//最后把遥控器归还
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}