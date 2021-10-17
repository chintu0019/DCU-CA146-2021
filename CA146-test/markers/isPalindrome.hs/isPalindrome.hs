-- isPalindrome xs indicates whether or not the list xs is a palindrome

isPalindrome :: [Int] -> Bool

isPalindrome []  = True
isPalindrome [_] = True
isPalindrome xs  = (head xs == last xs) && (isPalindrome (tail (init xs)))

