try:
    result = 10 / 7
    print(result)
    
except ZeroDivisionError:
    print(ZeroDivisionError)
finally:
    print("finally")