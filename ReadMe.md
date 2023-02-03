# CS 61A Note

## Chapter 1
***Tips:***
> Sometimes, it will take you a long time to solve one problem. Don't be upset, it's normal and worthy. The ability of solving problem by yourself is a core skill you have to gain in the process of learning coding.
> Learning slowly is the best and fast way to learn. You will learn fast after you have obtained necessary knowledge and skill in the former slow learning process.


## Chapter 2
### 2.2 Data Abstraction
In general, we can express abstract data using a collection of selectors and constructors, together with some behavior conditions. As long as the behavior conditions are met (such as the division property above), the selectors and constructors constitute a valid representation of a kind of data. The implementation details below an abstraction barrier may change, but if the behavior does not, then the data abstraction remains valid, and any program written using this data abstraction will remain correct.

***Tips:***
> Debugging is twice as hard as coding. A complex and long code is more easily to debug than an elegant and brief one. Therefore, you should write a version of understandable code first, then try to enable it more elegant.

## Chapter 3
### 3.2 Functional Programming
The machine-language programmer is concerned with using the given hardware to erect systems and utilities for the efficient implementation of resource-limited computations. 
High-level languages, erected on a machine-language substrate, hide concerns about the representation of data as collections of bits and the representation of programs as sequences of primitive instructions. 

**Scheme interpreter**
* When you install a Scheme interpreter, you may come across some problems. Using the Scheme interpreter in [hw06](https://inst.eecs.berkeley.edu/~cs61a/fa20/hw/hw06/) is a better choice.
* Or you can use the scheme interpreter [here](https://code.cs61a.org/)

#### Scheme Lists
In the late 1950s, computer scientists used confusing names
* cons: Two-argument procedure that creates a linked list
* car: Procedure that returns the first element of a list
* cdr: Procedure that returns the rest of a list
* nil: The empty list

**Important!**
Scheme lists are written in parentheses with elements separated by spaces

**Built-in List Processing Procedures**
(append s t ): list the elements of s and t; append can be called on more than 2 lists
(map f s): call a procedure f on each element of a list s and list the results
(filter f s): call a procedure f on each element of a list s and list the elements for
which a true value is the result
(apply f s): call a procedure f with the elements of a list as its arguments

**Quotation**
'<expression> is shorthand for (quote <expression>).
  (quote (1 2)) is equivalent to '(1 2)

**Lambda Expression**
``` scheme
  (lambda (<formal-parameters>) <body>)
```

**Tail recursion**
Tail recursion is defined as a recursive function in which the recursive call is the last statement that is executed by the function. So basically nothing is left to execute after the recursion call.

*Examples:*
* factorial's tail recursion version
``` scheme
(define (fac n k)
  (if (zero? n) k
  (fac (- n 1) (* n k))))
```
* reverse a list
``` scheme
(define (reverse s)
  (define (reverse-iter s r)
    (if (null? s) r
    (reverse-iter (cdr s) (cons (car s) r))))
  (reverse-iter s nil))
```

**Macro**
``` scheme
(define-macro (twice expr)
 (list 'begin expr expr))

(twice (print 2))
```

``` scheme
(define (twice expr) (list 'begin expr expr))

(eval (twice '(print 2)))
```

``` scheme
(define-macro (check expr)
  (list 'if expr ''passed
    (list 'quote (list 'failed: expr))))

(check (> x 0))
```

``` scheme
(define (map fn vals)
  (if (null? vals) nil
    (cons (fn (car vals))
      (map fn (cdr vals)))))

(define-macro (for sym vals expr)
  (list 'map (list 'lambda (list sym)  expr) vals))

(for x '(1 2 3 4) (* x x))
```