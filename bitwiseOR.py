#to take bitwise OR and then sum of all
#test case : 3
# 1 2 3
#O/P : 15



def solve(arr):
    answer = 0
    subarrays = dict()
    
    for x in arr:
        subarrays[0] = 1
        
        subarrays2 = dict()
        
        for y in subarrays:
            y2 = x | y
            if y2 not in subarrays2:
                subarrays2[y2] = subarrays[y]
            else:
                subarrays2[y2] += subarrays[y]
            answer += subarrays[y] * y2
        subarrays = subarrays2
        
    return answer

input()
arr = [ int(x) for x in input().split()]
answer = solve(arr)
print(answer)


