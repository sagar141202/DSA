# Palindrome Number

## Problem Statement
Given a non-negative integer x, determine if it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input integer x will be in the range [0, 2^31 - 1]. We need to write a function that returns true if the number is a palindrome and false otherwise.

## Approach
The approach is to convert the integer into a string and then compare it with its reverse. Alternatively, we can also reverse the integer without converting it to a string by using mathematical operations. We will use the latter approach to avoid string conversion.

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
        // If x is negative, it's not a palindrome
        if (x < 0) return false;
        
        // Initialize variables to store the reversed number
        int reversed = 0;
        
        // Store the original number
        int original = x;
        
        // Reverse the number
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // Check if the reversed number is the same as the original
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
- We can reverse an integer without converting it to a string by using the modulus operator to get the last digit and integer division to remove the last digit.
- We should handle negative numbers as a special case since they cannot be palindromes.
- The time complexity of the solution is O(log(n)) because we are essentially counting the number of digits in the input number.