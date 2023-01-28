(define (filter-lst fn lst)
  'YOUR-CODE-HERE
  (if (null? lst)
      nil
      (append 
        (if (fn (car lst))
            (list (car lst))
            nil
        )
        (filter-lst fn (cdr lst))
      )
  )
)

; ;; Tests
(define (even? x) (= (modulo x 2) 0))

(filter-lst even? '(0 1 1 2 3 5 8))

; expect (0 2 8)
(define (interleave first second) 
'YOUR-CODE-HERE
  (cond
    ((null? first) second)
    ((null? second) first)
    ((null? (cdr first)) (append first second))
    ((null? (cdr second)) (append (list (car first)) second (cdr first)))
    (else
      (append
        (list (car first))
        (list (car second))
        (interleave (cdr first) (cdr second)))))
)

(interleave (list 1 3 5) (list 2 4 6))

; expect (1 2 3 4 5 6)
(interleave (list 1 3 5) nil)

; expect (1 3 5)
(interleave (list 1 3 5) (list 2 4))

; expect (1 2 3 4 5)
(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (if (= n 0) start
    (accumulate combiner (combiner start (term n)) (- n 1) term))
)

(define (no-repeats lst) 
'YOUR-CODE-HERE
(if (null? lst) nil
(cons (car lst) 
  (no-repeats (filter-lst (lambda (x) (not (= x (car lst)))) lst)))))
