from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
left_button = Button(14)
right_button = Button(15)

left_name = input('Left player name: ')
right_name = input('Right player name: ')

while True:
    print('\n=== 新一局开始！LED 已亮起 ===')
    led.on()
    sleep(uniform(5, 10))  
    led.off()
    print('LED 已熄灭！按按钮！')

    def pressed(button):
        if button.pin.number == 14:
            print(left_name + ' 赢了！')
        else:
            print(right_name + ' 赢了！')
        
    left_button.when_pressed = pressed
    right_button.when_pressed = pressed

    sleep(1)
