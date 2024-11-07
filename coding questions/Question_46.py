#46.	How to find second largest integer in an array using only one loop?

def sec_largest(arr: [int]) -> int:
    max = second = float('-inf')
    for i in arr:
        if max < i:
            second = max
            max = i
        elif i > second and i != max:
            second = i
    return second

if __name__ == "__main__":
    arr = [100,2,3,4,5,4,1,10,56,7]
    print(sec_largest(arr))
