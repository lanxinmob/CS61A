scm>  (define with-list
...>          (list (list 'a 'b ) 'c  'd  (list  'e)  ) )
with-list
scm> (draw with-list)

scm>  (define with-list
...>           '((a b ) c  d  (e)  ) )
with-list
scm> (draw with-list)

scm>  (define with-list
...>          (cons 
                   (cons 'a (cons 'b nil )) 
                   (cons 'c  (cons 'd  (cons (cons 'e nil) nil ) ))
               ))
with-list
scm> (draw with-list)