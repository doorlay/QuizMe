#This file contains the code for my AP Computer Science Principles test performance task


#This marks start of the partition phase of the quicksort algorithm
def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

#This marks the beginning of the sort phase of the quicksort algorithm
def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

#The function that actually sorts through the list.
def main(myList):
    sortedList = quicksort(myList,0,len(myList)-1)
    print(sortedList)
    
    
#To get function to sort, define an array named 'myList' below. Then, pass into a call for main()
myList = [5,91,23,17,11,2]
main(myList)

