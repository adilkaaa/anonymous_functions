#1
# def my_len(s):
#     count=0
#     for i in s:
#         count+=1
#     return count
# print(my_len(input('word: ')))

#2
# a = {'a':1,'b':2}
# b = {'c':3,'d':4}
# def union_dict(d1,d2):
#     for k,d in d2.items():
#         a[k] = d
#     return d1
# print(union_dict(a,b))

#3
# def order():
#     with open('menu.txt', 'w') as f:
#         meal = input('What do you want to eat: ')
#         drink = input('drink: ')
#         f.write('meal: '+meal+'\n')
#         f.write('drink: '+drink)
#     return 'Zakaz vypolnen!!!'

# print(order())



#4
# word = input('enter file name: ')
# def create_file(name):
#     path = '/home/adil/Desktop/my_projects/month1/day13/slides/'
#     file = path+name+'.txt'
#     with open(file,'w') as f:
#         f.write('')
#     return 'File created'

# print(create_file(word))


#5
# def main():
#     print('Я главная функция')
    
#     def new_func():
#         print('Я вложенная функция')
#     new_func()
# main()


#6

# ex_d = {
#     'a':1,
#     'b':2,
#     'c':3,
#     'd':4
# }

# def split_dict(d):
#     k = tuple(d.keys())
#     v = tuple(d.values())
#     return k,v
# print(split_dict(ex_d))


#7

# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True if n!=1 else False
# print(is_prime(int(input('is number prime: '))))


#8
# n1 = int(input('number1 : '))
# n2 = int(input('number2 : '))
# n3 = int(input('number3 : '))

# print((lambda a,b,c: f'Обьем бассейна {a*b*c}')(n1,n2,n3))


# #9
# days_past = int(input('How many days past after NewYear: '))
# print((lambda x: f'ostalos:{365-x}')(days_past))


#10


# FibArray = [0,1]

# def fibonaci(n):
#    if n <= 0:
#         print("Incorrect input")
#    elif n <= len(FibArray):
#       return FibArray[n - 1]
#    else:
#         temp_fib = fibonaci(n - 1) + fibonaci(n - 2)
#         FibArray.append(temp_fib)
#         return temp_fib
# d = fibonaci(10)
# print(FibArray)



#11
# l = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453] 
# final = map(lambda x: x*1.185,l)
# print(list(final))


















