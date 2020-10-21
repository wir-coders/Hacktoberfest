# implements the kadane algorithm
# https://en.wikipedia.org/wiki/Maximum_subarray_problem

def kadane(l): # max_ending_here, max_so_far
    meh, msf = 0, 0
    a, b = 0, 0
    for i, x in enumerate(l):
        meh += x
        if meh < 0: meh = 0; a = i + 1
        if msf < meh: msf = meh; b = i
    return msf, a, b
    
# printing an example of the algorithm
m, a, b = kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(m, (a, b)) # 6 3 6  (i.e. 4, -1, 2, 1)
