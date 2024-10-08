import board
import digitalio
import time

class DisplayTotal:

    def __init__(self):

        self.displays = {
            "display_L": {
                'A': digitalio.DigitalInOut(board.GP0), 
                'B': digitalio.DigitalInOut(board.GP1), 
                'C': digitalio.DigitalInOut(board.GP2),
                'D': digitalio.DigitalInOut(board.GP3),
                'E': digitalio.DigitalInOut(board.GP4),
                'F': digitalio.DigitalInOut(board.GP5),
                'G': digitalio.DigitalInOut(board.GP6)
            },
            "display_R": {
                'A': digitalio.DigitalInOut(board.GP7), 
                'B': digitalio.DigitalInOut(board.GP8), 
                'C': digitalio.DigitalInOut(board.GP9),
                'D': digitalio.DigitalInOut(board.GP10),
                'E': digitalio.DigitalInOut(board.GP11),
                'F': digitalio.DigitalInOut(board.GP12),
                'G': digitalio.DigitalInOut(board.GP13)
            }
        }
        # Establecer la dirección como salida
        # for displays in self.displays.dicts():
        #     for segment in display.values():
        #         segment.direction = digitalio.Direction.OUTPUT
        #         segment.value = True
        
        for display in self.displays.keys():
            for segment, value in self.displays[display].items():
                self.displays[display][segment].direction = digitalio.Direction.OUTPUT
                self.displays[display][segment].value = True

    def display_number(self, display, number):
        """
            True: apagado
            False: encendido
        """
        if number == 0:
            self.displays[display]['A'].value = False
            self.displays[display]['B'].value = False
            self.displays[display]['C'].value = False
            self.displays[display]['D'].value = False
            self.displays[display]['E'].value = False
            self.displays[display]['F'].value = False
            self.displays[display]['G'].value = True
        elif number == 1:
            self.displays[display]['B'].value = False  
            self.displays[display]['C'].value = False
            self.displays[display]['A'].value = True
            self.displays[display]['D'].value = True
            self.displays[display]['E'].value = True
            self.displays[display]['F'].value = True
            self.displays[display]['G'].value = True
        elif number == 2:
            self.displays[display]['A'].value = False
            self.displays[display]['B'].value = False
            self.displays[display]['G'].value = False
            self.displays[display]['E'].value = False
            self.displays[display]['D'].value = False
            self.displays[display]['C'].value = True
            self.displays[display]['F'].value = True
        elif number == 3:
            self.displays[display]['A'].value = False
            self.displays[display]['B'].value = False
            self.displays[display]['G'].value = False            
            self.displays[display]['C'].value = False
            self.displays[display]['D'].value = False
            self.displays[display]['E'].value = True
            self.displays[display]['F'].value = True
        elif number == 4:
            self.displays[display]['F'].value = False
            self.displays[display]['G'].value = False
            self.displays[display]['B'].value = False
            self.displays[display]['C'].value = False
            self.displays[display]['A'].value = True
            self.displays[display]['D'].value = True
            self.displays[display]['E'].value = True
        elif number == 5:
            self.displays[display]['A'].value = False
            self.displays[display]['F'].value = False            
            self.displays[display]['G'].value = False            
            self.displays[display]['C'].value = False            
            self.displays[display]['D'].value = False 
            self.displays[display]['B'].value = True 
            self.displays[display]['E'].value = True 
        elif number == 6:
            self.displays[display]['A'].value = False
            self.displays[display]['F'].value = False            
            self.displays[display]['G'].value = False            
            self.displays[display]['C'].value = False            
            self.displays[display]['D'].value = False            
            self.displays[display]['E'].value = False                        
            self.displays[display]['B'].value = True                        
        elif number == 7:
            self.displays[display]['A'].value = False
            self.displays[display]['B'].value = False
            self.displays[display]['C'].value = False
            self.displays[display]['D'].value = True
            self.displays[display]['E'].value = True
            self.displays[display]['F'].value = True
            self.displays[display]['G'].value = True
        elif number == 8:
            self.displays[display]['A'].value = False
            self.displays[display]['B'].value = False
            self.displays[display]['C'].value = False
            self.displays[display]['D'].value = False
            self.displays[display]['E'].value = False
            self.displays[display]['F'].value = False
            self.displays[display]['G'].value = False
        elif number == 9:
            self.displays[display]['A'].value = False
            self.displays[display]['F'].value = False
            self.displays[display]['B'].value = False
            self.displays[display]['G'].value = False
            self.displays[display]['C'].value = False            
            self.displays[display]['D'].value = True            
            self.displays[display]['E'].value = True     

    def display_counter(self, cont):
        if cont > 10:
            pass
        else:
            pass

class Led():

    def __init__(self, pin):
        self.led_pin = digitalio.DigitalInOut(pin)
        self.led_pin.direction = digitalio.Direction.OUTPUT

    def display_led(self):
        while True:
            self.led_pin.value = True   # Encender la LED
            time.sleep(1)      # Mantener encendida por 1 segundo
            self.led_pin.value = False  # Apagar la LED
            time.sleep(1)      # Mantener apagada por 1 segundo

    def turnon(self):
        self.led_pin.value = True   # Encender la LED

    def turnoff(self):
        self.led_pin.value = False


class Sensor():
    def __init__(self, pin):
        self.sensor_pin = digitalio.DigitalInOut(pin)
        self.sensor_pin.direction = digitalio.Direction.INPUT

    def detect_inclination(self):
        if self.sensor_pin.value:
            return True
        else:
            return False


display = DisplayTotal()
yellow_led = Led(pin = board.GP17)
red_led = Led(pin = board.GP18)
sensor_x = Sensor(pin = board.GP28)
sensor_y = Sensor(pin = board.GP16)
detection_seconds = 0

while True:
    
    if sensor_x.detect_inclination() or sensor_y.detect_inclination():
        detection_seconds += 1
        display.display_number("display_L", detection_seconds)
        if detection_seconds >= 5:
            yellow_led.turnon()
        if detection_seconds >= 15:
            red_led.turnon()
    else:
        yellow_led.turnoff()
        red_led.turnoff()
        display.display_number("display_L", 0)
        detection_seconds = 0
        
    time.sleep(1)
