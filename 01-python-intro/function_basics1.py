#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())  # 5


#2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) # 5 - wrong, it was an error because the number_of_days... variable was undefined


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) # 10 - wrong it was 5, the 10 isn't a part of the function


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) # 5 


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x) # none


#6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3)) # will have an error

#7
def concatenate(b,c):
    return str(b)+str(c)
    print(concatenate(2,5)) #won't print anything with these indentation 

#8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents()) # will error becuase of indentation 

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # 7, 14, 7 - wrong it was 7,14,21 because i think it returned 14 on top of returning 7 (7+14)

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) # 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b) # 500, 300, 500, 300, 500 - wrong, it was 500, 500, 300, 500 because it didn't print b when defining the function, only when it was called

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b) # 500, 300, 300, 300 - wrong, it was 500,500,300,500 becuase the function doesn't print "b" unless it's called, and becuase it doesn't update the value of b? 

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b) # 500, 500, 300, 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo() # 1, 3, 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y) #10- wrong, it's 1,3,5,10 becuase when foo() gets called bar() gets called within it




















