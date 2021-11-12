# ALDO FUSTER TURPIN    

def get_second_lowest_score(students_info):
    scores = set()
    for student_info in students_info:
        student_score = student_info[1]
        scores.add(student_score)
    my_list = sorted(scores)
    
    if len (my_list) > 1:
        return my_list[1]
    return my_list[0]

def get_names_with(target_score, students_info):
    names = []
    for student_info in students_info:
        student_score = student_info[1]
        if student_score == target_score:
            student_name = student_info[0]
            names.append(student_name)
    return names

def get_names_of_second_lowest_score(students_info):
    second_lowest_score = get_second_lowest_score(students_info)
    names = get_names_with(second_lowest_score, students_info)
    return sorted(names)
    

if __name__ == '__main__':
    students_info = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_info.append([name, score])
        
    names = get_names_of_second_lowest_score(students_info)
    for name in names:
        print(name)
    

        
