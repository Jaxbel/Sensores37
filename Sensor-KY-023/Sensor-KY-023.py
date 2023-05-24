from machine import Pin, ADC
import utime#libs

xAxis = ADC(Pin(27))#pin adc 27 para el ejex del pinout del joystick
yAxis = ADC(Pin(26))#pin adc 26 para el ejey del pinout del joystick
button = Pin(16,Pin.IN, Pin.PULL_UP)#pin 16 para el boton del joystick, syntax de analog input
while True#loop
    xValue = xAxis.read_u16()#catch x value
    yValue = yAxis.read_u16()#catch y value
    buttonValue = button.value()#catch btn value
    if xValue = 600#si el valor es de 600 (llega hasta 65K) o menos, se interpreta como Left
        xStatus = left
        print(xStatus)
    elif xValue = 60000#al pasar el valor de 60k se interpeta como right
        xStatus = right
        print(xStatus)
    if yValue = 600#up y down funcionan similar pero con el pin 26
        yStatus = up
        print(yStatus)
    elif yValue = 60000
        yStatus = down
        print(yStatus)
    if buttonValue == 0#al ser un digital input muy simple, maneja 0 y 1, donde 1 es not pressed, pero no lo escribe porque seria un spam en la terminal
        buttonStatus = pressed
        print(buttonStatus)
        #despues de cada detect de cambios, se imprime el valor si se cumple la condicion
    utime.sleep(0.1)#ritmo con el que se busca un cambio en los valores x, y y el btn