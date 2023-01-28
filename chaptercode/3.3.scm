(define (even-subsets s)
  (if (null? s) nil
    (append (even-subsets (cdr s))
      (map (lambda (t) (cons (car s) t))
        (if (even? (car s))
          (even-subsets (cdr s))
          (odd-subsets (cdr s))))
        (if (even? (car s)) (list (list (car s))) nil))))
        
(define (odd-subsets s)
  (if (null? s) nil
    (append (odd-subsets (cdr s))
      (map (lambda (t) (cons (car s) t))
        (if (odd? (car s))
          (even-subsets (cdr s))
          (odd-subsets (cdr s))))
        (if (odd? (car s)) (list (list (car s))) nil))))


(define (even-subsets s)
  (if (null? s) nil
    (append (even-subsets (cdr s))
            (subset-helper even? s))))

(define (odd-subsets s)
  (if (null? s) nil
    (append (odd-subsets (cdr s))
            (subset-helper odd? s))))

(define (subset-helper f s)
  (append
      (map (lambda (t) (cons (car s) t))
        (if (f (car s))
          (even-subsets (cdr s))
          (odd-subsets (cdr s))))
      (if (f (car s)) (list (list (car s))) nil)))