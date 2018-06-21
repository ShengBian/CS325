# Author: Sheng Bian
# Date: April 22, 2017
# Description: This program read input from a file named “amount.txt”. The
# file contains lists of denominations (V) followed on the next line by the amount A.
# The results should be written to a file named change.txt and should contain the
# denomination set, the amount A, the change result array and the minimum number of
# coins used.

# This function is used for making change implementation. It will return minimum number
# of coins used. The following code reference from
# http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
# And I also get some idea from group discussion.
def makeChange(denominations, amount, minCoins, coinsUsed):
    for cent in range(amount + 1):
        coinCount = cent
        newCoin = 1
        for i in [c for c in denominations if c <= cent]:
            if minCoins[cent - i] + 1 < coinCount:
                coinCount = minCoins[cent - i] + 1
                newCoin = i
        minCoins[cent] = coinCount
        coinsUsed[cent] = newCoin
    return minCoins[amount]


# This function walks backward through the table to return the value of each coin used.
# The following code reference from
# http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
def coinsList(coinsUsed, change):
    coin = change
    array = []
    while coin > 0:
        thisCoin = coinsUsed[coin]
        coin = coin - thisCoin
        array.append(thisCoin)
    return array

# This function return an array of amount that each coin used.
def changeResult(arr1, arr2):
    arr = []
    for a in arr1:
        num = 0
        for b in arr2:
            if a == b:
                num = num + 1
        arr.append(num)
    return arr

# The following code exectuate above functions. It read data from amount.txt and write results
# to change.txt.
with open('change.txt', 'w') as file_output:
    with open('amount.txt', 'r') as file_input:
        for line in file_input:
            #
            file_output.write(line)
            line = line.rstrip('\n')
            deno = []
            for s in line.split(' '):
                s = int(s)
                deno.append(s)
            # read the second line of the code, that's amount
            line2 = next(file_input)
            line2 = line2.rstrip('\n')
            line2 = line2 + '\n'
            file_output.write(line2)
            line2 = line2.rstrip('\n')
            amount = int(line2)
            usedCoin = [0] * (amount + 1)
            coinAmount = [0] * (amount + 1)
            minAmount = makeChange(deno, amount, coinAmount, usedCoin)
            resultArr = changeResult(deno, coinsList(usedCoin, amount))
            merged = ' '.join([str(i) for i in resultArr]) + '\n'
            file_output.write(merged)
            file_output.write(str(minAmount) + '\n')
