#created by Piotr Ochal

import serial
import vgamepad as vg
ser= serial.Serial('COM3',9600)#serial port
gamepad = vg.VX360Gamepad()

jlx=0
jly=0
jrx=0
jry=0
while True :
    s = ser.read(1)
    # ABXY buttons
    if str(s) == "b'a'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

    if str(s) == "b'b'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

    if str(s) == "b'x'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

    if str(s) == "b'y'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

    # joystic
    if str(s) == "b'J'":
        s = ser.read(1)
        if str(s) == "b'l'":
            s = ser.read(1)
            if str(s) == "b'x'":
                j = ser.read(4)
                jlx = int(str(j)[2:6])-3048
            if str(s) == "b'y'":
                j = ser.read(4)
                jly = int(str(j)[2:6]) - 3048
        elif str(s) == "b'r'":
            s = ser.read(1)
            if str(s) == "b'x'":
                j = ser.read(4)
                jrx = int(str(j)[2:6])-3048
            if str(s) == "b'y'":
                j = ser.read(4)
                jry = int(str(j)[2:6]) - 3048

        gamepad.left_joystick_float(x_value_float=float(jlx / 2048), y_value_float=jly/2048)
        gamepad.right_joystick_float(x_value_float=float(jrx / 2048), y_value_float=jry / 2048)

    # triggers
    if str(s) == "b'T'":
        s = ser.read(1)
        if str(s) == "b'l'":
            t = ser.read(4)
            tl=int(str(t)[2:6])-1000
            gamepad.left_trigger_float(value_float=float(tl/4095))

        elif str(s) == "b'r'":
            t = ser.read(4)
            tr=int(str(t)[2:6])-1000
            gamepad.right_trigger_float(value_float=float(tr/4095))

    gamepad.update()
