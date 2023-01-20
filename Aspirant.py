from .meta.Student import Student

class Aspirant(Student):
    CLASSMETA = 'ASPIRANT'

    def __init__(self, name, surname, second_name, mid_score) -> None:
        super().__init__(name, surname, second_name, mid_score)
        self.update_grant()

    def update_mid_score(self, mid_score):
        self.mid_score = mid_score
        
    def update_grant(self):
        mid_score = self.mid_score
        if mid_score == 5:
            self.grant = 5000
        elif 4 < mid_score < 5:
            self.grant = 4500
        elif 3 < mid_score < 4:
            self.grant = 3500
        else:
            raise NotImplementedError

