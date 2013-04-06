import Data.List
import qualified Data.Map as Map
import Data.Maybe

cubes :: [Integer]
cubes = [x^3 | x <- [1..]]

problem62 :: Integer
problem62 = problem62' cubes Map.empty
    where
        problem62' (p:pt) cubeMap
            | (Map.member key cubeMap) &&
              (length cubeList) == 5        = head $ sort cubeList
            | otherwise                     = problem62' pt (Map.insert key cubeList cubeMap)
            where
                key = sort (show p)
                cubeList = p : (fromMaybe [] (Map.lookup key cubeMap))

main = print (problem62)
