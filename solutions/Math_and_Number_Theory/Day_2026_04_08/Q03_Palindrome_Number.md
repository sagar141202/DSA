# Palindrome Number

## Problem Statement
Given an integer `x`, determine if it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The function should return `true` if the number is a palindrome and `false` otherwise. The input integer `x` will be in the range `-2^31 <= x <= 2^31 - 1`.

## Approach
The approach is to convert the integer into a string, then compare the string with its reverse. If they are the same, the number is a palindrome. Alternatively, we can also reverse the integer mathematically by taking the last digit of the number in each step and appending it to the reversed number.

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
        // if x is negative, it cannot be a palindrome
        if (x < 0) return false;
        
        // initialize reversed number
        int reversed = 0;
        
        // store the original number
        int original = x;
        
        // reverse the number
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // check if the reversed number is the same as the original
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
- We can determine if a number is a palindrome by comparing the original number with its reverse.
- We can reverse a number by taking the last digit of the number in each step and appending it to the reversed number.
- Negative numbers cannot be palindromes because of the negative sign.