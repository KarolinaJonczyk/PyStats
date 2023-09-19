def mean(x: list)->float:
    """"arithmetic mean (average) of list
    adding all elements and divide by umber of elements"""
    if len(x) <= 1:
        raise TypeError("mean need more than one element")
    else: 
        sum_of_elements =sum(x)
        mean_value = sum_of_elements/len(x)
        return mean_value
    
     
def median(x:list)->float:
    """classic meadian of numeric data
    odd: finding the middle value
    even: arithmetic mean of two middle values"""
    x = sorted(x)
    n = len(x)
    if n == 0:
        return TypeError("mean not exist")
    if n%2 == 1:
        return x[n//2]
    if n%2 != 1:
        return (x[n//2] + x[n//2 - 1])/2
    
def low_median(x:list)->float:
    """median of numeric data:
    odd: works like classic median function
    even: return smaller middle value"""
    x = sorted(x)
    n = len(x)
    if n == 0:
        return TypeError("mean not exist")
    if n%2 == 1:
        return x[n//2]
    if n%2 != 1:
        return x[n//2 - 1]
    
def high_median(x:list)->float:
    """median of numeric data:
    odd: works like classic median function
    even: return bigger middle value"""
    x = sorted(x)
    n = len(x)
    if n == 0:
        return TypeError("mean not exist")
    else:
        return x[n//2]
    
def minimum(x:list)->float:
    """returns the smallest number in the list"""
    x = sorted(x)
    return x[0]

def maximum(x:list)->float:
    """returns the largest number in the list"""
    x = sorted(x)
    n = len(x)
    return x[n-1]

def standard_deviation(x:list)->float:
    """returns standard deviation of numeric data
    find the square root of the average
    of the squared differences between each 
    data point and the mean
    """
    mean_x = mean(x)
    n = len(x)
    s=0
    for i in x:
        s += (x[i-1] - mean_x)**2
    sd = (s/n)**0.5
    return sd

def variation(x:list)-> float:
    """returns square of standard deviation of numeric data"""
    under_sqrt = standard_deviation(x)
    return under_sqrt**2

def quantiles(q_n, x:list)->float:
    """q_n - number of quartile
        1st quantile: median of the first half of the sorted list
        2nd quantile: median of all list
        3rd quantile: median of the second half of the sorted list
        4th quantile: maximum of list"""
    x = sorted(x)
    n = len(x)
    if q_n not in [1,2,3,4]:
        return TypeError("choose only 1, 2, 3 or 4 quartile")
    else:
        if q_n == 1:
            end = int(n*0.5)
            x = x[0:end]
            return median(x) 
        if q_n == 2:
            return median(x)  
        if q_n == 3:
            start = int((n*0.5))
            end = int(n)
            x = x[start:end]
            return median(x)
        if q_n == 4:
            return max(x)

    
assert mean([1,2,3]) == 2
assert mean([1,2,3]) == 2.5, "False"
assert mean([0])
assert mean()

assert median([1,2,3,4]) == 2.5
assert median([1,2,3,4]) == 2, "must be 2.5"
assert median([1,2,3,4]) == 3, "must be 2.5"
assert median([1,2,3]) == 2
assert median([1,2,3]) == 2.5, "must be 2"
assert median([]) 

assert low_median([1,2,3,4]) == 3, "must be 2"
assert low_median([1,2,3,4]) == 2.0

assert high_median([1,2,3,4]) == 2, "must be 3"
assert high_median([1,2,3,4]) == 3

assert minimum([0,1,2,3]) == 1, 'must be 0'
assert minimum([0,1,2,3]) == 0

assert maximum([0,1,2,3]) == 1, 'must be 3'
assert maximum([0,1,2,3]) == 3

assert standard_deviation([2,1]) == 0.5
assert standard_deviation([2,1]) == 1, 'bad solution, it\'s 0.5'

assert variation([2,1]) == 0.5, 'bad solution, it\'s 0.25'
assert variation([2,1]) == 0.25

assert quantiles(1, [1,2,3,4]) == 1.5
assert quantiles(1, [1,2,3,4]) == 1
assert quantiles(5, [1,2,3,4]) == 4