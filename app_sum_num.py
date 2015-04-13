# Write a method that takes in an integer `num` and returns the sum of
# all integers between zero and num, up to and including `num`.
#
# Difficulty: easy.	

n = raw_input("Give me a number: ")
num = int(n) + 1
list = []

def sum_nums(num):
    for i in range(0, num):
        list.append(i)
    print sum(list)

sum_nums(num)

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print 'sum_nums(1) == 1: ' + str(sum_nums(1) == 1)
print 'sum_nums(2) == 3: ' + str(sum_nums(2) == 3)
print 'sum_nums(3) == 6: ' + str(sum_nums(3) == 6)
print 'sum_nums(4) == 10: ' + str(sum_nums(4) == 10)
print 'sum_nums(5) == 15: ' + str(sum_nums(5) == 15)

