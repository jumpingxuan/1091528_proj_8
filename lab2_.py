import RPi.GPIO as GPIO
import time

LED_PINS = [16, 18]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PINS[0], GPIO.OUT)
GPIO.setup(LED_PINS[1], GPIO.OUT)
pattern=1

def ButtonPressed(btn):
    global pattern
    if pattern==1:
        GPIO.output(LED_PINS[0], GPIO.HIGH)
        GPIO.output(LED_PINS[1], GPIO.HIGH)
        print("1")
    elif pattern==2:
        GPIO.output(LED_PINS[0], GPIO.LOW)
        GPIO.output(LED_PINS[1], GPIO.LOW)
        print("2")
    elif pattern==0:
        print("3")
        counter=1
        time.sleep(0.2)
        while True:
            input = GPIO.input(BTN_PIN)
            if input==GPIO.LOW:
               break
            for i in range(2):
                if (counter >> i) & 0x00000001:
                    GPIO.output(LED_PINS[i], GPIO.HIGH)
                else:
                    GPIO.output(LED_PINS[i], GPIO.LOW)
            counter = counter << 1
            if counter > 2:
                counter = 1
            time.sleep(1)
           

    pattern=(pattern+1)%3





GPIO.setmode(GPIO.BOARD)
BTN_PIN = 15
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, ButtonPressed, 200)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")
finally:
    GPIO.cleanup()