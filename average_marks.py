n = int(input())
students_marks = {}
for i in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float,line[1:]))
    students_marks[name] = marks
    
query_name = input()
marks = students_marks[query_name]
average = sum(marks)/len(marks)
print("{:.2f}".format(average))
