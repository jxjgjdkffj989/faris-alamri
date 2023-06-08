input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Heart)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    radio.sendValue("10", 0)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showNumber(1)
})
basic.showString("faris ")
basic.forever(function on_forever() {
    
})
