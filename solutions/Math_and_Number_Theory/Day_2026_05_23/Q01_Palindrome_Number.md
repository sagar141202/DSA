# Palindrome Number

## Problem Statement
Determine whether an integer is a palindrome. A palindrome is an integer that remains the same when its digits are reversed. The input integer will be between -2^31 and 2^31 - 1. For example, 121 is a palindrome, while 123 is not. The function should return true if the integer is a palindrome and false otherwise.

## Approach
The algorithm checks if the input number is negative, in which case it's not a palindrome. Then it reverses the number and checks if it's equal to the original. This is done by taking the last digit of the number using the modulus operator and appending it to the reversed number.

## Complexity
- Time: O(log(n))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // if the number is negative, it's not a palindrome
        if (x < 0) return false;
        
        // store the original number
        int original = x;
        
        // initialize the reversed number
        int reversed = 0;
        
        // reverse the number
        while (x != 0) {
            // get the last digit
            int digit = x % 10;
            
            // append the digit to the reversed number
            reversed = reversed * 10 + digit;
            
            // remove the last digit from the original number
            x /= 10;
        }
        
        // check if the reversed number is equal to the original
        return original == reversed;
    }
};
```

## Test Cases
```
Input: 121
Output: true
Input: 123
Output: false
Input: -121
Output: false
```

## Key Takeaways
- Check for negative numbers first, as they cannot be palindromes.
- Reversing the number can be done by taking the last digit using the modulus operator and appending it to the reversed number.
- The time complexity is O(log(n)) because we are iterating over the digits of the number, and the number of digits is proportional to the logarithm of the number.