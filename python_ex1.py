#Write a short Python function, is multiple(n, m), that takes two integer
#values and returns True if n is a multiple of m, that is, n = mi for some
#integer i, and False otherwise.    
def is_multiple(n,m):
    if n % m == 0:
        return True
    else:
        return False 


##Write a short Python function, is even(k),
# that takes an integer value and
#returns True if k is even, and False otherwise. 
# However, your function cannot use the multiplication, modulo, or division operators.
def is_even(k):
    return str(k)[-1] in ('0','2','4','6','8')


#Write a short Python function, minmax(data), 
# that takes a sequence of
#one or more numbers, and returns the smallest 
# and largest numbers, in the
#form of a tuple of length two. 
# Do not use the built-in functions min or
#max in implementing your solution.

def minmax(data):
    min_ = max_ = data[0]
    for val in data:
        if val < min_:
            min_ = val
        if val > max_:
            max_ = val
    return min_,max_            


#Write a short Python function that takes
#  a positive integer n and returns
#the sum of the squares of all 
# the positive integers smaller than n.

def sum_squares(integer):
    ssq = 0
    for x in range(0,integer):
        ssq =ssq + x**2
    return(ssq)

def sum_squares_listcomp(integer):

    ssq = sum([x**2 for x in range(integer)])
    return(ssq)

#Write a short Python function that takes a positive integer
#n and returns the sum of the squares of all the odd
#positive integers smaller than n.
#+ as a line in list comprehension

def sum_sqaures_odd_listcomp(integer):
    ssq = sum([x**2 for x in range(integer) if x%2 != 0])
    return ssq

#What parameters should be sent to the range constructor, to produce a
#range with values 50, 60, 70, 80?
print([x for x in range(50,81,10)])

#Python allows negative integers to be used as indices into
#  a sequence, such as a string. If string s has length n,
#  and expression s[k] is used for index −n≤k<0, what is 
# the equivalent index j ≥0 such that s[j] references
#the same element?

streeng = 'string'

n = len(streeng)
j = -4
print(streeng[j])
k = j + n
print(n)

#What parameters should be sent to the range constructor, to produce a
#range with values 8, 6, 4, 2, 0, −2, −4, −6, −8

print([x for x in range(8,-9,-2)])

#Write a Python function that takes a sequence 
# of numbers and determines
#if all the numbers are different from each other
# (that is, they are distinct).

def is_distinct(data):
    cell1 = list(data)
    cell2 = set(data)
    return (len(cell1) == len(cell2))

print(is_distinct([1,2,3,3]))

def mutable_func(array,newel):
    array.append(newel)

my_list = [1,2,3,4]

mutable_func(my_list,5)
print(my_list)

def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor

(scale(my_list,5)) 
print(my_list)       


#C-1.18
#[0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
print([2**x for x in range(0,10,2)])