
from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
left_button = Button(14)
right_button = Button(15)

left_name = input("left player name：")
right_name = input("right player name：")

left_score = 0
right_score = 0

while True:
    print("\n===== new game =====")
    print(f"score：{left_name} {left_score}  | {right_name} {right_score} ")
    
    led.on()
    print("LED on, wait for the LED to go out...")
    sleep(uniform(5, 10))
    
    led.off()
    print("LED off！Press！")

    def pressed(button):
        global left_score, right_score
        if button.pin.number == 14:
            left_score += 1
            print(f" {left_name} won the game !")
        else:
            right_score += 1
            print(f" {right_name} won the game !")

    left_button.when_pressed = pressed
    right_button.when_pressed = pressed

     sleep(5)
