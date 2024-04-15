class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Богдан", "Анонім", "Марко"]:
            raise ValueError("Дозволені імена: Богдан, Анонім, Марко")
        self.name = name

        # if hobby == "":
        #     raise ValueError("Хобі не введено")

a = Name("Марко", "Баскетбол")