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
    else:
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
    else:
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
    data point and the mean"""
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

def geometric_mean(x:list)->float:
    '''Geometric mean is defined as the n-th root of the product of n numbers'''
    n = len(x)
    result = 1
    for i in range(n):
        result *= x[i]
    result = result**(1/n)
    return result


def harmonic_mean(x:list)->float:
    '''The harmonic mean is a numerical average calculated by dividing the number of observations
    by the reciprocal of each number in the series'''
    n = len(x)
    result = 0
    for i in range(n):
        result += 1/(x[i])
    result = n / result
    return result


def generalized_mean(k, x:list)->float:
    '''k = 2 quadratic mean
       k = 0 geometric mean
       k != {0,2} generalized mean with exponent k of real numbers'''
    n = len(x)
    if k == 0:
        result=geom_mean(x)
    else:
        result = 0
        for i in range(n):
            result += x[i]**k
        result = (result/n)**k
    return result

def mode(x:list)->list:
    '''Returns the most frequent element in the list 
    in case of multiple dominants, it returns their list'''
    counting = []
    mode = []
    for i in set(x):
        num = x.count(i)
        counting.append(num)
        maximum = max(counting)
        elements = list(set(x))
    for i, count in enumerate(counting):
        if count == maximum:
            mode.append(elements[i])
    return mode

def statistic_range(x:list)->float:
    '''difference between the largest and smallest values from list'''
    xmin = min(x)
    xmax = max(x)
    xrange = xmax - xmin
    return xrange

def average_absolute_deviation(x:list)->float:
    '''Average absolute deviation is defined as the mean of absolute
    values of the deviations from list'''
    xmean = mean(x)
    n = len(x)
    s = 0
    for i in range(n):
        s += abs(x[i] - xmean)
    avg_abs_mean = s/n
    return avg_abs_mean

def skewness_coef(x:list)->float:
    '''skewnes coefficient is is a measure of the asymmetry of the probability 
    distribution of a real-valued random variable about its mean.
    The skewness value can be positive, zero, negative, or undefined.
    negative skew - left-skewed
    zero - no skewness
    positive skew - right-skewed'''
    if len(mode(x)) == 1:
        skew = (mean(x) - mode(x)[0])/standard_deviation(x)
    else:
        skew = (mean(x) - mean(mode(x))) / standard_deviation(x)
    return skew

def third_central_moment(x:list)->float:
    '''according to the definition of the central moment, the sum of 
    the third powers of deviations of the value of a statistical 
    feature from the arithmetic mean value, divided by n
    zero - symmetrical distribution
    negative - left-skewed
    positive - right-skewed'''
    n = len(x)
    m = mean(x)
    s = 0
    for i in range(n):
        s += (x[i] - m)**3
    s = s/n
    return s

def kurtosis(x:list)->float:
    '''kurtosis is a measure of the "tailedness" of the probability
    distribution of a real-valued random variable.
    zero -  the excess kurtosis of any univariate normal distribution
    positive - leptokurtic
    negative - platykurtic'''
    n = len(x)
    s = 0
    for i in range(n):
        s+=(1/n) * (x[i] - mean(x))**4
    return s/standard_deviation(x)

def excess_kurtosis(x:list)->float:
    '''The excess kurtosis is defined as kurtosis minus 3.
    '''
    xkurtosis = kurtosis(x)
    ex_kurtosis = xkurtosis - 3
    return ex_kurtosis

def gini_coefficient(x:list)->float:
    '''work in progress...
    I need to read more about this method'''
    n = len(x)
    if x == sorted(x):
        s = 0
        for i in range(n):
            s += (2*i - n -1)*x[i]
        gini = s/(mean(x)*n**2)
    #else/elif:...
        return gini   

def covariance(x:list, y:list)->float:
    '''Covariance is a measure of the joint variability of two random variables.'''
    n = len(x)
    xmean = mean(x)
    ymean = mean(y)
    cov = 0
    for i in range(n):
        cov += (x[i] - xmean)*(y[i] - ymean)
    cov = cov/n
    return cov

def IQR(x:list)->float:
    '''Interquartile range (IQR).
    This is a measure of statistical dispersion, 
    which is the spread of the data.'''
    iqr = quantiles(3, x) - quantiles(1, x)
    return iqr

def testfunc():
    pass
