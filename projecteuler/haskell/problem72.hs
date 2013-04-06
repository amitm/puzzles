import Data.Numbers.Primes
import Data.List
import Data.Ratio

distinctPrimeFactors :: Int -> [Int]
distinctPrimeFactors n = (nub (factor primes n))
    where
        factor ps@(p:pt) x  | p*p > x       = [x]
                            | rem x p == 0  = p : factor ps (quot x p)
                            | otherwise     = factor pt x
totient :: Int -> Integer
totient 1 = 1
totient n = numerator ratio `div` denominator ratio
    where ratio = foldl (\acc x -> acc * (1 - (1 % (toInteger x))))
                        ((toInteger n) % 1) (distinctPrimeFactors n)

main = print (sum [(totient x) | x <- [2..1000000]])
