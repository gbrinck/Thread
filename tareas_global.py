#Programa que maneja una tarea adicional
import machine
import utime
import _thread

led_int = machine.Pin(25, machine.Pin.OUT)
led_ext = machine.Pin(15, machine.Pin.OUT)

global led_status
led_status = 'vacio'
print (led_status)

def tarea_secundaria():
    while True:
        led_int.value(1)
        global led_status
        led_status ='Led interno encendido'
        print ('from sec', led_status)
        utime.sleep(1)
        led_int.value(0)
        utime.sleep(1)
        
_thread.start_new_thread(tarea_secundaria, ())

#comienzo de mi tarea principal
while True:
    led_ext.value(1)
    print ('from pri ',led_status)
    utime.sleep(.3)
    led_ext.value(0)
    utime.sleep(.3)
