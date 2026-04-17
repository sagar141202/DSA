# Palindrome Number

## Problem Statement
Given an integer `x`, determine if it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input integer `x` will be in the range `-2^31 <= x <= 2^31 - 1`. If `x` is a palindrome number, return `true`; otherwise, return `false`.

## Approach
The approach to solve this problem is to convert the integer into a string and compare it with its reverse. If they are equal, then the number is a palindrome. Alternatively, we can also reverse the integer mathematically without converting it to a string.

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
        // If x is negative, it is not a palindrome
        if (x < 0) return false;
        
        int reversed = 0;
        int original = x;
        
        // Reverse the integer
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // Check if the reversed integer is equal to the original
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
- A palindrome number remains the same when its digits are reversed.
- We can solve this problem by converting the integer to a string and comparing it with its reverse, or by reversing the integer mathematically.
- The time complexity of the solution is O(log(n)) because we are reversing the integer, which takes logarithmic time.