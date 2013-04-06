import Data.Char (digitToInt)
import qualified Data.Map as Map

factorial :: Int -> Int
factorial n = foldl (*) 1 [1..n]

recomp :: Int -> Int
recomp n = foldl (+) 0 [(factorial (digitToInt x)) | x <- show n]

steps :: Int -> Int
steps x
    | x == 169          = 3
    | x == 363601       = 3
    | x == 1454         = 3
    | x == 871          = 2
    | x == 45361        = 2
    | x == 872          = 2
    | x == 45362        = 2
    | n == x            = 1
    | otherwise         = 1 + (steps n)
    where n = recomp x

main :: IO ()
-- This could be sped up by saving the intermediate steps in a hash
main = print (sum [1 | x <- [1..1000000], (steps x) == 60])
