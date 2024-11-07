#30.	Write a program which takes a sequence of numbers and check if all numbers are unique.

def isUnique(seq: [int]) -> bool:
    # s = set(seq)
    # if len(s) == len(seq):
    #     return True
    # return False
    return len(set(seq)) == len(seq)

if __name__ == "__main__":
    seq = [1,2,3,4,5,5]
    print(isUnique(seq))