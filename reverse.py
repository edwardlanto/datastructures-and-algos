def reverse(array):
    for i in range(int(len(array) / 2)):
        other = len(array) - i - 1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    return array

print(reverse([ 1,2,3,4 ]))

# Big 0 = O(N) 
# Divided by two because the array is swapping two elements