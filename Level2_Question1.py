# Write a program to accept a student’s name and scores in three subject. 
# Display the 1st, 2nd, average and total. 
# Display whether the student has secured 1st , 2nd , pass class or has failed.
# 1st class is for a score of 60 and above, 2nd class is for a score of 50 and above,
# while pass class is for a score of 35 and above. 
# If the score is less than 35, then the student fails.

name = input('Enter the student name:')

sub = []
for _ in range(3):
    marks = int(input('Enter Marks'))
    sub.append(marks)

for i in range(3):
    if sub[i] < 35:
        print('subject', i+1, 'is failed')
    elif sub[i] >= 50 and sub[i] < 60:
        print('subject',i+1 , ' is passed in second class')
    elif sub[i] >= 35 and sub[i] < 50:
        print('Subject',i+1,  'is passed')
    elif sub[i] >= 60:
        print('subject',i+1, 'is passed in first class')


total = sum(sub)
print('Total Marks', total)
print('Average Marks', round(total/3, 2))
