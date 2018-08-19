def makeChange( coins, amount ):
    '''recursively calls the makeChange function to get the minimum number of coins needed
    to make change for the amount
    parameters:
        coins - list of coins (list of int)
        amount - amount to be made change of (int)
    returns:
        solution - minimum number of coins needed to make change of the amount (int)
    '''
    number_of_coins = len( coins )
    solution = float('inf')
    for coin in coins:
        if coin < amount:
            temp_solution = 1 + makeChange( coins, amount - coin )
            if temp_solution <= solution:
                solution = temp_solution
        elif coin == amount:
            solution = 1
        elif coin > amount:
            break
    return solution

def main():
    coins = input( "Enter the coins separated by space " )
    coins = coins.split()
    coins = [ int( coins[idx] ) for idx in range( len( coins )) ]
    amount = int( input( "Enter the amount " ))
    solution = makeChange( coins, amount )
    print( "Coins needed to make change for", amount, "is", solution )

if __name__ == '__main__':
    main()