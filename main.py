def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    radio.send_value("10", 0)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("faris ")

def on_forever():
    pass
basic.forever(on_forever)
