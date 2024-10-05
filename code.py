import board
import digitalio
import time



class Display:
  
    segments = {
    'A': digitalio.DigitalInOut(board.GP0), 
    'B': digitalio.DigitalInOut(board.GP1), 
    'C': digitalio.DigitalInOut(board.GP2),
    'D': digitalio.DigitalInOut(board.GP3),
    'E': digitalio.DigitalInOut(board.GP4),
    'F': digitalio.DigitalInOut(board.GP5),
    'G': digitalio.DigitalInOut(board.GP6)
    }

    def __init__(self):
        # Establecer la dirección como salida
        for segment in self.segments.values():
            segment.direction = digitalio.Direction.OUTPUT
            segment.value = True

    def display_number(self, number):
        """
            True: apagado
            False: encendido
        """
        if number == 1:
            self.segments['B'].value = False  
            self.segments['C'].value = False
            self.segments['A'].value = True
            self.segments['D'].value = True
            self.segments['E'].value = True
            self.segments['F'].value = True
            self.segments['G'].value = True
        elif number == 2:
            self.segments['A'].value = False
            self.segments['B'].value = False
            self.segments['G'].value = False
            self.segments['E'].value = False
            self.segments['D'].value = False
            self.segments['C'].value = True
            self.segments['F'].value = True
        elif number == 3:
            self.segments['A'].value = False
            self.segments['B'].value = False
            self.segments['G'].value = False            
            self.segments['C'].value = False
            self.segments['D'].value = False
            self.segments['E'].value = True
            self.segments['F'].value = True
        elif number == 4:
            self.segments['F'].value = False
            self.segments['G'].value = False
            self.segments['B'].value = False
            self.segments['C'].value = False
            self.segments['A'].value = True
            self.segments['D'].value = True
            self.segments['E'].value = True
        elif number == 5:
            self.segments['A'].value = False
            self.segments['F'].value = False            
            self.segments['G'].value = False            
            self.segments['C'].value = False            
            self.segments['D'].value = False 
            self.segments['B'].value = True 
            self.segments['E'].value = True 
        elif number == 6:
            self.segments['A'].value = False
            self.segments['F'].value = False            
            self.segments['G'].value = False            
            self.segments['C'].value = False            
            self.segments['D'].value = False            
            self.segments['E'].value = False                        
            self.segments['B'].value = True                        
        elif number == 7:
            self.segments['A'].value = False
            self.segments['B'].value = False
            self.segments['C'].value = False
            self.segments['D'].value = True
            self.segments['E'].value = True
            self.segments['F'].value = True
            self.segments['G'].value = True
        elif number == 8:
            self.segments['A'].value = False
            self.segments['B'].value = False
            self.segments['C'].value = False
            self.segments['D'].value = False
            self.segments['E'].value = False
            self.segments['F'].value = False
            self.segments['G'].value = False
        elif number == 9:
            self.segments['A'].value = False
            self.segments['F'].value = False
            self.segments['B'].value = False
            self.segments['G'].value = False
            self.segments['C'].value = False            
            self.segments['D'].value = True            
            self.segments['E'].value = True            
        else: # cero
            for segment in self.segments.values():
                segment.value = True
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

display = Display()
yellow_led = Led(pin = board.GP17)
sensor_x = Sensor(pin = board.GP28)
sensor_y = Sensor(pin = board.GP16)
detection_seconds = 0

while True:
    
    if sensor_x.detect_inclination() or sensor_y.detect_inclination():
        detection_seconds += 1
        display.display_number(detection_seconds)
        if detection_seconds >= 5:
            yellow_led.turnon()
    else:
        yellow_led.turnoff()
        display.display_number(0)
        detection_seconds = 0
        
    time.sleep(1)
