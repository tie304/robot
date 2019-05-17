

class Robot:
    def __init__(self,driver):
        self.driver = driver
        self.forward_speed = 50
        self.backward_speed = -50

    def left(self):
        pass

    def right(self):
        pass

    def stop(self):
        return self.driver.stop()

    def forward(self):
        self.driver.driveBoth(self.forward_speed,self.forward_speed)

    def backward(self):
        return self.driver.driveBoth(self.backward_speed,self.backward_speed)
