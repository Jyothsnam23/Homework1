# Task3-Task4 1
#l= [1,2,"jyothsna",2+3j,3.4]
#print(l)




#2
#    0 1 2 3 4
#   -5-4 -3 -2 -1
#list[start:end:step]
#l = [1,2,3,4,5]
#print(l[1:4])

#3
#x = lambda a,b : a*b or a+b
#y = 10
#z = 5
#print(x(y,z))

# def multiply_list(items):
#     tot = 1
#     for x in items:
#         tot *=x
#     return tot

#print(multiply_list[1,2,3,4,5,6,7])

# list = [1,2,3,4,5,6]
# sum = sum(list)
# print(sum)


#4

# list = [8,9,34,67,98,100,23,46,78,100]
# print("smallest element: ", min(list))
# print("largest element:",max(list))
    
#5
# li = [1,2,3,4,5,6,7,8,9,11,12,13,14]
# for i in li:
#      if (i%2!=0):
#           print(i)
#           li.remove(i)
# else:
#         pass
            
# print(li)    

#6th doubt

# def printValue():
#  l = list()
# for i in range(1,31):
#     print(i**2)
# print(l[:5])
# print(l[:-5])
    
# printValue()  

#7th

# a = [1,2,34,5,6]
# b= [7,8,9,10]
# a.append(b)
# print(a)

#8th



# a = {1:10,2:20} 
# b = {3:30,4:40}
# c = {**a, **b}
# print(c)


    #9th
    
# n = int(input('Input a number'))
#         d = dict()
#     for x in range(1,n+1):
#         d[x]=x*x
#     print(d)

#10th 

# values = input ("Input some coma seperated number")
# list = values.split(",")
# tuple = tuple(list)
# print('list: ', list)
# print('tuple:', tuple)
    
    
    # Task 2 1st.
    
#n = "123abc" [::-1]
# print(n)

#2

# def up_low(s):
#      u = sum (l for i in s if i.isupper())
#      l = sum(l for i in s if i.islower())
#      print("No of upper case characters: %s,No of lower case characater: %s" %(u,l))
  
#3

# def unique_list(l):
#     x = []
#     for i in l:
#         if i not in x:
#            x.append(i)
#     return x 

# print(unique_list([1,1,2,3,3,4,3,4,4,5,6,7])) 

# #4th doubt

# n = input('enter a string : ')
# l = n.split('-')
# l.sort()
# print('-'.join (l))


#5th doubt

# l = []
# while True:
#     l = input()
#     if l:
#         lines.append(l.upper())
#     else: 
#         break
# for l in lines():
#     print(l)


#6th 


# def calculateSum(a,b):
#     s = int(a) + int(b)
#     return s
    
    
# num1 = "10"
# num2 = "20"

# sum = calculateSum(num1,num2)

# print ("Sum = ", sum)

#7th doubt

def max_len_str(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1>len2:
        print(s1)
    elif len2>len1:
        print(s2)
    else :
        print(s1)        
        print(s2)

max_len_str("jyothsna", "niri")


#8th
# sqr_t = ()
# for i in range(1,21):
#     sqr_t.apend(i*i)
    
# print(*sqr_t)
 
                

     
    
    
    
    

    
     
            