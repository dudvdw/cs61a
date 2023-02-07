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


#### Tail recursion
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


#### Macro
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


## How to Design Programs
* From Problem Aanlysis to Data Definitions

* Signature, Purpose Statement, Header

* Functional Examples

* Function Template

* Testing


## Summary
### What Do You Learn From CS61A ?
I have learned programming for a long time. At first, I searched information about 「How to learn Computer Science？」. There are so many answers on the website.
After summarising these information, I tried to learn the core courses on the syllabus of some famous university. I started learning from *Mathematical Logic*, *Digital Circuit*, *Analog Circuit*......, reading books recommended on the website, such as *Discrete Mathematics and Its Applications*, *Computer Organization and Design: The Hardware/Software Interface*, *Computer Systems: A Programmer's Perspective*, *Computer Networking: A Top-Down Approach*, *Algorithm*, *Introduction to Algorithms*, *Modern Operating Systems*, *Thinking in Java*......, and many books I can not remember their names now. However, I still remember these days that I learned Python from the website, learned Java following *Java: The Complete Reference* on the notepad in Windows7 system. I got up early to read some books before the course, wrote code under the instruction of books or website in spare time. The process of learning by oneself was alone and boring, but I kept moving without hesitation. I knew I would approach the goal a bit after reading some pages of books, writing some lines of codes.

Paying lots of efforts on studying CS by myself, whereas the result is not proportional with it. Why? I didn't know at that moment, maybe I had no gift on programming, I thought. However, I like learning new things, I have strong curiosity to make sense of those problems. But I felt confused at that time.

Later, I found that many programmers didn't learn a lot at school, they learned more after they started to work or attended the training institutions. At that moment, I realized one can learn more from project than school or books. 

After taking this course, I find I make mistake about learning.

Knowledge and application are two important notions when we talk about learning. If you study by yourself, you obtain knowledge from books, or website. When you write code under the instruction of these materials, you try to transfer those knowledge to practice. If you study this major at school, there is one more procedure -- exam. Although you get a good grade on the examination, you merely know some basic syntax, or build a simple administrative system of book-database.
All of these process of learning miss a key procedure -- application. When you complete project in your job, you try to use knowledge to solve so many problems, not merely simple practice. It is a process of applying knowledge, pushing you to learn it well. You may grow rapidly by this project-oriented learning method, but it has obvious defect -- it is not systematic. It denotes you learn things randomly, leading by projects in your work. That is a disadvantage for you to form a relatively integrated knowledge system, resulting in hardly transfer to another unfamiliar project rapidly.

There are four primary procedures in the process of learning:
* Learn  
**aim**: obtain knowledge  
**method**: read text/books, watch video

* Examine
**aim**: consolidate knowledge  
**method**: do homework, attend exam

* Exercise 
**aim**: obtain skill  
**method**: do exercise/lab

* Apply  
**aim**: obtain and consolidate skill  
**method**: complete project

Make a plan, set a deadline, complete it in sequence, you will approach the goal step by step. Keep moving!

## Life Advise
Don't Compare.
  -- Professor John DeNero

The best state of one is that he/she feels confident on his/her body and mind. And he/she likes the satisfied state at this moment which comes from the heart, not origins from comparing with others.