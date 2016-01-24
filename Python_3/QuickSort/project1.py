import sys
import time

def quicksort(lyst,length):
    if(length <= 10):
      IS(lyst, length)
    else:
      quicksortHelper(lyst, 0, length - 1)

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary)
    return boundary

def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

def IS(a,length):
    for i in range(1,length,1):
        j = i
        value = a[j]
        while (j > 0 and value < a[j-1]):
            a[j] = a[j-1]
            j = j-1
        a[j] = value

def main():

    filename = "file3"
    length = int(input("How many lines?"))
    a = []
    file = open(filename,"r")
    for i in range(0,length,1):
        a.append(int(file.readline()))

    t1 = time.process_time()
    quicksort(a,length)
    t2 = time.process_time()

    print (t2-t1)

main()    
            
                
