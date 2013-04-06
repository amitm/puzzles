hcf :: Int -> Int -> Int
hcf m 0 = m
hcf 0 n = n
hcf m n
    | m == n    = m
    | m > n     = hcf n (rem m n)
    | otherwise = hcf n m


problem73 :: Int -> Int
problem73 n =
    let bottom = 1 / 3
        top = 1 / 2
    in (sum [1 | x <- (counter 1 1 n),
                let n = (realToFrac (fst x)) / (realToFrac (snd x)),
                n >= bottom && n <= top])
    where
        counter :: Int -> Int -> Int -> [(Int, Int)]
        counter n d limit
            | n == d && n == limit      = []
            | n == d                    = (counter 1 (d + 1) limit)
            | (hcf n d) == 1            = (n, d) : (counter (n + 1) d limit)
            | otherwise                 = (counter (n + 1) d limit)

main = print ((problem73 12000) - 2)