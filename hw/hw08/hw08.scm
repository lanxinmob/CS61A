(define (ascending? s) 
        (if (or (null? s) (null? (cdr s)) )
           #t
        (if (<= (car s) (car(cdr s)))
           (ascending? (cdr s))
           #f))
)

(define (my-filter pred s) 
        (if (or (null? s))
            s
        (if (pred (car s))
            (cons (car s)(my-filter pred (cdr s)))
            (my-filter pred (cdr s))
            ))
)

(define (interleave lst1 lst2) 
        (cond  ((null? lst2) lst1) 
               ((null? lst1) lst2)
               (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2))))))
)

(define (no-repeats s)
        (if (null? s)s
            (cons (car s)
            (no-repeats (filter (lambda (x) (not(= (car s) x)))(cdr s)))))
)
