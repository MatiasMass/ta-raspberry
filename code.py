import board
import digitalio
import time


class Display:
  
    segments = {
    'A': digitalio.DigitalInOut(board.GP1),
    'B': digitalio.DigitalInOut(board.GP0),
    'C': digitalio.DigitalInOut(board.GP5),
    'D': digitalio.DigitalInOut(board.GP7),
    'E': digitalio.DigitalInOut(board.GP3),
    'F': digitalio.DigitalInOut(board.GP6),
    'G': digitalio.DigitalInOut(board.GP2)
    }

    def __init__(self):
        # Establecer la dirección como salida
        for segment in self.segments.values():
            segment.direction = digitalio.Direction.OUTPUT
            segment.value = True

    def show_numbers(self):

        while True:
            self.segments['C'].value = False # Encender segmento

            time.sleep(2)

            self.segments['C'].value = True  # Apagar el segmento 

            time.sleep(2)

    def display_number(self, number):
        if number == 1:
            self.segments['B'].value = False
            self.segments['C'].value = False
        elif number == 2:
            self.segments['A'].value = False
            self.segments['B'].value = False
            self.segments['G'].value = False
            self.segments['E'].value = False
            self.segments['D'].value = False
        elif number == 3:
            self.segments['A'].value = False
            self.segments['B'].value = False
            self.segments['G'].value = False            
            self.segments['C'].value = False
            self.segments['D'].value = False
        elif number == 4:
            self.segments['F'].value = False
            self.segments['G'].value = False
            self.segments['B'].value = False
            self.segments['C'].value = False
        elif number == 5:
            self.segments['A'].value = False
            self.segments['F'].value = False            
            self.segments['G'].value = False            
            self.segments['C'].value = False            
            self.segments['D'].value = False 
        elif number == 6:
            self.segments['A'].value = False
            self.segments['F'].value = False            
            self.segments['G'].value = False            
            self.segments['C'].value = False            
            self.segments['D'].value = False            
            self.segments['E'].value = False                        
        elif number == 7:
            self.segments['A'].value = False
            self.segments['B'].value = False
            self.segments['C'].value = False
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
    
display = Display()

#display.show_numbers()
while True:
    display.display_number(1)