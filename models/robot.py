

class Robot:
    def __init__(self,driver):
        self.driver = driver
        self.forward_speed = -50
        self.backward_speed = 50
        self.turn_slow = 2
        self.offset = .10

    def left(self):
        self.driver.drive(1,self.forward_speed - 15)
        self.driver.drive(2,self.forward_speed)

    def right(self):
        self.driver.drive(1,self.forward_speed)
        self.driver.drive(2,self.backward_speed - 15)

    def stop(self):
        return self.driver.stop()

    def forward(self):
        offset_speed = (self.forward_speed * self.offset) + self.forward_speed
        self.driver.drive(1,offset_speed)
        self.driver.drive(2,self.forward_speed)

    def backward(self):
        self.driver.drive(1,self.backward_speed)
        self.driver.drive(2,self.backward_speed)
