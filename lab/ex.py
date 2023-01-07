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
@trace
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

cascade2(1234)