class Car:
    def __init__(self, type_engine: str, color: str, model: str ) ->None:
        self.__type_engine = type_engine
        self.__color = color
        self.__model = model

    def __modify__private_key(self, key: str) ->str:
        return key.replace(f"_{self.__class__.name__}__","")


    def __str__(self):
        start ="{\n"
        content = ""
        end = "}"
        for key, value in self.__dict__.items():
            content += f"\t{self.__modify__private_key()}: {value}\n"

        return f"{start}{content}{end}"


