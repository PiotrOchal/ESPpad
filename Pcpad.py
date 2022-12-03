import serial
import vgamepad as vg
import numpy as np
import time
ser= serial.Serial('COM3',512000)
gamepad = vg.VX360Gamepad()






def my_callback(client, target, large_motor, small_motor, led_number, user_data):
    """
    Callback function triggered at each received state change


    :param large_motor: integer in [0, 255] representing the state of the large motor
    :param small_motor: integer in [0, 255] representing the state of the small motor

    """
    # Do your things here. For instance:
    #print(f"Received notification for client {client}, target {target}")
    #print(f"large motor: {large_motor}, small motor: {small_motor}")

    #print('kolejny')
    while True:
        s = ser.read(1)
        if str(s) == "b'm'":break


    ser.write(np.uint8(small_motor))
    ser.write(np.uint8(large_motor))
    '''
    #print('small:'+str(small_motor)+',big:'+str(large_motor))
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
'''




    #print(f"led number: {led_number}")



gamepad . register_notification ( callback_function = my_callback )





while True :


    s = ser.read(1)
    # ABXY buttons
    if str(s) == "b'e'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)

        elif str(s) == "b'1'":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        gamepad.update()
    elif str(s) == "b'q'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)


        elif str(s) == "b'1'":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        gamepad.update()
    elif str(s) == "b'a'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)


        elif str(s) == "b'1'":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.update()
    elif str(s) == "b'b'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)


        elif str(s) == "b'1'":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()
    elif str(s) == "b'x'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)


        elif str(s) == "b'1'":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        gamepad.update()
    elif str(s) == "b'y'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)


        elif str(s) == "b'1'":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        gamepad.update()
    elif str(s) == "b'^'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)


        elif str(s) == "b'1'":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        gamepad.update()
    elif str(s) == "b'v'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)


        elif str(s) == "b'1'":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.update()
    elif str(s) == "b'<'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)


        elif str(s) == "b'1'":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        gamepad.update()
    elif str(s) == "b'>'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)


        elif str(s) == "b'1'":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.update()
    # joystic
    elif str(s) == "b'J'":
        s = ser.read(1)
        if str(s) == "b'L'":
            s = ser.read(1)
            if str(s) == "b'x'":
                j = ser.read(4)
                try:jlx = int(str(j)[2:6])-3048
                except:
                    print('cos nie tak')
            elif str(s) == "b'y'":
                j = ser.read(4)
                try:jly = int(str(j)[2:6]) - 3048
                except:
                    print('cos nie tak')
            try:
                gamepad.left_joystick_float(x_value_float=float((jlx) / 2048), y_value_float=float((jly) / 2048))
                gamepad.update()
            except:
                print('cos nie tak')

        elif str(s) == "b'R'":
            s = ser.read(1)
            if str(s) == "b'x'":
                j = ser.read(4)
                try:jrx = int(str(j)[2:6])-3048
                except:
                    print('cos nie tak')
            elif str(s) == "b'y'":
                j = ser.read(4)
                try:jry = int(str(j)[2:6]) - 3048
                except:
                    print('cos nie tak')
        #print('prawy X: '+str(jrx))
        #print('prawy Y: ' + str(jry))

            try:
                gamepad.right_joystick_float(x_value_float=float(jrx / 2048), y_value_float=float(jry / 2048))
                gamepad.update()
            except:
                print('cos nie tak')

    # triggers
    elif str(s) == "b'T'":
        s = ser.read(1)
        if str(s) == "b'l'":
            t = ser.read(4)
            tl=int(str(t)[2:6])-1000
            gamepad.left_trigger_float(value_float=float(tl/4095))
            gamepad.update()

        elif str(s) == "b'r'":
            t = ser.read(4)
            tr=int(str(t)[2:6])-1000
            gamepad.right_trigger_float(value_float=float(tr/4095))
            gamepad.update()

    #else: gamepad.register_notification(callback_function=my_callback)



    gamepad.update()

    #gamepad.register_notification(callback_function=my_callback)
