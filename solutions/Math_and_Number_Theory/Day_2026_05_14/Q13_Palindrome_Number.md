# Palindrome Number

## Problem Statement
Given a non-negative integer, determine whether it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome, but 123 is not. The input integer will be in the range [0, 2^31 - 1]. The solution should return true if the number is a palindrome and false otherwise.

## Approach
The approach to solve this problem is to convert the integer into a string and then compare it with its reverse. Alternatively, we can also reverse the integer mathematically without converting it to a string. We will use the mathematical approach to solve this problem.

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
- We can solve this problem by reversing the integer mathematically without converting it to a string.
- We need to handle the case where the input integer is negative, as negative numbers cannot be palindrome.
- The time complexity of the solution is O(log(n)) because we are reversing the integer digit by digit.