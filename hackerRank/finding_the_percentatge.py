# ALDO FUSTER TURPIN

def getAverageFrom(student_name, marks):
    student_marks = marks[student_name]
    total = 0
    
    for v in student_marks:
        total += v
    return total / len(student_marks)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    result = getAverageFrom(query_name, student_marks)
    result_formated = "{:.2f}".format(result)
    print(result_formated)
