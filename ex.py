def all_pairs(s):
    for item1 in s:
        for item2 in s:
            for item3 in s:
                yield (item1, item2, item3)


def letters_generator():
        current = 'a'
        while current <= 'd':
            yield current
            current = chr(ord(current)+1)

def combo (a, b):
  """Return the smallest integer with all of the digits of a and b (in order).
  >>> combo(531, 432)
  45312
  >>> combo(531, 4321)
  45321
  >>> combo(1234, 9123)
  91234
  """
  if a == 0 or b == 0:
    return a + b
  elif a % 10 == b % 10:
    return combo(a//10, b//10)*10 + a%10
  return min(combo(a//10, b)*10 + a%10, combo(a, b//10)*10 + b%10)

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else: 
        return count_partitions(n-m, m) + count_partitions(n, m-1)

def div(n, d):

  '''
  >>> q, r = div(2013, 10)
  >>> q
  201
  >>> r
  3
  '''
  return n//d, n%d

def fib(n):
  pre, cur = 0, 1
  while n > 0:
    pre, cur = cur, pre+cur
    n -= 1
    print(pre)
  return cur


def search(f):
  x = 0
  while True:
    if f(x):
      return x
    x += 1

def square(x):
  return x*x

def inverse(f):
  """Return a function g(y) that returns x such that f(x) == y
  >>> sqrt = inverse(square)
  >>> sqrt(16)
  4
  """
  def inverse_of_f(y):
    def is_inverse_of_y(x):
      return f(x) == y
    return search(is_inverse_of_y)
  return inverse_of_f
  # return lambda y: search(lambda x: f(x) == y)

def apply_twice(f, x):
  return f(f(x))

def make_adder(n):
  def adder(k):
    return k + n
  return adder

def compose(f, g):
  def h(x):
    return f(g(x))
  return h

def print_sums(n): 
  print(n)
  def next_sum(k):
    return print_sums(n+k)
  return next_sum

def curry2(f):
  """Return a curried version of the given two-arguments function"""
  def g(x):
    def h(y):
      return f(x, y)
    return h
  return g

def uncurry2(g):
  """Return a two-arguments version of the given curried function"""
  def f(x, y):
    return g(x)(y)
  return f

def remove(n, digit):
  kept, digits = 0, 0
  while n > 0:
    n, last = n // 10, n % 10
    if last != digit:
      kept = kept + last * pow(10, digits)
      digits += 1 
  print(kept)
  return kept

def sum_digits(n):
  if n<10:
    return n
  else:
    all_exclude_last, last = n // 10, n % 10
    return sum_digits(all_exclude_last) + last

def factorial(n):
  fact = 1
  i = 1
  while i <= n:
    fact *= i
    i += 1
  return fact
    
def fact(n):
  if n == 0:
    return 1
  else:
    return n * fact(n-1)

def cascade(n):
  if n < 10:
    print(n)
  else:
    print(n)
    cascade(n//10)
    print(n)

def cascade2(n):
  grow(n)
  print(n)
  shrink(n)

def f_then_g(f, g, n):
  if n: 
    f(n)
    g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

