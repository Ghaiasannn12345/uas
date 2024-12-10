def Bubble_sort (arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

data = [50,49,48,47,46,45,44,43,42,41,40,31,32,33,34,35,36,37,38,39,30,29,28,27,26,25,24,23,22,21,20,11,12,13,14,15,16,17,18,19,10,9,7,8,6,1,2,3,4,5]
print(f"data sebelum di urutkan", data)
sorting_data = Bubble_sort(data)
print(f"data sesudah di urutkan",sorting_data)
