(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

(define (zip pairs)
  (define (ziper pair res)
    (cond
      ((null? pair) res)
      (else 
        (ziper (cdr pair) (list (append (car res) (list (caar pair))) (append (cadr res) (cdar pair))))
      )
    )
  )
  (ziper pairs '(nil nil))
)


;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (enum s n)
    (cond
    ((null? s) nil)
    (else
    (cons (cons n (cons (car s) nil)) (enum (cdr s) (+ n 1)))
    )))
    (enum s 0)
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (cond
    ((null? list1) list2)
    ((null? list2) list1)
    (else 
      (if (comp (car list1) (car list2)) 
        (cons (car list1) (merge comp (cdr list1) list2))
        (cons (car list2) (merge comp list1 (cdr list2)))
        )
    )
  )
)
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
  (define (getres s cur res)
    (cond
      ((null? s) res)
      ((null? (cdr s)) (append res (list (append cur s))))
      (else
        (if (<= (car s) (car (cdr s)))
          (getres (cdr s) (append cur (list (car s))) res)
          (getres (cdr s) nil (append res (cons (append cur (list (car s))) nil)))
        )
      )
    )
  )
  (getres s nil nil)
)
    ; END PROBLEM 17

;; Problem EC
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((quoted? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           ; note, form is lambda or define, you need to evaluate the body
           ; therefore, map let-to-lambda function to body
           (append (list form params) (map let-to-lambda body))
           ; END PROBLEM EC
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (define params (car (zip values)))
           (define args (map let-to-lambda (cadr (zip values))))
           (cons (append (list 'lambda params) (map let-to-lambda body)) args) 
           ; END PROBLEM EC
           ))
        (else
         ; BEGIN PROBLEM EC
         (map let-to-lambda expr)
         ; END PROBLEM EC
         )))

