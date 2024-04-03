array = [69, 420, 73, 42]


def func_one(y):
    print(y)


# Question 1 Remove the comment from the line beneath this one and run this code. What will the line below output/print?
# func_one(array)

# Question 2 Remove the comment from the line beneath this one and run this code. What will the line below output/print?
# func_one(10)

# Question 3 Remove the comment from the line beneath this one and run this code. What will the line below output/print?
# print(func_one(array))

# Question 4 Remove the comment from the line beneath this one and run this code. What will the line below output/print?
# print(func_one)
# Question 5, what is the thing that was printed by print(func_one) in the line above? Answer: It was the memory address of the function object. https://stackoverflow.com/questions/32083871/what-does-everything-mean-when-someone-says-everything-in-python-is-an-object

# Question 6, what will func_two print and why? https://medium.com/@daniel.tooke/variables-and-memory-addresses-in-python-6d96d672ed3d
def func_two():
    x = [1, 2, 3]
    y = [1, 2, 3]
    print(x == y)
    print(x is y)
# func_two()


# Question 7 Remove the comment from the line beneath this one and run this code. What will the line below output/print? I'm not asking what func_two will print. Only what the line below this one will print. The line beneath this one will only print one line. func_two will print two lines because of its two print statements but this question isn't asking about those two print statements, only this one.
# print("This is me printing func_two()", func_two())

# Question 8 Remove the comment from the line beneath this one and run this code. What will the line below output/print? You should know the answer now because of Questino 5.
# print("This is me printing func_two", func_two)




# Array Questions:
array = [69, 420, 73, 42]


def func_three(parameter_because_i_can_name_this_anything):
    for i in parameter_because_i_can_name_this_anything:
        print(i)


def func_four(parameter_because_i_can_name_this_anything):
    for i in range(len(parameter_because_i_can_name_this_anything)):
        print(i)

# https://stackoverflow.com/questions/53421435/whats-the-difference-between-using-range-and-using-a-for-loop
# Question 9 Remove the comment from the two lines beneath this one and run this code. What will the lines below output/print? Will they print the same thing?
# func_three(array)
# func_four(array)


def func_five(jack_in_the_box):
    for i in range(len(jack_in_the_box)):
        jack_in_the_box[i] = 18


func_five(array)
# Question 10 Remove the comment from the line beneath this one and run this code. What will the line below output/print?
# print(array)


def func_six():
    x = 10


# Question 11 Remove the comment from the print statement beneath this question and run this code. What will the line below output/print? Hint... There might be an error.
# https://www.datacamp.com/tutorial/scope-of-variables-python
func_six()
# print(x)


# Question 12 Remove the comment from the print statement beneath this question and run this code. What will the line below output/print?
# https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/
def func_seven(x):
    x = 10
x = 23
func_seven(x)
#print("The value of x after func_seven is...", x)
