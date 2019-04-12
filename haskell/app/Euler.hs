module Nums where

multipleSum :: Int -> Int -> Int
multipleSum currentNumber total =
    if currentNumber == 0
        then total
        else if mod currentNumber 3 == 0 || mod currentNumber 5 == 0
            then multipleSum (currentNumber - 1) (total + currentNumber)
            else multipleSum (currentNumber - 1) total

