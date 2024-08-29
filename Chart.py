print('Hello World')


#List

user_list=['Jay','Ronak','Kapil','Janvi','Gopi']
"""
print(user_list)
print(user_list[4])
user_list.append('Hetvi')
print(user_list)
user_list.remove('Kapil')
print(user_list)
user_list[1]='Ronak'
print(user_list)
user_list.insert(1,'Ashka')
print(user_list)
print(len(user_list))
user_list.sort()
print(user_list)
ssssuser_list.sort(reverse=True)
print(user_list)
user_list.reverse()
print(user_list)
"""
#user_list.pop()
#print(user_list.pop())
#remove_value = user_list.pop()
#print(remove_value)
#print(user_list)
#print(user_list[1:4])


'''
Jay = [1,38,45,34,22,10]
print(Jay)
print(min(Jay))
print(max(Jay))
print(sum(Jay))
Jay.sort()
print(Jay)
print(len(user_list))
'''


#Tuple
'''

GG = ('BSDK','Lodu','BSDK','Chodu','BSDK')
print(type(GG))
print(GG)
print(GG[4])
print(GG.count('BSDK'))
print(GG.index('Chodu'))


'''
#Dictionaries

'''
car={'Brand':'Ferrari', 'model':'P1'}
print("Car of Brand" + car['Brand'])
print("Car of model" + car['model'])

print(car.get('Brand'))

car['color']="Red"
print(car)

del car['Brand']
print(car)

print(len(car))

car['brand']="Dodge"
print(car)
'''

#prg1

#list1=[1,2,3,4,5,6]
#list2=[2,3,6,9,8,10]

#set1 = set(list1)
#set2 = set(list2)

#comman_element = set1.intersection(set2)

#print("Comman Element:",comman_element)

'''


#for loop

Marks = {
    
    'hindi' : 50,
    'Eng' : 40,
    'Maths' : 60,
}

for subject , mark in Marks.items():
    print(f'subject is: {subject}')
    print(f'Marks is : {mark}')
for subject in Marks.keys():
    print(f'subject is: {subject}')
for subject in Marks.keys():
    print(f'Marks is: {mark}')



till_num = int(input('Enter the specified Number:'))

my_list=[]

for num in range(1, till_num+1):
    result = ""
    if num % 3 == 0:
        result = result + 'Fizz'
        if num % 5 == 0:
            result = result + 'Buzz'
    elif num % 5 == 0:
        result = result + 'Buzz' 
    else :
        result = num
    (my_list.append(result))

print(my_list)
'''

import matplotlib.pyplot as plt

x = ['english', 'gujjrati', 'maths']
y = [89, 78, 76]

plt.plot(x, y)
plt.xlabel('subject')  # typo: xlable -> xlabel
plt.ylabel('marks')   # typo: ylable -> ylabel
plt.title('marks chart')
plt.show()