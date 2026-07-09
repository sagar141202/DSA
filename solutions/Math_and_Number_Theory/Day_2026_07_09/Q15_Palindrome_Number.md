# Palindrome Number

## Problem Statement
Given an integer `x`, determine if it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input `x` will be a 32-bit signed integer. If `x` is negative, it cannot be a palindrome number because of the negative sign. The function should return `true` if `x` is a palindrome number and `false` otherwise.

## Approach
To solve this problem, we can convert the integer into a string and then compare it with its reverse. Alternatively, we can reverse the integer mathematically by repeatedly taking the last digit and appending it to the result.

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
        // Negative numbers cannot be palindrome
        if (x < 0) return false;
        
        // Initialize variables to store the reversed number
        int reversed = 0;
        int original = x;
        
        // Reverse the number
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // Check if the reversed number is equal to the original number
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
- Always consider the edge case where the input number is negative.
- Be mindful of potential integer overflow when reversing the number.
- This problem can be solved using either a string-based approach or a mathematical approach.