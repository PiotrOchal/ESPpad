import serial
import vgamepad as vg
ser= serial.Serial('COM3',512000)
gamepad = vg.VX360Gamepad()

jlx=0
jly=0
jrx=0
jry=0
while True :
    s = ser.read(1)
    # ABXY buttons
    if str(s) == "b'R'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)

    elif str(s) == "b'L'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    elif str(s) == "b'a'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

    elif str(s) == "b'b'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

    elif str(s) == "b'x'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

    elif str(s) == "b'y'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    elif str(s) == "b'^'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

    elif str(s) == "b'v'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)

    elif str(s) == "b'<'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

    elif str(s) == "b'>'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    # joystic
    elif str(s) == "b'J'":
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
        #print('prawy X: '+str(jrx))
        #print('prawy Y: ' + str(jry))
        gamepad.left_joystick_float(x_value_float=float((jlx) / 2048), y_value_float=float((jly)/2048))
        gamepad.right_joystick_float(x_value_float=float(jrx / 2048), y_value_float=float(jry / 2048))

    # triggers
    elif str(s) == "b'T'":
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
