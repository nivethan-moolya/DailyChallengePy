'''
Date: Feb 06
Challenge: Write a function that groups a string into parentheses clusters. Each cluster should be balanced.
Algorithm:
01: Count the number of immediate open parenthesis
02: Make a temporary list & append all open + closed parenthesis until closedParentheses==openParentheses (a full balanced parenthesis)
03: Once 02 criteria is met, join the temp list into a string and append into an output list + clear the temp list for next iteration if any.
'''

def makeBalancedCluster(shuffledParentheses):
    balancedParentheses = []
    tempCluster = []
    openParentheses=0
    closedParentheses=0
    for i in range(0,len(shuffledParentheses)):
        if '(' in shuffledParentheses[i]:
            openParentheses+=1
            tempCluster.append(shuffledParentheses[i])
        elif ')' in shuffledParentheses[i] and closedParentheses<openParentheses:
            closedParentheses+=1
            tempCluster.append(shuffledParentheses[i])
        else:
            tempCluster.clear()
            balancedParentheses.clear()
            balancedParentheses.append('Invalid Input')
            break

        if closedParentheses==openParentheses:
            balancedParentheses.append(''.join(tempCluster))
            tempCluster.clear()
    print(f'Balanced Cluster of parentheses: {balancedParentheses}')
    return balancedParentheses

makeBalancedCluster(input(f'Provide string of Parentheses to make balanced clusters:'))