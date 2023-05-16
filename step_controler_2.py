def main():
    import time
    from pymata4 import pymata4

    num_steps = 32
    pins1 = [2, 3, 4, 5]
    pins2 = [6, 7, 8, 9]
    pins3 = [10, 11, 12, 13]
    board = pymata4.Pymata4(com_port="COM6")

    def unfold():
        motorSpeed = 5
        angle = -190
        board.set_pin_mode_stepper(num_steps, pins1)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625)) 
        time.sleep(8)
        angle = -45
        board.set_pin_mode_stepper(num_steps, pins2)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625)) 
        time.sleep(4)
        angle = -100
        board.set_pin_mode_stepper(num_steps, pins3)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625)) 
        time.sleep(6)
        angle = -45
        board.set_pin_mode_stepper(num_steps, pins2)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625)) 
        time.sleep(4)
        angle = 90
        board.set_pin_mode_stepper(num_steps, pins3)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625)) 
        time.sleep(6)
        angle = -180
        board.set_pin_mode_stepper(num_steps, pins1)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625)) 
        time.sleep(9)
        angle = -165
        board.set_pin_mode_stepper(num_steps, pins2)
        time.sleep(1)
        board.stepper_write(motorSpeed * 50, int(angle*5.625)) 
        time.sleep(9)
    unfold()