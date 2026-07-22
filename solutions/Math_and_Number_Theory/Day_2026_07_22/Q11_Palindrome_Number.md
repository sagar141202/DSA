# Palindrome Number

## Problem Statement
Given an integer `x`, determine if it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The function should return `true` if the number is a palindrome and `false` otherwise. The input integer `x` will be in the range `-2^31 <= x <= 2^31 - 1`.

## Approach
The algorithm involves converting the integer into a string and then comparing it with its reverse. Alternatively, we can also reverse the integer mathematically by taking the remainder of the number when divided by 10 and appending it to the reversed number.

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
        
        int reversed = 0;
        int original = x;
        
        // Reverse the integer
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // Check if the reversed integer is the same as the original
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
- To check if a number is a palindrome, we can reverse the number and compare it with the original.
- We can reverse an integer mathematically without converting it to a string.
- Negative numbers cannot be palindrome numbers because of the negative sign.