DATA = [
    {
        'maximum_range': 5,
        'minimum_range': 5,
        'scholarship_amount_student': 3000,
        'scholarship_amount_graduate_student': 5000
    },
    {
        'maximum_range': 5,
        'minimum_range': 4,
        'scholarship_amount_student': 2000,
        'scholarship_amount_graduate_student': 4500
    },
    {
        'maximum_range': 4,
        'minimum_range': 3,
        'scholarship_amount_student': 1500,
        'scholarship_amount_graduate_student': 3500
    },
]


def student(full_name, group_number, average_rating):
    return average_rating, 'student'

def graduate_student(full_name, group_number, average_rating):
    return average_rating, 'graduate_student'

def get_scholarship_amount(student_info):
    average_rating = student_info[0]
    degree = student_info[1]
    for info in DATA:
        # if info['maximum_range'] >= average_rating >= info['minimum_range']:
        if info['minimum_range'] <= average_rating <= info['maximum_range']:
            if degree == 'student':
                return info['scholarship_amount_student']
            else:
                return info['scholarship_amount_graduate_student']
        else:
            raise NotImplementedError
