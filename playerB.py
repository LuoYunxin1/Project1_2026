from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
left_button = Button(14)
right_button = Button(15)

left_name = input('Left player name: ')
right_name = input('Right player name: ')

left_score = 0
right_score = 0

while True:
    print('\n=== new game ===')
    print(f'score：{left_name} {left_score}  | {right_name} {right_score} ')
    led.on()
    sleep(uniform(5, 10))

    def pressed(button):
        global left_score, right_score
        if button.pin.number == 14:
            left_score += 1
            print(left_name + ' win the game！')
        else:
            right_score += 1
            print(right_name + ' win the game！')

    left_button.when_pressed = pressed
    right_button.when_pressed = pressed

    sleep(1)
