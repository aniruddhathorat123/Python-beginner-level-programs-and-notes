# Exceptions handling:

#try:
    #code you want to run
#except:    
    #executed if error occurs
    # same like catch block.
#else:
    #executed if no error
#finally:
    #always executed 
    
# e.g.:
try:
    num = int(input("Enter the number between 1 to 30: "))
    if num > 30:
        raise ValueError
    30/num
except ZeroDivisionError as error:
    print(error, ": Can't divide number by zero!")
except ValueError as error:
    print(error, ": Bad input!")
# generic error handling    
except:
    print("Invaid input!")
else:
    print(f"30/{num} = {30/num}")
finally:
    print("* Thanks for playing *")



