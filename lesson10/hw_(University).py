from datetime import date


class University:
    pass


class People:
    def __init__(self, name: str, surname: str, patronymic: str, 
                 birth_day: date, phone: str):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth_day = birth_day
        self.phone = phone


class Student(People):
    def __init__(self, name: str, surname: str, patronymic: str, 
                 birth_day: date, phone: str, id: int, group: int,
                 group_leader: str, specialty_code: str):
        super().__init__(self, name, surname, patronymic, birth_day, phone)
        self.id = id
        self.group = group
        self.group_leader = group_leader
        self.specialty_code = specialty_code
