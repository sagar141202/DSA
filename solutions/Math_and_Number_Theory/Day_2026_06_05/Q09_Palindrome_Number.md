# Palindrome Number

## Problem Statement
Given a non-negative integer, determine whether it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input integer will be between 0 and 2^31 - 1.

## Approach
To solve this problem, we can convert the integer into a string and compare it with its reverse. Alternatively, we can use mathematical operations to reverse the integer and compare it with the original number. We will use the latter approach to avoid string conversion.

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
        // if x is negative, it cannot be a palindrome
        if (x < 0) return false;
        
        // initialize variables to store the reversed number
        int reversed = 0;
        int original = x;
        
        // reverse the number
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // compare the reversed number with the original number
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
```

## Key Takeaways
- We can solve this problem without converting the integer to a string.
- The time complexity is O(log n) because we are reversing the number digit by digit.
- The space complexity is O(1) because we are using a constant amount of space to store the reversed number and the original number.