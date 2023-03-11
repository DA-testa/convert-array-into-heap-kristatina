# python3
import heapq

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    heapq.heapify(data)
    swapCount = 0
    for i in range(len(data)):
        swaps.append(heapq.heappop(data))
        swapCount += 1
    return swaps, swapCount

def main(data, swapCount):
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    for i in range(len(data)):
        if 2*i+1 < len(data) and data[2*i+1] < data[i]:
            return False
        if 2*i+2 < len(data) and data[2*i+2] < data[i]:
            return False
    return True

    izvele = input("F vai I?")
    if "F" in izvele:
        F_path = input("faila ceļš: ")
        with open(F_path, "r") as f:
            n = f.read()
            data = list(map(int, input().split()))
    elif "I" in izvele:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
        
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print(4*len(data))
    print(swapCount)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
