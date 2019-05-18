

class Robot:
    def __init__(self,driver):
        self.driver = driver
        self.forward_speed = -50
        self.backward_speed = 50
        self.turn_slow = 2

    def left(self):
        self.driver.drive(1,self.backward_speed / self.turn_slow)
        self.driver.drive(2,self.forward_speed / self.turn_slow)

    def right(self):
        self.driver.drive(1,self.forward_speed / self.turn_slow)
        self.driver.drive(2,self.backward_speed / self.turn_slow)

    def stop(self):
        return self.driver.stop()

    def forward(self):
        return self.driver.driveBoth(self.forward_speed,self.forward_speed)

    def backward(self):
        return self.driver.driveBoth(self.backward_speed,self.backward_speed)
