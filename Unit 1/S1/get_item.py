def get_item(arr, x):
    if x < 0 or x >=len(arr):
        print("Index out of range")
        return None

    else:
        print(arr[x])
        return arr[x]
items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)