def linear_search(list:list, target):
    for index in range(len(list)):
        if list[index] == target:
            return index
    return None
my_list = [1, 2, 3, 4, 5]
index=linear_search(my_list, 3)
if index is not None: 
    print("3 os not in the list")
else:
    print("3 is in the list at index", index)
#binary search
#works only on sorted list
#we look at the middle element of the list and compare it to the target
#if the target is less than the middle element we search the left half of the list
#if the target is greater than the middle element we search the right half of the list
#then we repeat the process until we find the target or the list is empty
def binary_search(list:list, target):
    low=0
    high=len(list)-1
    while low <= high:
        mid=(low+high)//2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low=mid+1
        else:
            high=mid-1
    return None
my_list = [1, 2, 3, 4, 5]
index=binary_search(my_list, 3)
if index is not None:
    print("3 is in the list at index", index)
else:
    print("3 is not in the list") 