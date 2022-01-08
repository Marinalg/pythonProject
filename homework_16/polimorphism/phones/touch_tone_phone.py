from homework_16.polimorphism.phones.phone import Phone


class  Touch_tone_phone(Phone):
    def__init__(self, color: str, year: int)->None:
      super().__init__(color, year)
      self.__press_button_answer() = False
      self.__press_button_resert() = False


    def call(self):
       self.__tap_button_answer() = True

