def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)    #리스트의 길이만큼 반복, 가장 작은 원소를 순서대로 저장
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,6,2,10]))
#가장 작은 원소를 선택해 새로운 리스트에 정렬
