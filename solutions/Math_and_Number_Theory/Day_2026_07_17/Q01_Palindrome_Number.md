# Palindrome Number

## Problem Statement
Given an integer `x`, determine if it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input integer `x` will be in the range `-2^31 <= x <= 2^31 - 1`. If `x` is a palindrome number, return `true`; otherwise, return `false`.

## Approach
The approach is to convert the integer into a string and compare it with its reverse. If they are the same, then the number is a palindrome. Alternatively, we can also reverse the integer mathematically without converting it to a string.

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
        // if x is negative, it's not a palindrome
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
- We can solve this problem by converting the integer into a string and comparing it with its reverse, or by reversing the integer mathematically.
- The time complexity of this solution is O(log(n)) because we are essentially counting the number of digits in the input number.
- The space complexity is O(1) because we are only using a constant amount of space to store the reversed number and the original number.