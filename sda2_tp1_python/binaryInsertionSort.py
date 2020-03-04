def binary_search(arr, val, start, end):
        if start == end:
                print("1")
                if arr[start] > val:
                        return start
                else:
                        return start + 1

        if start > end:
                print("2")
                return start
        
        mid = int((start + end)/2)
        
        if arr[mid] < val:
                print("3")
                return binary_search(arr, val, mid+1, end)
        elif arr[mid] > val:
                print("4")
                return binary_search(arr, val, start, mid - 1)
        else:
                print("5")
                return mid

def insertion_sort(arr):
        for i in range(1, len(arr)):
                val = arr[i]
                j = binary_search(arr, val, 0, i - 1)
                arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
        return arr

print(insertion_sort([37, 23, 0, 17, 12, 72, 31, 
                        46, 100, 88, 54, -1]))