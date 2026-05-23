# Palindrome Number

## Problem Statement
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise. A palindrome is a number or a text phrase that reads the same backwards as forwards. For example, "12321" is a palindrome number. The input will be a 32-bit signed integer. If the input number is negative, it cannot be a palindrome, so the function should return `false`. The constraints are: `-2^31 <= x <= 2^31 - 1`.

## Approach
To determine if a number is a palindrome, we can convert it to a string and compare it with its reverse. Alternatively, we can extract the digits of the number from right to left and compare them with the digits from left to right. We will use the latter approach for efficiency.

## Complexity
- Time: O(log(x))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // Negative numbers cannot be palindromes
        if (x < 0) return false;
        
        // Initialize variables
        int reversed = 0;
        int original = x;
        
        // Extract digits from right to left
        while (x != 0) {
            int digit = x % 10;
            reversed = reversed * 10 + digit;
            x /= 10;
        }
        
        // Compare the reversed number with the original
        return original == reversed;
    }
};
```

## Test Cases
```
Input: 121
Output: true
Input: -121
Output: false
Input: 10
Output: false
```

## Key Takeaways
- Be sure to handle negative numbers as they cannot be palindromes.
- The time complexity is O(log(x)) because we are processing each digit of the number once.
- The space complexity is O(1) as we are using a constant amount of space to store the reversed number and other variables.