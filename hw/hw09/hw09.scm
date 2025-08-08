(define (curry-cook formals body) 
        (define (f formals)
        (if  (null?  formals)
             body
             (list 'lambda  (list (car formals)) (f (cdr formals)))))
        (f formals)     
)

(define (curry-consume curry args)
        (if  (null?  (cdr args))
             (curry (car args))
             (curry-consume (curry (car args)) (cdr args)))
)

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons 'cond
        (map (lambda (option)
               (cons  (car (cdr switch-expr)) (cdr option )(cdr option))
             (car (cdr (cdr switch-expr)))))))
