# Palindrome Number

## Problem Statement
Given an integer `x`, determine if it is a palindrome number, which means it remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input integer `x` will be in the range `-2^31 <= x <= 2^31 - 1`. If `x` is a palindrome number, return `true`; otherwise, return `false`. 

## Approach
The algorithm involves converting the integer into a string and comparing it with its reverse. If they are the same, the number is a palindrome. Alternatively, we can also reverse the integer mathematically without converting it to a string.

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
- We can solve this problem by converting the integer to a string or by reversing the integer mathematically.
- Negative numbers cannot be palindrome because of the negative sign.
- The time complexity is O(log(n)) because we are processing each digit of the integer once.