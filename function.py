#what is a function and how we are gona definig a function , what are the parameter and arrgument

def tarun(gender):
    # defining a function
    # here gender is the parameter

    print("tarun is a bad",gender) 

#  calling a function
# here boy , girl , guy,student are the arrgument 

tarun("boy")
tarun("girl")
tarun("guy")
tarun("student")

#  using for loop calling a function and printing it using a list
names=["tarun","vaihu","sejl","tanu","tarun","vaihu","sejl","tanu","tarun","vaihu","sejl","tanu","tarun","vaihu","sejl","tanu","tarun","vaihu","sejl","tanu","tarun","vaihu","sejl","tanu","tarun","vaihu","sejl","tanu"]
for gender in names:
        tarun(gender)


# defining two parameters in one function
def vaishu(abc , xyz): #--->  here abc is first parameter and xyz is the second parameter. 
    print("my name is",abc,"and my age is",xyz)

# calling the two parameters using for loop in list
name=["Tarun","vaishu","sejl","tanu","vaishnavi"]
for abc in name:
    vaishu(abc ,18)

# how we will know about the key:

def hello(*,name,age):
    print("My name is",name,"and my age is",age)
# creating a list for names:-
names=["taun","vaishu","sejl","tanu"]
#  running a for loop for i in names:-
for i in names:
    hello(name=i,age=40)
    