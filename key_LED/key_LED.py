import utime
from Maix import GPIO
from fpioa_manager import fm

io_led_g = 12
io_led_r = 13
io_led_b = 14
io_key = 16


fm.register(io_led_g,fm.fpioa.GPIO0)
fm.register(io_key, fm.fpioa.GPIOHS1)

led_b = GPIO(GPIO.GPIO0,GPIO.OUT)
key = GPIO(GPIO.GPIOHS1, GPIO.IN)

led_b.value(1)

led_state = True

while(1):

    if key.value() == 0: # 等待按键按下
        led_state = not led_state
        led_b.value(led_state)

    while(key.value() == 0):
        utime.sleep_ms(20)


