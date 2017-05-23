def search(x, nums):
    low = 0
    high = len(nums) -1
    count = 0  # new line
    print("START RANGE: ", low, "--", high)
    print("ELEMENT SEARCHING FOR: ", x)
  
    while low <= high:  #while still range to search
        print("searching list from low to high: ", low, '--', high)
        mid = (low+high)//2         #take midpoint of list
        item = nums[mid]
        count = count + 1
        if x == item:      #found it!
            print('found target value:', x, ' in position:', mid)
            print('NUMBER OF COMPARISONS: ', count)
            return mid
        elif x < item:  #x in lower half of range
            print('x in lower half of range')
            high = mid-1
        else:   #x is in upper half
            print('x in upper half of range')
            low = mid+1

    
    return -1


# to test
mylist = list(range(1000))
print ("binary search list",mylist)
search (999, mylist)
