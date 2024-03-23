class Student:
    __valid_houses__ = ('Gryffendor', 'HufflePoffle', 'Ravenclew', 'Slytherin')

    def __init__(self, name: str, house: str) -> None:
        self.__validate_house__(name)
        self.name = name
        self.__validate_house__(house) 
        self.house = house
    def __validate_name__(self,name :str) -> Exception:
        if not name:
            raise ValueError
    def __validate_house__(self,house:str) -> Exception:
        if house not in self.__valid_houses__:
            raise ValueError
    @property
    def house(self):
        return self.house
    @house.getter
    def house(self, house: str) -> str:
        return self.house 
    @property
    def name(self):
        return self.name
    @name.getter
    def name(self, name: str) -> str:
        return self.name   
    def __str__(self) -> str:
        return f'{self.name} from {self.house}'


def main():
    student = Student('Harry', 'Something wrong!')
    print(student)

def get_name() -> str: return input("Name: ") 

def get_house() -> str: return input("House: ")

if __name__ == "__main__":
    main()
