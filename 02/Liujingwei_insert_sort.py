arr = [75, 38, 21, 111, 888, 5647, 158, 3, 25, 77]

for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
        b = arr[i]
        j = i

        while j > 0 and arr[j - 1] > b:
            arr[j], arr[j - 1] = arr[j - 1], b
            j = j - 1

print arr
