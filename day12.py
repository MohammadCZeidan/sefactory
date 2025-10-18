#selection sort
#https://algorithm-visualizer.seancoughlin.me/sorting/selectionSort
#find the smallest element in the array and swap it with the first element
def selection_sort(list):
    n = len(list)
    for i in range(len(list)-1):
        min_index = i
        for j in range(i + 1, n):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]#temp=list[i] list[i]=list[min_index] list[min_index]=temp 
    return list
print(selection_sort([64, 25, 12, 22, 11]))
#merge sort
#https://algorithm-visualizer.seancoughlin.me/sorting/mergeSort
#devide the array into two halves, sort each half recursively, and then merge the sorted halves back together
def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1
    return list