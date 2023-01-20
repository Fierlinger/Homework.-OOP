class Student:
    CLASSMETA = 'META'

    def __init__(self, name, surname, second_name, mid_score):
        self.name = name
        self.surname = surname
        self.second_name = second_name
        self.mid_score = mid_score

    def __repr__(self) -> str:
        return "{" + f"""
    name: {self.name}, 
    surname: {self.surname}, 
    second_name: {self.second_name}, 
    mid_score: {self.mid_score}, 
    grant: {self.grant}, 
    _class_meta: {self.CLASSMETA}
""" + "}"
