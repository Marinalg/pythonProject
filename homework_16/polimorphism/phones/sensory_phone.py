from homework_16.polimorphism.phones.phone import Phone

class Sensory_phone(Phone):
   def__init__(self,color: str,year:int)->None:
        super().__init__(color,year)
        self.__tap_button_answer() = False
        self.__tap_button_reset() = False

   def call(self):
     self.__tap_button_answer() = True



