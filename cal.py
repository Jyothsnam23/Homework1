i = int(input('Enter 1 - Addition \n Enter 2 - Subtraction \n Enter 3 - Multiplication \n Enter 4 - Division \n Enter 5 - Average \n'))
num1,num2 = [(int(num1) for num1 in input('Enter two values: ').split())]
if i==1:
    ans = num1 + num2
    if ans <= -1:
        print('Negative')
    else :
        print(ans)
    elif i==2:
        ans = num1 - num2
        if ans <= -1:
            print('Negative')
        else:
            print(ans)
        elif i==3:
            ans = num1 * num2
            if ans <=-1
            print('Negative')
            else:
                print(ans)
                elif i==4:
                ans = num1 / num2
                if ans <= -1
                print('Negative')
                else:
                    print(ans)
                    elif i==5:
                    first,second = [int(first) for first in input('enter two more values:').split()]
                    ans = num1+num2+first+second
                    ans = ans/4
                    if ans<0:
                        print('Negative')
                    else:
                        print(ans)