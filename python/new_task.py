grades = []

for i in range(4):
    x = int(input())
    grades.append(x)


avg = sum(grades)/len(grades)

if avg >= 4:
    print('Результат: отлично')
    
elif 3 <= avg <= 4:
    print('Результат: хорошо')
    
    
else:
    print('Результат тап')
    
