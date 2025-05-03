#9.1
with open('grades.txt', mode='w') as grades:
    grades.write('Suzy 96\n')
    grades.write('Kai 67\n')
    grades.write('Tiffany 100\n')
    grades.write('Joshua 82\n')
#9.2
with open('grades.txt', 'r') as grades:
    print(f'{"Name":<9}{"Grade"}')
    grade_count = 0
    grade_total = 0
    for record in grades:
        name, grade = record.split()
        Grade = int(grade)
        grade_count += 1
        grade_total += Grade
        print(f'{name:<9}{grade}')
    print(f'Total: {grade_total}\nGrade Count: {grade_count}\nGrade Average: {grade_total/grade_count:.2f}')

#9.3
#firstname,lastname,exam1grade,exam2grade,exam3grade
import csv
with open('grades.csv', mode='w', newline='') as grades:
    writer = csv.writer(accounts)
    writer.writerow(['Suzy','Lee',76,87,95])
    writer.writerow(['Kyle','Smith',100,98,99])
