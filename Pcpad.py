import serial
import vgamepad as vg
ser= serial.Serial('COM3',9600)
gamepad = vg.VX360Gamepad()

while True :
    s = ser.read(1)  # reading up to 100 bytes
    if str(s) == "b'a'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            #print("tu jest a nie wciscniiete")
        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            #print("tu jest a wciscniiete")

    if str(s) == "b'b'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            #print("tu jest b nie wciscniiete")
        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            #print("tu jest b wciscniiete")

    if str(s) == "b'x'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            #print("tu jest x nie wciscniiete")
        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            #print("tu jest x wciscniiete")

    if str(s) == "b'y'":
        s = ser.read(1)
        if str(s) == "b'0'":
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            #print("tu jest y nie wciscniiete")
        else:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            #print("tu jest y wciscniiete")



    if str(s) == "b'J'":
        s = ser.read(1)
        if str(s) == "b'l'":
            s = ser.read(1)
            if str(s) == "b'x'":
                j = ser.read(4)
                jlx=int(str(j)[2:6])-3048
                gamepad.left_joystick_float(x_value_float=float(jlx/2048), y_value_float=0.0)
                #print("polożenie x  "+str(jlx))

    if str(s) == "b'T'":###docelowo zmienić na T l
        s = ser.read(1)
        if str(s) == "b'l'":
            t = ser.read(4)
            tl=int(str(t)[2:6])-1000
            gamepad.left_trigger_float(value_float=float(tl/4095))
            #print("triger "+str(tl))
        if str(s) == "b'r'":
            t = ser.read(4)
            tr=int(str(t)[2:6])-1000
            gamepad.right_trigger_float(value_float=float(tr/4095))
            #print("triger r  "+str(tr))
    gamepad.update()