#print('Hello World')

#Enter the marks of the students
Marks = int(input("Enter your Marks:"))

if Marks >=90:
    print('You have scored: A')
elif Marks <=90 and Marks >= 80:
    print('You have scored: B')
elif Marks <=80 and Marks >= 70:
    print('You have scored: C')
else:
    print('You are failed')