# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    f = 0
    for i in nums:
        k = -1
        for j in nums:
            k += 1
            if f == k:
                continue
            if i + j == target:
                return [f, k]
        f += 1


def max_profit(prices):
    profit = 0
    for i in prices:
        for j in prices:
            temProfit = j - i
            if temProfit > profit:
                profit = temProfit
                print(i, j)
        prices = prices[1::]
    return profit


def max_subarray(nums):
    maxSum = 0
    subArrLen = len(nums)
    i = 1
    k = 0

    for z in nums:
        maxSum += z

    while(k < subArrLen):
        tempSum = 0

        for j in nums[k:i]:
            tempSum += j
        
        if maxSum < tempSum:
            maxSum = tempSum
            
        if i == subArrLen:
            k += 1
            i = 0

            while(i < k):
                i += 1

        i += 1

        if i == k and i + 1 != subArrLen:
            i += 1

    return maxSum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    #print(two_sum([3, 3], 6))   # [0, 1]
    #print(max_profit([7, 1, 5, 3, 6, 4]))   #5
    #print(max_subarray([-1, -2, -3]))   #-1
    pass


if __name__ == "__main__":
    main()
