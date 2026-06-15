# Palindrome Number

## Problem Statement
Given a non-negative integer, determine if it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input will be a 32-bit signed integer. If the input is negative, it is not a palindrome number.

## Approach
The algorithm will first check if the number is negative, in which case it is not a palindrome. Then, it will reverse the number and compare it with the original number to check if they are the same. This approach ensures that the function correctly identifies palindrome numbers.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // If the number is negative, it is not a palindrome
        if (x < 0) {
            return false;
        }
        
        // Initialize variables to store the reversed number
        int reversed = 0;
        int original = x;
        
        // Reverse the number
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // Check if the reversed number is the same as the original number
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
- Always check for negative numbers first, as they cannot be palindromes.
- Reversing a number can be done by taking the remainder of the number when divided by 10 and adding it to the reversed number after shifting the digits to the left.
- Comparing the reversed number with the original number is the final step to determine if the number is a palindrome.