def makeChange( coins, amount, solutions ):
    '''this function finds out the minimum number of coins needed to make change for the
    amount using dynamic programming
    parameters:
        coins - list of coins (list of int)
        amount - amount to be made change of (int)
        solutions - 
    returns:
        result - minimum number of coins needed to make change of the amount (int)
    '''
    number_of_coins = len( coins )
    result = float('inf')
    for coin in coins:
        if coin < amount:
            if solutions[amount - coin] != float( 'inf' ):
                temp_solution = 1 + solutions[amount - coin]
            else:
                temp_solution = 1 + makeChange( coins, amount - coin, solutions )
                solutions[amount - coin] = temp_solution
            if temp_solution <= result:
                result = temp_solution
                solutions[amount] = result
        elif coin == amount:
            result = 1
            solutions[amount] = result
        elif coin > amount:
            break
    return result

def main():
    coins = input( "Enter the coins separated by space " )
    coins = coins.split()
    coins = [ int( coins[idx] ) for idx in range( len( coins )) ]
    amount = int( input( "Enter the amount " ))
    solutions = []
    for idx in range( max( [ amount + 1, max( coins ) ] ) ):
        if idx in coins:
            solutions.append( 1 )
        else:
            solutions.append( float('inf') )
    result = makeChange( coins, amount, solutions )
    print( "Coins needed to make change for", amount, "is", result )
    
if __name__ == '__main__':
    main()