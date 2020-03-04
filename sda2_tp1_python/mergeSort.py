def mergeSort(arr):
        print(arr)
        if len(arr) > 1:
                # Getting the middle index of the array
                mid = len(arr) // 2
                # Saving first half in L
                L = arr[:mid]
                # Saving second half in R
                R = arr[mid:]

                mergeSort(L)
                mergeSort(R)

                i = j = k = 0

                # Copy data to temp arrays L[] and R[]
                while i < len(L) and j < len(R):
                        if L[i] < R[j]:
                                arr[k] = L[i]
                                i+=1
                        else:
                                arr[k] = R[j]
                                j+=1
                        k+=1
                
                # Check if any element was left
                while i < len(L):
                        arr[k] = L[i]
                        i+=1
                        k+=1
                
                while j < len(R):
                        arr[k] = R[j]
                        j+=1
                        k+=1
        

def printList(arr):
        for i in range(len(arr)):
                print(arr[i], end=" ")
        print()

if __name__ == '__main__':
        arr = [12, 11, 13, 5, 6, 7]
        print("Given array is", end="\n")
        printList(arr)
        mergeSort(arr)
        print("Sorted array is: ", end="\n")
        printList(arr)   

