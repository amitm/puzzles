factorial :: Int -> Int
factorial n = foldl (*) 1 [1..n]

curiousSum :: Int -> Int -> Int
curiousSum start 0 = start
curiousSum start n = curiousSum (start + factorial (n `mod` 10)) (n `div` 10)

main :: IO ()
main = print (sum [x | x <- [3..100000], x == curiousSum 0 x])
