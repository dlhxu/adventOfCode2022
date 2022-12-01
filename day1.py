import sys
import heapq

# part 2
def topThreeMaxCals(lines):
    hq = []
    temp = 0
    for line in lines:
        if not line == "\n":
            temp += int(line)
        else:
            heapq.heappush(hq, temp)
            temp = 0
    # end of file, push to heap
    heapq.heappush(hq, temp)
    return sum(heapq.nlargest(3, hq))

# part 1
def maxAmountOfCals(lines):
    maxCals = 0
    temp = 0
    for line in lines:
        if not line == "\n":
            temp += int(line)
        else:
            maxCals = max(maxCals, temp)
            temp = 0
    return maxCals

def main():
    # parse input from file
    with open('input_day1.txt', 'r') as fp:
        lines = fp.readlines()
        maxCals = topThreeMaxCals(lines)
        print(maxCals)

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
