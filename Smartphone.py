class Phone:
    def __init__(self, company, model, year, state, exploitation, processor, display, battery, camera):
        self._company = company
        self._model = model
        self._year = year
        self._state = state
        self._exploitation = exploitation
        self.processor = processor
        self.display = display
        self.battery = battery
        self.camera = camera

    def set_company(self, company: str) -> None:
        self._company = company

    def set_model(self, model: str) -> None:
        self._model = model

    def set_year(self, year: str) -> None:
        self._year = year

    def set_state(self, state: str) -> None:
        self._state = state

    def set_exploitation(self, exploitation: str) -> None:
        self._exploitation = exploitation

    def __str__(self) -> str:
        return f"Company: {self._company}, Model: {self._model}, Year: {self._year}, State: {self._state}, Exploitation: {self._exploitation}\nProcessor: {self.processor}\nDisplay: {self.display}\nBattery: {self.battery}\nCamera: {self.camera}"

class Processor:
    def __init__(self, brand: str, cores: int, frequency: float):
        self._brand = brand
        self._cores = cores
        self._frequency = frequency

    def set_brand(self, brand: str) -> None:
        self._brand = brand

    def set_cores(self, cores: int) -> None:
        self._cores = cores

    def set_frequency(self, frequency: float) -> None:
        self._frequency = frequency

    def get_brand(self) -> str:
        return self._brand

    def get_cores(self) -> int:
        return self._cores

    def get_frequency(self) -> float:
        return self._frequency

    def __str__(self) -> str:
        return f"Процессор: {self._brand}\nКоличество ядер: {self._cores}\nЧастота: {self._frequency} ГГц"
       
class Display:
    def __init__(self, size: float, resolution: str):
        self._size = size
        self._resolution = resolution

    def get_size(self) -> float:
        return self._size

    def set_size(self, size: float) -> None:
        self._size = size

    def get_resolution(self) -> str:
        return self._resolution

    def set_resolution(self, resolution: str) -> None:
        self._resolution = resolution

    def __str__(self) -> str:
        return f"Диагональ экрана: {self._size} дюймов\nРазрешение экрана: {self._resolution}"
        
class Battery:
    def __init__(self, capacity: int, power: int):
        self._capacity = capacity
        self._power = power

    def set_capacity(self, capacity: int) -> None:
        self._capacity = capacity

    def set_power(self, power: int) -> None:
        self._power = power

    def get_capacity(self) -> int:
        return self._capacity

    def get_power(self) -> int:
        return self._power

    def __str__(self) -> str:
        return f"Емкость батареи: {self._capacity} мАч\nМощность: {self._power} Вт"
        
class Camera:
    def __init__(self, name: str, resolution: int, lens: str):
        self._name = name
        self._resolution = resolution
        self._lens = lens

    def set_name(self, name: str) -> None:
        self._name = name

    def set_resolution(self, resolution: int) -> None:
        self._resolution = resolution

    def set_lens(self, lens: str) -> None:
        self._lens = lens

    def get_name(self) -> str:
        return self._name

    def get_resolution(self) -> int:
        return self._resolution

    def get_lens(self) -> str:
        return self._lens

    def __str__(self) -> str:
        return f"Камера: {self._name}\nМегапиксели: {self._resolution}\nДиафрагма: {self._lens}"

class Iphone(Phone):
    def __init__(self, company, model, year, state, exploitation, processor, display, battery, camera):
        super().__init__(company, model, year, state, exploitation, processor, display, battery, camera)

    def print_info_phone(self):
        print("Характеристика айфона")
        print(f"Компания: {self._company}")
        print(f"Модель: {self._model}")
        print(f"Год: {self._year}")
        print(f"Состояние: {self._state}")
        print(f"Время использования: {self._exploitation}")
        print(self.processor)
        print(self.display)
        print(self.battery)
        print(self.camera)
        
class AndroidPhone(Phone):
    def __init__(self, company, model, year, state, exploitation, processor, display, battery, camera):
        super().__init__(company, model, year, state, exploitation, processor, display, battery, camera)

    def print_info_phone(self):
        print("Характеристика андроида:")
        print(f"Компания: {self._company}")
        print(f"Модель: {self._model}")
        print(f"Год: {self._year}")
        print(f"Состояние: {self._state}")
        print(f"Время использования: {self._exploitation}")
        print(self.processor)
        print(self.display)
        print(self.battery)
        print(self.camera)
    
    def compare_phone(self, other_phone):
        differences = []

        def compare_attributes(attr_name, attr_value, other_value):
            if attr_value != other_value:
                differences.append(f"{attr_name}: {attr_value} не совпадает с  {other_value}")

        print(f"Сравнение телефона {self._company} {self._model} и {other_phone._company} {other_phone._model}:")

        compare_attributes("Год", self._year, other_phone._year)
        compare_attributes("Состояние", self._state, other_phone._state)
        compare_attributes("Время использования", self._exploitation, other_phone._exploitation)

        compare_attributes("Ядра процессора", self.processor.get_cores(), other_phone.processor.get_cores())
        compare_attributes("Частота процессора", self.processor.get_frequency(), other_phone.processor.get_frequency())

        compare_attributes("Диагональ экрана", self.display.get_size(), other_phone.display.get_size())
        compare_attributes("Разрешение экрана", self.display.get_resolution(), other_phone.display.get_resolution())

        compare_attributes("Емкость батареи", self.battery.get_capacity(), other_phone.battery.get_capacity())
        compare_attributes("Мощность батареи", self.battery.get_power(), other_phone.battery.get_power())

        compare_attributes("Разрешение камеры", self.camera.get_resolution(), other_phone.camera.get_resolution())
        compare_attributes("Диафрагма камеры", self.camera.get_lens(), other_phone.camera.get_lens())

        if differences:
            print("Обнаружены различия:")
            for difference in differences:
                print(difference)
        else:
            print("Все характеристики совпадают.")

# Пример использования полиморфизма
processor1 = Processor("Snapdragon 865", 8, 2.8)
display1 = Display(6.5, '1040x2000')
battery1 = Battery(5000, 100)
camera1 = Camera("Sony IMX586", 12, "f/1.7")

processor2 = Processor("Bionic M3", 8, 2.84)
display2 = Display(6.55, '1080x2400')
battery2 = Battery(4500, 65)
camera2 = Camera("Iphone 11", 48, "f/1.8")

phone1 = AndroidPhone("Samsung", "Galaxy S20", "2020", "рабочий", "2 года", processor1, display1, battery1, camera1)
phone2 = Iphone("Apple", "iPhone 12", "2021", "рабочий", "3 года", processor2, display2, battery2, camera2)

phone1.print_info_phone()
print()
phone2.print_info_phone()
print()
print("Сравнение андроида и айфона: ")
phone1.compare_phone(phone2)
