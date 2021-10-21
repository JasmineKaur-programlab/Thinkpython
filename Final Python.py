#!/usr/bin/env python
# coding: utf-8

# In[1]:


0.1+0.2-0.3


# In[2]:


mystring ='abcdefghijk'


# In[3]:


mystring[::2]


# In[4]:


mystring[2:7:2] #important indexing ,step size


# In[5]:


mystring[::-1]


# In[6]:


#immutability


# In[7]:


name ="Sam"


# In[8]:


name[0]="P"


# In[493]:


name[1]


# In[494]:


name[1:]


# In[495]:


name[1:2]


# In[496]:


name[:2]


# In[497]:


name[:]


# In[498]:


my_string="abcdefggghhh"


# In[499]:


my_string[2:3:4]


# In[500]:


last_letters=name[1:]


# In[501]:


last_letters


# In[502]:


'P'+last_letters


# In[503]:


x='Hello World'


# In[504]:


x+"It is beautiful outside!"


# In[505]:


x


# In[506]:


x=x+"It is beautiful outside"


# In[507]:


x


# In[508]:


x


# In[509]:


letter ='z'


# In[510]:


letter*10


# In[511]:


2+3


# In[512]:


'2'+'3'


# In[513]:


x='Hello World'


# In[514]:


x.capitalize()


# In[515]:


x.upper()


# In[516]:


x


# In[517]:


x.lower()


# In[518]:


x.split()


# In[519]:


x = 'Hi this is a string'


# In[520]:


x.split()


# In[521]:


x.split('i')


# In[522]:


print('My name is jasmine {}'.format('INSERT'))


# In[523]:


print('The {} {} {}'.format('fox','brown','quick'))


# In[524]:


print('The {2} {1} {0}'.format('fox','brown','quick'))


# In[525]:


print('The {0} {0} {0}'.format('fox','brown','quick'))


# In[526]:


print('The {f} {b} {f}'.format(f='fox',b='brown',q='quick'))


# In[ ]:


#float formatting-sets the value,width and precision of a floating point number


# In[527]:


result =100/777


# In[ ]:


result


# In[ ]:


print("The result was {r:1.3f}".format(r=result))


# In[531]:


print("The result was {r:1.2f}".format(r=result))


# In[532]:


name = "Jose"


# In[533]:


print('Hello,his name is {}'.format(name))


# In[534]:


print(f'Hello,his name is {name}')


# In[529]:


name ="Sam"
age = 3


# In[530]:


print(f'{name} is {age} years old.')


# In[ ]:


#lists


# In[535]:


my_list=[5,7,8]


# In[536]:


my_list=['STRING',100,23.2]


# In[537]:


len(my_list)


# In[538]:


my_list=['one','two','three']


# In[539]:


my_list[0]


# In[540]:


my_list[1:]


# In[541]:


my_list


# In[557]:


another_list=['four','five']


# In[558]:


new_list=my_list + another_list


# In[559]:


new_list


# In[545]:


my_list


# In[546]:


another_list


# In[560]:


new_list


# In[561]:


new_list[0]='ONE ALL CAPS'


# In[562]:


new_list


# In[563]:


new_list.append('six')


# In[564]:


new_list


# In[565]:


new_list.append('seven')


# In[566]:


new_list


# In[567]:


new_list.pop()


# In[568]:


new_list


# In[569]:


popped_item=new_list.pop()


# In[570]:


popped_item


# In[571]:


new_list


# In[572]:


new_list.pop()


# In[573]:


new_list


# In[574]:


new_list.pop(-1)


# In[575]:


new_list


# In[576]:


new_list.pop(0)


# In[577]:


new_list


# In[578]:


new_list


# In[579]:


new_list


# In[580]:


new_list = ['a','e','x','b','c']


# In[581]:


num_list=[4,1,8,3]


# In[582]:


new_list.sort()


# In[583]:


new_list


# In[584]:


my_sorted_list=new_list.sort() #does not work #cant reassign to something else


# In[585]:


type(my_sorted_list)


# In[586]:


None


# In[ ]:


#it doesnt return anything


# In[587]:


new_list.sort()
my_sorted_list=new_list


# In[588]:


my_sorted_list


# In[589]:


num_list


# In[590]:


num_list.sort()


# In[591]:


num_list


# In[592]:


num_list.reverse()


# In[593]:


num_list


# In[ ]:


# How do I index a nested list? For example if I want to grab 2 from [1,1,[1,2]]?

#You would just add another set of brackets for indexing the nested list, for example: my_list[2][1]


# In[ ]:


#dictionaries


# In[ ]:


#unordered mappings without knowing index position


# In[ ]:


#use dictionary when objects are retrieved by key name
#use list when objects are retrieved by location and indexed or sliced


# In[ ]:


#when grabbing something quickly use dictionary


# In[594]:


my_dict={'key1':'value1','key2':'value2'}


# In[595]:


my_dict


# In[596]:


my_dict['key1']


# In[597]:


my_dict['key1']


# In[598]:


prices_lookup={'apple':2.99,'oranges':1.99,'milk':5.80}


# In[599]:


prices_lookup['apple']


# In[ ]:


#dictionaries can hold other dictionaries


# In[600]:


d ={'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}


# In[601]:


d['k2']


# In[602]:


d['k3']


# In[603]:


d['k3']['insideKey']


# In[604]:


d={'key1':['a','b','c']}


# In[605]:


d


# In[606]:


my_list = d['key1']


# In[607]:


my_list


# In[608]:


letter = my_list[2]


# In[609]:


letter


# In[610]:


letter.upper()


# In[611]:


d


# In[612]:


d['key1'][2].upper()


# In[613]:


d = {'k1':100,'k2':200}


# In[614]:


d


# In[615]:


d['k3']=300


# In[14]:


d


# In[616]:


d['k1']='NEW VALUE'


# In[617]:


d


# In[618]:


d={'k1':100,'k2':200,'k3':300}


# In[619]:


d.keys()


# In[621]:


d.values()


# In[620]:


d.items()


# In[21]:


#Do dictionaries keep an order? How do I print the values of the dictionary in order?

#Dictionaries are mappings and do not retain order!


# In[22]:


#dictionaries are mutable


# In[23]:


#lists are mutable


# In[24]:


#tuples -immutability
#similar to lists


# In[25]:


t=(1,2,3)


# In[26]:


my_list=[1,2,3]


# In[27]:


type(t)


# In[28]:


type(my_list)


# In[29]:


len(t)


# In[30]:


t


# In[31]:


t =('one',2)


# In[32]:


t[0]


# In[33]:


t[-1]


# In[34]:


t=('a','a','b')


# In[35]:


t.count('a')


# In[36]:


t.index('a')


# In[37]:


t.index('b')


# In[38]:


t


# In[39]:


my_list


# In[40]:


my_list[0]='NEW'


# In[41]:


my_list


# In[42]:


t[0]='NEW'


# In[ ]:


#Sets are unordered collections of unique elements


# In[228]:


myset = set()


# In[229]:


myset


# In[230]:


myset.add(1)


# In[231]:


myset


# In[232]:


myset.add(2)


# In[233]:


myset


# In[234]:


mylist = [1,1,1,1,1,2,2,2,3,3,3,3]


# In[235]:


set(mylist)


# In[236]:


True


# In[237]:


true


# In[622]:


False


# In[623]:


type(False)


# In[624]:


1 > 2


# In[625]:


1 == 1


# In[626]:


b = None


# In[627]:


b


# In[628]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'Hello this is a text file\nthis is the second line\nthis is the third line')


# In[629]:


myfile = open('myfile.txt')


# In[630]:


myfile = open('whoops_wrong.txt')


# In[879]:


pwd


# In[880]:


my_file = open('myfile.txt')


# In[881]:


my_file.read()


# In[882]:


my_file.read()


# In[883]:


myfile.seek(0)


# In[884]:


myfile.read()


# In[885]:


myfile.read()


# In[886]:


myfile.seek(0)


# In[887]:


contents = myfile.read()


# In[888]:


contents


# In[889]:


myfile.seek(0)


# In[890]:


myfile.readlines()


# In[891]:


pwd


# In[892]:


myfile.close()


# In[893]:


with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()


# In[894]:


with open('myfile.txt',mode='w') as my_file:
    contents = myfile.read()


# In[895]:


with open('myfile.txt',mode='a') as myfile:
    contents = myfile.read()


# In[896]:


get_ipython().run_cell_magic('writefile', 'my_new_file.txt', 'ONE ON FIRST\nTWO ON SECOND\nTHREE ON THIRD')


# In[897]:


with open('my_new_file.txt',mode='r') as f:
    print(f.read())


# In[898]:


with open('my_new_file.txt',mode='a')as f:
    f.write('FOUR ON FOURTH')


# In[899]:


with open('my_new_file.txt',mode='r') as f:
    print(f.read())


# In[900]:


with open('dhfjdkshfjdks.txt',mode='w')as f:
    f.write('I CREATED THIS FILE!')


# In[ ]:


#so w created that file for us, r and a would have given us error


# In[901]:


with open('dhfjdkshfjdks.txt',mode='r')as f:
    print(f.read())


# In[902]:


2 == 2


# In[903]:


2 == 1


# In[904]:


'hello'=='bye'


# In[905]:


'Bye'=='bye'


# In[906]:


'2'== 2


# In[907]:


2.0 == 2


# In[908]:


3 !=3


# In[909]:


4!=5


# In[910]:


2>1


# In[912]:


1>2


# In[913]:


1<2


# In[914]:


2<5


# In[915]:


2 >= 2


# In[916]:


4 <= 1


# In[917]:


1 < 2


# In[918]:


2 < 3


# In[919]:


1 < 2


# In[635]:


1 < 2 > 3


# In[636]:


1 < 2 and 2 < 3


# In[637]:


1 < 2 < 3


# In[638]:


('h' == 'h') and (2 == 2)


# In[639]:


1 == 1 or 2 == 2


# In[640]:


100 == 1 or 2 ==200


# In[641]:


100 == 1 or 2 == 2


# In[642]:


1 == 1


# In[643]:


not(1==1)


# In[644]:


400 > 5000


# In[645]:


not 400>5000


# In[646]:


1!=1


# In[647]:


if True:
    print('ITS TRUE!')


# In[648]:


hungry = True
if hungry==True:
    print('FEED ME!')
else:
    print('Iam not hungry')


# In[649]:


loc = 'Bank'
if loc =='Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool')
elif loc == 'Store':
    print("Welcome to the store!")
else:
    print('I do not know much')


# In[650]:


name ="Sammy"
if name == 'Frankie':
    print("Hello Frankie")
elif name =='Sammy':
    print('Hello Sammy')
else:
    print("What is your name?")


# In[651]:


my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)


# In[652]:


my_list = [1,2,3,4,5,6,7,8,9,10]


# In[653]:


list_sum = 0

for num in my_list:
    list_sum = list_sum + num
    
print(list_sum)


# In[654]:


mystring = "Hello World"

for letter in "Hello World":
    print(letter)
    
for _ in "Hello World":
    print("cool!")


# In[655]:


tup = (1,2,3)

for item in tup:
    print(item)


# In[656]:


mylist = [(1,2),(3,4),(5,6),(7,8)]


# In[657]:


len(mylist)


# In[658]:


for item in mylist:
    print(item) #tuple unpacking


# In[659]:


for (a,b) in mylist:
    print(a)
    print(b)


# In[660]:


for (a,b) in mylist:
    print(b)


# In[661]:


mylist =[(1,2,3),(5,6,7),(8,9,10)]


# In[662]:


for a,b,c in mylist:
    print(b)


# In[663]:


d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item)


# In[664]:


d = {'k1':1,'k2':2,'k3':3}

for key,value in d.items():
    print(value)


# In[665]:


d = {'k1':1,'k2':2,'k3':3}

for value in d.values():
    print(value)


# In[666]:


#here it is in order but it can be unordered


# In[667]:


x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x=x+1


# In[668]:


x = 0

while x < 5:
    print(f'The current value of x is {x}')
    
    x+=1
else:
    print('X is not less than 5')


# In[669]:


X = 50

while x<5:
    print(f'The current value of x is {x}')
    
    x+=1
else:
    print("X is not less than 5")


# In[670]:


x = [1,2,3]

for item in x:
    
    pass
print('end of my script')


# In[671]:


mystring = 'Sammy'


# In[672]:


for letter in mystring:
    if letter == 'a':
        continue
    print(letter)


# In[673]:


for letter in mystring:
    if letter == 'a':
        break
    print(letter)


# In[674]:


x = 0

while x<5:
    if x == 2:
        break
    print(x)
    x+=1


# In[675]:


mylist = [1,2,3]


# In[676]:


for num in range(10):
    print(num)


# In[677]:


#specify index position


# In[678]:


for num in range(0,10,2):
    print(num)


# In[679]:


for num in range(3,10):
    print(num)


# In[680]:


for num in range(0,11,2):
    print(num)


# In[681]:


range(0,11,2)


# In[682]:


list(range(0,11,2))


# In[683]:


index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count+=1


# In[684]:


index_count = 0
word = 'abcde'

for letter in word:
    
    print(word[index_count])
    index_count += 1


# In[685]:


word ='abcde'

for item in enumerate(word):
    print(item)


# In[686]:


word ='abcde'

for item in enumerate(word):
    print(item)


# In[687]:


word= 'abcde'

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')


# In[688]:


mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c']


# In[689]:


zip(mylist1,mylist2)


# In[690]:


for item in zip(mylist1,mylist2):
    print(item)


# In[691]:


mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)


# In[692]:


#what if lists are uneven


# In[693]:


mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]


# In[694]:


for item in zip(mylist1,mylist2,mylist3):
    print(item)


# In[695]:


#zip the elements till the shortest


# In[696]:


list(zip(mylist1,mylist2))


# In[697]:


'x' in [1,2,3]


# In[698]:


'x' in ['x','y','z']


# In[699]:


'a' in 'a world'


# In[700]:


'mykey' in {'mykey':345}


# In[701]:


d = {'mykey':345}
345 in d.values()


# In[702]:


345 in d.keys()


# In[703]:


mylist = [10,20,30,40,100]


# In[704]:


min(mylist)


# In[705]:


max(mylist)


# In[706]:


from random import shuffle


# In[707]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[708]:


shuffle(mylist)


# In[709]:


mylist


# In[710]:


random_list = shuffle(mylist)


# In[711]:


random_list


# In[712]:


type(random_list)


# In[713]:


mylist


# In[714]:


from random import randint


# In[715]:


randint(0,100)  #grab a random integer (lower to upper)


# In[716]:


randint(0,100)


# In[717]:


mynum = randint(0,10)


# In[718]:


mynum


# In[719]:


input('Enter a number here')


# In[720]:


result = input('What is your name?')


# In[721]:


result


# In[722]:


type(result)


# In[723]:


result1 = input('number')


# In[724]:


type(result1)


# In[725]:


float(result1)


# In[726]:


int(result1)


# In[727]:


#list comprehensions


# In[728]:


mystring = 'hello'


# In[729]:


mylist=[]
for letter in mystring:
    mylist.append(letter)


# In[730]:


mylist


# In[731]:


mylist=[letter for letter in mystring]


# In[732]:


mylist


# In[733]:


mylist = [x for x in 'word']


# In[734]:


mylist


# In[735]:


mylist = [qweqwe for qweqwe in 'wordtwo']


# In[736]:


mylist


# In[737]:


mylist = [x for x in range(0,11)]


# In[738]:


mylist = [num for num in range(0,11)]


# In[739]:


mylist


# In[740]:


mylist = [num**2 for num in range(0,11)] #dont use list comprehensions


# In[741]:


mylist


# In[742]:


mylist = [x for x in range(0,11) if x%2==0]


# In[743]:


mylist


# In[744]:


celcius =[0,10,20,34.5]


# In[745]:


fahrenheit = [((9/5)*temp + 32)for temp in celcius]


# In[746]:


fahrenheit


# In[747]:


fahrenheit = []

for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))


# In[748]:


fahrenheit


# In[749]:


results = [x if x%2==0 else 'ODD'for x in range(0,11) ]


# In[750]:


results


# In[751]:


mylist = []


# In[752]:


for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)


# In[753]:


mylist


# In[754]:


mylist = []

for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)


# In[755]:


mylist


# In[756]:


st = 'Print only words that start with s in this sentence'


# In[757]:


st


# In[758]:


st.split()


# In[759]:


for word in st.split():
    print(word)


# In[760]:


for word in st.split():
    if word[0] == 's':
        print(word)


# In[761]:


st = 'Sam Print only the words that start with s in this sentence'


# In[762]:


for word in st.split():
    if word[0] =='s' :
        print(word)
        


# In[763]:


#to print even numbers range
list(range(0,11,2))


# In[764]:


for num in range(0,11,2):
    print(num)


# In[765]:


#list comprehensions to create a list of all numbers between 1 and 50
#code in this cell divisible by 3
[x for x in range(1,51) if x%3 == 0]


# In[766]:


st = 'Print every number in this sentence that has even number of letters'


# In[767]:


for word in st.split():
    if len(word)%2 == 0:
        print(word+ 'is even!')


# In[768]:


#write a program that prints the integers from 1 to 100.Multiples of three print"Fizz" insteas of the number, and for the multiples of five print"Buzz". 


# In[769]:


for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print('Fizzbuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)
        


# In[770]:


st = 'Create a list of the first letters of every word in this string'


# In[771]:


[word for word in st.split()]


# In[772]:


[word[0]for word in st.split()]


# In[773]:


mylist = [1,2,3]


# In[774]:


mylist.append(4)


# In[775]:


mylist


# In[776]:


mylist.pop()


# In[777]:


mylist


# In[778]:


help(mylist.insert)


# In[779]:


#functions


# In[780]:


def name_of_function():
    print("Hello")


# In[781]:


def name_of_function(name):
    "Docstring explains function"
    print("Hello"+name)


# In[782]:


name_of_function("Jose")


# In[783]:


def add_function(num1,num2):
    return num1+num2

#return allows to save it to a variable


# In[784]:


result = add_function(1,2)


# In[785]:


print(result)


# In[786]:


def say_hello():
    print("hello")
    print("are")
    print("you")


# In[787]:


say_hello()


# In[788]:


say_hello


# In[789]:


def say_hello(name):
    print(f'Hello {name}')


# In[790]:


say_hello('Jose')


# In[791]:


def say_hello(name='Default'):
    print(f'Hello {name}')


# In[792]:


say_hello('Jose')


# In[793]:


def add_num(num1,num2):
    return num1+num2


# In[794]:


result=add_num(10,20)


# In[795]:


result


# In[796]:


def print_result(a,b):
    print(a+b)


# In[797]:


def return_result(a,b):
    return a+b


# In[798]:


result=print_result(10,20)


# In[799]:


result


# In[800]:


type(result) #not get anything back because type is nonetype


# In[801]:


result=return_result(10,20)


# In[802]:


result


# In[803]:


#you need return to grab the result


# In[804]:


def myfunc(a,b):
    print(a+b)
    return a+b


# In[805]:


result = myfunc(10,20)


# In[806]:


result


# In[807]:


def sum_numbers(num1,num2):
    return num1+num2


# In[808]:


sum_numbers(10,20)


# In[809]:


sum_numbers('10','20')


# In[810]:


2 % 2


# In[811]:


3 % 2


# In[812]:


41 % 40


# In[813]:


20 % 2


# In[814]:


20 % 2 == 0


# In[815]:


21 % 2 == 0


# In[816]:


def even_check(number):
    result=number % 2 == 0
    return result


# In[817]:


even_check(20)


# In[818]:


even_check(21)


# In[819]:


def even_check(number):
    return number % 2 ==0


# In[820]:


even_check(88)


# In[821]:


#RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST


# In[822]:


def check_even_list(num_list):
    
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
        


# In[823]:


check_even_list([1,3,5])


# In[824]:


check_even_list([2,4,5])


# In[825]:


check_even_list([2,1,1,1])


# In[826]:


check_even_list([1,1,1,2])


# In[827]:


def check_even_list(num_list):
    
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            return False #wrong
        


# In[828]:


check_even_list([9,6,9])


# In[829]:


def check_even_list(num_list):
    
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False

#here second return is outside


# In[830]:


check_even_list([1,2,5])


# In[831]:


check_even_list([1,3,5])


# In[832]:


#return all even numbers in a list
def check_even_list(num_list):
    even_numbers = []
    
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
            
        else:
            pass
            
    return even_numbers
    


# In[833]:


check_even_list([1,2,3,4,5])


# In[834]:


check_even_list([1,3,5])


# In[835]:


stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]


# In[836]:


for item in stock_prices:
    print(item)


# In[837]:


for ticker,price in stock_prices:
    print(price+(0.1*price))


# In[920]:


work_hours = [('Abby',100),('Billy',400),('Cassie',800)]


# In[921]:


#find out employee of the month
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    #return
    return(employee_of_month,current_max)


# In[922]:


employee_check(work_hours)


# In[923]:


work_hours = [('Abby',100),('Billy',4000),('Cassie',800)]


# In[924]:


employee_check(work_hours)


# In[925]:


result = employee_check(work_hours)


# In[926]:


result


# In[927]:


name


# In[928]:


name,hours=employee_check(work_hours) #tuple un


# In[929]:


name


# In[930]:


hours


# In[931]:


example = [1,2,3,4,5,6,7]


# In[850]:


from random import shuffle


# In[851]:


shuffle(example)


# In[852]:


example


# In[853]:


#shuffle does not return anything it just shuffles the objects


# In[854]:


result = shuffle(example)


# In[855]:


result


# In[856]:


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# In[857]:


result = shuffle_list(example)


# In[858]:


result


# In[859]:


#lets create a game of three lists and find out when we shuffle them what we come accross


# In[860]:


mylist = ['','O','']


# In[861]:


shuffle_list(mylist)


# In[862]:


#find where is O , it is not in same spot


# In[863]:


def player_guess():
    
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number : 0,1, or 2")
    
    return int(guess)


# In[864]:


player_guess()


# In[865]:


myindex = player_guess()


# In[866]:


myindex


# In[867]:


def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)


# In[868]:


#steps
#initial list
#shuffle list
#user guess
#check guess


# In[869]:


#initial list
my_list = ['','O','']
#shuffle list
mixedup_list = shuffle_list(mylist)
#user guess
guess = player_guess()
#check_guess
check_guess(mixedup_list,guess)


# In[870]:


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# In[871]:


def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)


# In[872]:


#initial list
my_list = ['','O','']
#shuffle list
mixedup_list = shuffle_list(mylist)
#user guess
guess = player_guess()
#check_guess
check_guess(mixedup_list,guess)


# In[873]:


def myfunc(a,b,c=0,d=0,e=0):
    #Returns 5% of the sum of a and b
    return sum((a,b,c,d)) * 0.05


# In[874]:


myfunc(40,60)


# In[875]:


def myfunc(a,b,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*0.05
    


# In[876]:


myfunc(40,60,100,100,3,4)


# In[ ]:


#it lets us take only arbitrary set of arguments


# In[877]:


def myfunc(*args):
    return sum(args)*0.05


# In[878]:


myfunc(4,5,60,70)


# In[932]:


def myfunc(*args):
    for item in args:
        print(item)


# In[933]:


myfunc(40,60,100,1,34)


# In[935]:


def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


# In[937]:


myfunc(fruit='apple',veggie='lettuce')


# In[938]:


def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


# In[939]:


myfunc(fruit='apple',veggie='lettuce')


# In[940]:


def myfunc(**kwargs):
    print(kwargs)


# In[944]:


def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {}{}'.format(args[0],kwargs['food']))


# In[948]:


myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')


# In[952]:


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        #one or both numbers are odd!
        if a>b:
            result = a
        else:
            result = b
    return result


# In[953]:


lesser_of_two_evens(2,4)


# In[954]:


lesser_of_two_evens(2,5)


# In[955]:


min(10,20)


# In[956]:


max(10,20)


# In[958]:


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        result = min(a,b)
    else:
        result = max(a,b)
    return result


# In[959]:


lesser_of_two_evens(2,4)


# In[961]:


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
    
    


# In[962]:


lesser_of_two_evens(5,6)


# In[965]:


def animal_crackers(text):
    wordlist = text.split()
    
    first = wordlist[0]
    second =wordlist[1]
    
    return first[0] == second[0]


# In[966]:


animal_crackers('Levelheaded Llama')


# In[967]:


animal_crackers('Crazy Kangaroo')


# In[968]:


animal_crackers('Crazy cat')


# In[970]:


def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)
    
    return wordlist[0][0]==wordlist[1][0]


# In[971]:


animal_crackers('Levelheaded Llama')


# In[972]:


animal_crackers('Crazy cat')


# In[974]:


#true if n1 20, sum = 20, n2 = 20
def makes_twenty(n1,n2):
    if n1+n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False


# In[977]:


makes_twenty(10,10)


# In[978]:


makes_twenty(2,3)


# In[979]:


def makes_twenty(n1,n2):
    return (n1+n2) == 20 or n1==20 or n2==20


# In[980]:


makes_twenty(10,15)


# In[981]:


#function that capitalizes the first and fourth letters


# In[982]:


def old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    
    return first_letter.upper()+inbetween+fourth_letter.upper()+rest


# In[984]:


old_macdonald('macdonald')


# In[985]:


#second way


# In[987]:


def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    
    return first_half.capitalize()+second_half.capitalize()


# In[988]:


old_macdonald('macdonald')


# In[990]:


def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return reverse_word_list


# In[991]:


#check
master_yoda('I am home')


# In[992]:


mylist=['a','b','c']


# In[993]:


'--'.join(mylist)


# In[995]:


'000000'.join(mylist)


# In[997]:


#given an integer n, return True if n is within 10 of either 100 or 200


# In[999]:


def almost_there(n):
    
    return(abs(100-n)<=10) or (abs(200-n)<=10)


# In[1004]:


#given a list of ints, return True if the array contains a 3 next to a 3 somewhere
def has_33(nums):
    
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1]==3:
            return True
        
    return False


# In[1006]:


has_33([1,3,1,3])


# In[1007]:


#given a string, return a string where for every character in the original there are three characters


# In[1008]:


def paper_doll(text):
    result = ''
    
    for char in text:
        result += char*3
    return result


# In[1009]:


paper_doll('Hello')


# In[1010]:


paper_doll('Mississippi')


# In[1011]:


def blackjack(a,b,c):
    
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])-10 <=31:
        return sum([a,b,c])-10
    else:
        return "BUST"


# In[1012]:


blackjack(5,6,7)


# In[1013]:


blackjack(9,9,9)


# In[1014]:


blackjack(9,9,11)


# In[1]:


def almost_there(n):
    return(abs(100-n)<=10)or(abs(200-n)<=10)


# In[2]:


almost_there(104)


# In[3]:


almost_there(150)


# In[4]:


almost_there(209)


# In[5]:


#return the sum of numbers in the array except ignore sections of numbers starting with a 6 and extending to next 9


# In[5]:


def summer_69(arr):
    total = 0
    add = True
    
    for num in arr:
        while add:
            if num!=6:
                total+=num
                break
            else:
                add = False
        while not add:
            if num!=9:
                break
            else:
                add = True
                break
    return total       
            
            


# In[6]:


#Check
summer_69([1,3,5])


# In[7]:


summer_69([4,5,6,7,8,9])


# In[8]:


summer_69([2,1,6,9,11])


# In[1]:


#function that takes a list of integers and returns True if it contains 007 in order


# In[3]:


def spy_game(nums):
    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)
            
    return len(code) == 1


# In[4]:


spy_game([1,2,4,0,0,7,5])


# In[5]:


spy_game([1,0,2,4,0,5,7])


# In[6]:


spy_game([1,7,2,0,4,5,0])


# In[7]:


#write a function that returns the prime numbers that exist up to and including a given number


# In[12]:


def count_primes(num):
    #Check for 0 or 1 input
    if num < 2:
        return 0
    #############
    # 2 or greater
    #############
    #Store prime numbers
    primes = [2]
    #Counter
    x = 3
    
    #x is going through every number up to input num
    while x <= num:
        #Check if x is prime
        for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


# In[13]:


count_primes(100)


# In[1]:


def print_big(letter):
    patterns = {1:'*',2:''}


# In[2]:


#lambda expressions,map and filter functions


# In[3]:


def square(num):
    return num**2


# In[4]:


my_nums = [1,2,3,4,5]


# In[6]:


for item in map(square,my_nums):
    print(item)


# In[7]:


list(map(square,my_nums))


# In[13]:


def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
    


# In[14]:


names = ['Andy','Eve','Sally']


# In[1]:


def square(num):
    return num**2


# In[2]:


my_nums = [1,2,3,4,5]


# In[5]:


for item in map(square,my_nums):
    print(item)


# In[7]:


def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


# In[8]:


names = ['Andy','Eve','Sally']


# In[10]:


list(map(splicer,names))


# In[11]:


def check_even(num):
    return num%2 == 0


# In[12]:


mynums = [1,2,3,4,5,6]


# In[14]:


filter(check_even,mynums)


# In[15]:


list(filter(check_even,mynums))


# In[16]:


for n in filter(check_even,mynums):
    print(n)


# In[17]:


def square(num):
    result = num ** 2
    return result


# In[18]:


square(3)


# In[19]:


lambda num: num ** 2


# In[20]:


square(5)


# In[21]:


list(map(lambda num:num**2,mynums))


# In[22]:


lambda num:num%2 == 0


# In[23]:


list(filter(lambda num:num%2 == 0,mynums))


# In[24]:


names


# In[26]:


list(map(lambda x:x[::-1],names))


# In[27]:


x = 25

def printer():
    x = 50
    return x


# In[28]:


print(x)


# In[29]:


print(printer())


# In[30]:


#l , #E, #G, #B


# In[31]:


lambda num:num**2


# In[32]:


name = 'THIS IS A GLOBAL STRING'


# In[2]:


def greet():
    name = 'Sammy'
    
    def hello():
        print("Hello"+name)
        
    hello()

greet()


# In[3]:


greet()


# In[4]:


len


# In[1]:


x = 50

def func(x):
    global x
    print(f'X is {x}')
    
    #LOCAL REASSIGNMENT
    x=200
    print(f'I just locally changed X to {x}')


# In[2]:


func(x)


# In[3]:


print(x)


# In[4]:


#object oriented programming


# In[2]:


class NameOfClass():
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2
        
    def some_method(self):
        


# In[6]:


mylist = [1,2,3]


# In[7]:


myset = set()


# In[8]:


type(myset)


# In[9]:


type(mylist)


# In[10]:


class Sample():
    pass


# In[11]:


my_sample = Sample()


# In[12]:


type(my_sample)


# In[7]:


class Dog:
  
    # class attribute
    attr1 = "mammal"
  
    # Instance attribute
    def __init__(self, name):
        self.name = name
  
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
  
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
  
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))


# In[1]:


class Dog:
    
    #class attribute
    attr1 = "mammal"
    
    #instance attribute
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        print("My name is {}".format(self.name))
        
#driver code
#object instantiation
Rodger = Dog("Rodger")
Tommy  = Dog("Tommy")

#Accessing class methods
Rodger.speak()
Tommy.speak()


# In[6]:


#inheritence
class Pearson(object):
    
    #__init__is known as the constructor
    def __init__ (self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        
        
#child class

class Employee(Pearson):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post   = post
        
        #invoking the__init__of the parent class
        Pearson.__init__(self,name,idnumber)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("Idnumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
        
#creation of an object variable or an instance
a = Employee('Rahul',886012,200000,"Intern")

#calling a function using its instance
a.display()
a.details()


# In[4]:


class Bird:
    def intro(self):
        print("There are many types of birds ")
        
    def flight(self):
        print("Most of the birds can fly but some cannot")
        
class sparrow(Bird):
    
    def flight(self):
        print("Sparrows can fly.")
        
class ostrich(Bird):
    
    def flight(self):
        print("Ostriches cannot fly.")
        
obj_bird = Bird()
obj_spr  = sparrow()
obj_ost  = ostrich()

obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()


# In[5]:


class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
  
# Creating a derived class
class Derived(Base):
    def __init__(self):
  
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
  
  
# Driver code
obj1 = Base()
print(obj1.a)


# In[1]:


def add(n1,n2):
    print(n1+n2)


# In[2]:


add(10,20)


# In[3]:


number1 = 10


# In[4]:


number2 = input("Please provide a number:")


# In[5]:


add(number1,number2)
print("Something happened!")


# In[10]:


try:
    
    
    result = 10 + '10'
except:
    print("Hey it looks like you arent adding correctly")
else:
    print("Add went well!")
    print(result)


# In[11]:


result


# In[12]:


try:
    
    
    result = 10 + 10
except:
    print("Hey it looks like you arent adding correctly")
else:
    print("Add went well!")
    print(result)


# In[13]:


result


# In[17]:


try:
    f = open('testfile','w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error")
finally:
    print("I always run")


# In[18]:


try:
    f = open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error")
finally:
    print("I always run")


# In[19]:


try:
    f = open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("All other exceptions")
finally:
    print("I always run")


# In[20]:


try:
    f = open('testfile','w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("All other exceptions")
finally:
    print("I always run")


# In[21]:


def ask_for_int():
    
    while True:
    try:
        result = int(input("Please provide number"))
    except:
        print("Whoops! That is not a number")
        continue
    els
    finally
        print("End of try/except/finally")


# In[1]:


a = 1
b = 2
print(a)
print(b)


# In[2]:


def func():
    return 1


# In[3]:


func()


# In[4]:


func


# In[5]:


def hello():
    return "Hello!"


# In[6]:


hello()


# In[7]:


hello


# In[8]:


greet = hello


# In[9]:


greet()


# In[10]:


hello()


# In[11]:


del hello


# In[12]:


hello()


# In[13]:


greet()


# In[4]:


def hello(name='Jose'):
    print('The hello() function has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t This is welcome() inside hello'
        
    print(greet())
    print(welcome())
    print('This is the end of the hello function!')


# In[5]:


hello()


# In[6]:


def hello(name='Jose'):
    print('The hello() function has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t This is welcome() inside hello'
        
    print("I am going to return a function!!")
    
    if name == 'Jose':
        return greet
    else:
        return welcome


# In[7]:


hello


# In[8]:


my_new_func = hello('Jose')


# In[9]:


print(my_new_func())


# In[10]:


def cool():
    
    def super_cool():
        return 'I am very cool!'
    
    return super_cool


# In[11]:


some_func = cool()


# In[12]:


some_func


# In[13]:


some_func()


# In[14]:


#DEFINING A FUNC INSIDE A FUNC INSTEAD OF BUILDING A FUNCTION


# In[15]:


def hello():
    return 'Hi Jose!'


# In[16]:


def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())


# In[17]:


hello()


# In[18]:


other(hello)


# In[ ]:





# In[ ]:





# In[3]:


#decorator

def new_decorator(original_func):
    
    def wrap_func():
        
        print('Some extra code, before the original function')
        
        original_func()
        
        print('Some extra code, after the original function!')
        
    return wrap_func   


# In[2]:


def func_needs_decorator():
    print("I want to be decorated!!")


# In[4]:


func_needs_decorator()


# In[6]:


new_decorator()


# In[7]:


#generator
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


# In[9]:



for x in create_cubes(10):
    print(x)


# In[10]:


#generators help in saving memory space , lets say we want just that list


# In[11]:


def create_cubes(n):
    
    for x in range(n):
        yield x**3


# In[12]:


for x in create_cubes(10000):
    print(x)


# In[13]:


list(create_cubes(10))


# In[15]:


def gen_fibon(n):
    
    a=1
    b=1
    for i in range(n):
        yield a
        a,b = b, a+b


# In[16]:


for number in gen_fibon(10):
    print(number)


# In[17]:


def gen_fibon(n):
    a = 1
    b = 1
    output = []
    
    for i in range(n):
        output.append(a)
        a,b = b , a+b


# In[18]:


for number in gen_fibon(10):
    print(number)


# In[19]:


def simple_gen():
    for x in range(3):
        yield x


# In[20]:


for number in simple_gen():
    print(number)


# In[21]:


g = simple_gen()


# In[22]:


g


# In[23]:


next(g)


# In[24]:


print(next(g))


# In[25]:


print(next(g))


# In[27]:


s = 'hello'


# In[28]:


for letter in s:
    print(letter)


# In[29]:


next(s)


# In[30]:


s_iter = iter(s)


# In[31]:


next(s_iter)


# In[ ]:


#yield important

