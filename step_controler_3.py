def main():
    import time
    from pymata4 import pymata4

    num_steps = 32
    pins1 = [2, 4, 3, 5]
    pins2 = [6, 8, 7, 9]
    #pins3 = [10, 12, 11, 13]
    board = pymata4.Pymata4(com_port="COM6")
    board.shutdown_on_exception = False

    def fold():
        board.start()
        motorSpeed = 5
        angle = 100
        board.set_pin_mode_stepper(num_steps, pins2)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625))
        time.sleep(5)
        angle = -130
        board.set_pin_mode_stepper(num_steps, pins1)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625))
        time.sleep(7)
        angle = -30
        board.set_pin_mode_stepper(num_steps, pins2)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625))
        time.sleep(2)
        angle = 180
        board.set_pin_mode_stepper(num_steps, pins1)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625))
        time.sleep(10)
        angle = -105
        board.set_pin_mode_stepper(num_steps, pins2)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625))
        time.sleep(6)
    fold()
