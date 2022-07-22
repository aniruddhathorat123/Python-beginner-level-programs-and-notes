# largest palindrome of two 3 - digit numbers.
# find the largest palindrom from multiplication of 2 - 3 digit number(aaa x bbb).

from time import time

# check whether given number is palindrome or not.
def is_palindrome(val):
    return str(val) == str(val)[::-1]

# start from highest 3 digit number to lowest 3 digit number
# so that we can get largest palindrome in less iterations.
def palindrome():
    start_time = time()
    palindrome_nums = []
    iterations = 0
    start_no = 100
    start2_no = 100
    end_no = 999
    # Go in reverse from high value to low value.
    for num1 in range(end_no, start_no, -1):
        # break the loop once we get lowest 3 digit number which 
        # can possibly generate largest 3 digit palindromne number.
        if num1 < start_no:
            break
        for num2 in range(end_no, start2_no, -1):
            iterations += 1
            res = num1 * num2
            if is_palindrome(res):
                palindrome_nums.append(res)
                # find the lowest cap number which ensure that all numbers
                # below that number will never gives the largest palindrome number.
                start_no = max((num1 * num2) / end_no, start_no)
                start2_no = num2
            # avoid repeated multiplication for same numbers.
            # like 100 * 101 and 101 * 100 like that.
            if num1 == num2:
                break
    print(f"Palindrome nums : {palindrome_nums}")
    print(f"End time : {time() - start_time}")
    print(f"iterations : {iterations}")
    return max(palindrome_nums)

print(f"Algo 1: Largest palindome : {palindrome()}")

# Time efficient alogrithm to find largest palindrome from 3 digit multiplication.
# we are checking highest possible palindrome against the digits 
# whose multiplication can generate te given palindrome.
def palindrome_algo2():
    start_time1 = time()
    iterations = 0
    for dig1 in range(9,0,-1):
        for dig2 in range(9,-1,-1):
            for dig3 in range(9,-1,-1):
                # we create the -palindromes by adding the 'placevalues', 
                # example step 999999 -> 998899 -> 997799 etc but only to 100001 
                palindrome = dig1*100000 + dig2*10000 + dig3*1000 + dig3*100 + dig2*10 + dig1
                #print(palindrome) #debug
                
                #lowest number to check against that can generate a higher 
                low_val = int(palindrome/999) # or low_val = palindrome//999 
                # highest possible factor to check, one factor must be lower than this
                high_val = int(palindrome**0.5)+1
                # check if palindrome divisible by any of the numbers between min and max
                for digit in range(low_val,high_val):
                    iterations += 1
                    #check for divisibility, since we are stepping through palindromes in order, as soon as we find one: we are Done! 
                    if palindrome % digit == 0:
                        return 'palindrome:',palindrome, 'digit:',digit, 'palindrome/digit:', palindrome/digit ,'iterations:',iterations, "end time : ", (time()-start_time1)

print(f"Algo 2: palindrome:{palindrome_algo2()}")


#OP: 
# Palindrome nums : [888888, 861168, 886688, 906609]
# End time : 0.24600005149841309
# iterations : 3585
# Algo 1: Largest palindome : 906609
# Algo 2: palindrome:('palindrome:', 906609, 'digit:', 913, 'palindrome/digit:', 993.0, 'iterations:', 2136, 'end time : ', 0.014999866485595703)
