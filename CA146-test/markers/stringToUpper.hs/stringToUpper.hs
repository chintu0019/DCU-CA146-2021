import Data.Char(toUpper)

-- stringToUpper xs converts all lower case letters in the string xs to upper case

stringToUpper :: String -> String

stringToUpper []     = []
stringToUpper (x:xs) = (toUpper x):stringToUpper xs
