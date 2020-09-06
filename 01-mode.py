listNumbers = [1,2,3,4,5,6,6,8,8,6,9]
listGrades = [87.5, 88.5, 60.5, 90.5, 88.5]

def Mode(arr):
    array = max(set(arr), key = arr.count)
    print("max frequen in array:",array)

Mode(listNumbers)
Mode(listGrades)