; First attempt at learning clojure If we list all the natural numbers below
; 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of  these
; multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

(defn prob1 [i, sum]
    (if (>= i 1000)
        sum
        (if (or (= (rem i 5) 0) (= (rem i 3) 0))
            (prob1 (+ i 1) (+ sum i))
            (prob1 (+ i 1) sum))))
;(println (prob1 3 0))

(defn prob2 []
    (defn fib [a b limit total testfn]
        (let [c (+ a b)]
            (if (> c limit)
                total
                (fib b c limit (+ total (testfn c)) testfn))))
    (fib 1 2 4000000 2 (fn [x] (if (= (rem x 2) 0) x 0))))

(defn prob25 []
    ((fn [a b]
        (let [c (+ a b)]
            (if (>= (count (str c)) 10)
                c
                (recur b c)))) 1 2))
            
;(println (prob2))
(println (prob25))
