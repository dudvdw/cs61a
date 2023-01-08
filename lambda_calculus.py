# interpret and visualize
def x_():
    return 0

def f_(x=None):
    return lambda : 1 + x()

def interpret(f):
    print(f(f_)(x_)())

def predicate(f):
    if f(f_)(x_)() == 0:
        print(False)
    else:
        print(True)

Church_0 = lambda f: lambda x: x
Church_1 = lambda f: lambda x: f(x)
Church_2 = lambda f: lambda x: f(f(x))
Church_3 = lambda f: lambda x: f(f(f(x)))

SUCC = lambda n: lambda f: lambda x: f(n(f)(x))

PLUS = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))

MULT = lambda m: lambda n: m(PLUS(n))(Church_0)

PRED = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda u: u)

Church_True = lambda u: lambda v: u
Church_False = lambda u: lambda v: v

# AND = λ p.λ q.p q p
AND = lambda p: lambda q: p(q)(p)
# OR = λ p.λ q.p p q
OR = lambda p: lambda q: p(p)(q)
# NOT = λ p.p FALSE TRUE
NOT = lambda p: p(Church_False)(Church_True)

# 数学定义： ISZERO = λ n. n (λ x. FALSE) TRUE
ISZERO = lambda n: n(lambda x: Church_False)(Church_True)

FACT_ = lambda n: n(lambda u: MULT(n)(FACT_(PRED(n))))(Church_1)

# Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))
# F = lambda g: lambda n: n(lambda u: MULT(n)(g(PRED(n))))(Church_1)
# FACT = Y(F)

T = lambda f: lambda x: f(f)(x)
G = lambda g: lambda n: n(lambda u: MULT(n)(g(g)(PRED(n))))(Church_1)
FACT = T(G)


factorial = (lambda a:lambda v:a(a)(v))(lambda s: lambda x:1 if x==0 else x*s(s)(x-1))

