import time

def forFinder(num):
    is_prime = True
    for i in range(num):
        if num % (i+1) == 0:
            if i+1 != num and i > 1:
                is_prime = False
                break
    if is_prime:
        return True
    else:
        return False

def whileFinder(num):
    is_prime = True
    i = 0
    while i < num:
        if num % (i+1) == 0:
            if i+1 != num and i > 1:
                is_prime = False
                break
        i += 1
    if is_prime:
        return True
    else:
        return False

number = int(input("Enter the number"))
before = time.perf_counter_ns()
solution_for = forFinder(number)
after = time.perf_counter_ns()
time_for = after-before
before = time.perf_counter_ns()
solution_while = whileFinder(number)
after = time.perf_counter_ns()
time_while = after-before
if solution_for:
    print("The number is prime and took: " + str(time_for) + "ns for the for function and " + str(time_while) + "ns for the while function")
else:
    print("The number is not prime and took: " + str(time_for) + "ns for the for function and " + str(time_while) + "ns for the while function")