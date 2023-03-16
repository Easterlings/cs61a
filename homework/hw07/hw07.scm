(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ascending? asc-lst) 
    (
        if(> (length asc-lst) 1) 
        (
            if(> (car asc-lst) (cadr asc-lst)) 
                false
                (ascending? (cdr asc-lst))
        )
        true
    )
)

(define (square n) (* n n))

(define (pow base exp) 
    (
        if (= base 1)
        1
        (
            if(= exp 1)
            base
            (
                if (= (modulo exp 2) 0)
                    (square (pow base (/ exp 2)))
                    (* base (square (pow base (/ (- exp 1) 2))))
            )
        )
    )
)
