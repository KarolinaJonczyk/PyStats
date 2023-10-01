import workflows/Pystats1.py

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

assert geom_mean([2,2,2]) == 2
assert geom_mean([2,2,2]) == 3

assert harmonic_mean([2,2,0.5,0.5]) == 0.8
assert harmonic_mean([2,2,0.5,0.5]) == 1.5

assert generalized_mean(2, [1,2]) == 6.25
assert generalized_mean(2, [1,2]) == 6.25000001

assert mode([9,7, 1, 7, 9, 2, 9, 7, 3, 0]) == [7,9]
assert mode([7, 1, 7, 9, 2, 7, 3, 0]) == [7]
assert mode([7, 1, 7, 9, 2, 7, 3, 0]) == 7

assert statistic_range([1,2,3,4]) == 3
assert statistic_range([1,2,3,4]) == 4

assert average_absolute_deviation([1,2,3]) == 0.666666
assert average_absolute_deviation([1,2,3]) == 0.6666666666666666

assert skewness_coef([1,1,2]) == 1
assert skewness_coef([1,1,2,2]) == 1

assert third_central_moment([3,2,3,3,3,1]) == -0.5
assert third_central_moment([3,2,3,3,3,1]) == 0.5

assert kurtosis([1,2]) == 0.125
assert kurtosis([1,2]) == -0.125

assert excess_kurtosis([1,2]) == -2.875
assert excess_kurtosis([1,2]) == 2.875

assert gini_coefficient([1,2,3,4]) == -0.25
assert gini_coefficient([1,2,3,4]) == 0.25

assert covariance([1,2,3], [2,3,5]) == 1.0
assert covariance([1,2,3], [2,3,5]) == 0.1

assert IQR([1,2,3,4]) == 2
assert IQR([1,2,3,4]) == 3
