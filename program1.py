import sys

money = sys.argv[1]

def moneyCount(amount):
    #calculates the amount of dollars, quarters, dimes, nickels, and pennies needed
    global money
    money = money.split('.')
    try:
        dollars = int(money[0])
        if dollars > 0:
            print(dollars, ' dollars')
    except:
        print('please provide a dollar amount')
        return
    
    try:
        cents = int(money[1])
        quarters = cents//25
        cents %= 25
        dimes = cents//10
        cents %= 10
        nickels = cents//5
        cents %= 5
        pennys = cents
        
        coins = [quarters,dimes,nickels,pennys]
        for coin in coins:
            if coin != 0:
                print

        if quarters != 0:
            print(quarters, " quarters")
        if dimes != 0:
            print(dimes, " dimes")
        if nickels != 0:
            print(nickels, " nickels")
        if pennys != 0:
            print(pennys, " pennys")

    except:
        print('please provide a cent amount')
        return

    return

if money[0] == '$':
    money = money.replace('$', '')
    moneyCount(money)
else:
    print('string must have $ as its first character \nsome terminals may eat the $ sign, in which case please use \$ instead')
