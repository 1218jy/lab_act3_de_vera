# List comprehension to compute square of odd integers
#from a given list of integers, create a new list using comprehension that will compute the square of odd integer elements.

#sample calls

#[2,4,3] == [9] [0,0,1,1] == [1,1]


def square_of_odds(lst):
    return [x**2 for x in lst if x % 2 != 0]

print(square_of_odds([2, 4, 3])) 
print(square_of_odds([0, 0, 1, 1]))   
