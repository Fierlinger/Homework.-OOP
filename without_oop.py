from scholarship_data import DATA


def bachelor(full_name, group_number, mid_score):
    return mid_score, 'bachelor'

def postgraduate(full_name, group_number, mid_score):
    return mid_score, 'postgraduate'


def get_scholarship_for_student(student_information): 
    mid_score = student_information[0]
    degree = student_information[1]
    if degree == 'bachelor':
        for item in DATA:
            if mid_score == item['max_mark']: 
                return item['scholarship_bachelor']
            if item['min_mark'] < mid_score < item['max_mark']: 
                return item['scholarship_bachelor']
            if item['min_mark'] < mid_score <= item['max_mark']: 
                return item['scholarship_bachelor']
    
    else: 
        for item in DATA:
            if mid_score == item['max_mark']: 
                return item['scholarship_postgraduate']
            if item['min_mark'] < mid_score < item['max_mark']: 
                return item['scholarship_postgraduate']
            if item['min_mark'] < mid_score <= item['max_mark']: 
                return item['scholarship_postgraduate']
    return 'student without scholarship'
