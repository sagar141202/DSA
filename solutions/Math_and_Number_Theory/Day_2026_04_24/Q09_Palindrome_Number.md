# Palindrome Number

## Problem Statement
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise. A palindrome is a number that reads the same backward as forward. For example, 121 is a palindrome while 123 is not. The input integer `x` will be in the range `-2^31 <= x <= 2^31 - 1`. 

## Approach
The approach is to reverse the integer and compare it with the original number. If they are the same, then the number is a palindrome. We can reverse the integer by taking the last digit of the number using the modulus operator and appending it to the reversed number.

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
        // negative numbers cannot be palindrome
        if (x < 0) return false;
        
        int reversed = 0;
        int original = x;
        
        // reverse the integer
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // check if the reversed integer is the same as the original
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
- We can solve this problem by reversing the integer and comparing it with the original number.
- Negative numbers cannot be palindrome because of the negative sign.
- The time complexity is O(log(n)) because we are iterating over the digits of the number, and the number of digits in a number `n` is `log(n)`.