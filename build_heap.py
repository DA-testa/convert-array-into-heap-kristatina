# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data)-1):
            if data[i]>data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
                swaps.append((i,i+1))
    return swaps

def main():
    izvele = input()
    if "F" in izvele:
        F_path = input()
        with open("./tests/" + F_path + "r") as f:
            n = int(f.read())
            data = list(map(int, f.read().split()))
    elif "I" in izvele:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    #for i in range(len(data)):
        #if 2*i+1 < len(data) and data[2*i+1] < data[i]:
            #return False
        #if 2*i+2 < len(data) and data[2*i+2] < data[i]:
            #return False
    #return True

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
