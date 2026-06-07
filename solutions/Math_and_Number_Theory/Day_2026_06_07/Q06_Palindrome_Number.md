# Palindrome Number

## Problem Statement
Given a non-negative integer, determine whether it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. The input will be a 32-bit signed integer, and the function should return true if the number is a palindrome and false otherwise. For example, 12321 is a palindrome number, but 123456 is not.

## Approach
The algorithm involves converting the number into a string and checking if it is the same when reversed. Alternatively, we can also solve this problem mathematically by comparing the first and last digits, then the second and second-to-last digits, and so on. We will use the mathematical approach to avoid string conversion.

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
Input: 12321
Output: true
Input: 123456
Output: false
Input: -12321
Output: false
```

## Key Takeaways
- We should always check for negative numbers first, as they cannot be palindrome.
- The mathematical approach is more efficient than converting the number to a string.
- We need to be careful when reversing the number to avoid overflow.