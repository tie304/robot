

class Robot:
    def __init__(self,diver):
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
        return self.diver.driveBoth(self.forward_speed,self.forward_speed)

    def backward(self):
        return self.diver.driveBoth(self.backward_speed,self.backward_speed)
