import hal.hal_input_switch as input
import hal.hal_led as led
import time

def main():
    input.init()
    led.init()
    start_time = 0
    elapsed_time = 0

    while True:
        if input.read_slide_switch() == True:
            blink_led(5)

            start_time = 0
            elapsed_time = 0

        else:
            if start_time == 0:
                start_time = time.time()

            if elapsed_time < 5:
                blink_led(10)
                elapsed_time = time.time() - start_time
            
            led.set_output(0,0)

def blink_led(frequency):
    period = 1.0 / frequency
    led.set_output(0, 1)
    time.sleep(period / 2)
    led.set_output(0, 0)
    time.sleep(period / 2)

if __name__ == "__main__":
    main()
