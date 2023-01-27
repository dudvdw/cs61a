# Q4
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    product = 1
    while k>0:
      product = product *  n
      n = n - 1
      k = k - 1
    print(product)
    return product


# Q5 Sum digit
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    sum = 0
    while y > 0:
      digit = y % 10
      sum = sum + digit
      y = y // 10
    print(sum)
    return sum

# Q7 Double Eight
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    flag = False
    while n>0:
      digit = n % 10
      n = n // 10
      if digit != 8:
        flag = False
      else: 
        if flag == True:
          print(True)
          return True
        else:
          flag = True
    print(False)
    return False
double_eights(1808)