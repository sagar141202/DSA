# Palindrome Number

## Problem Statement
Given a non-negative integer, determine if it is a palindrome. A palindrome number is a number that remains the same when its digits are reversed. For example, 12321 is a palindrome number, but 123456 is not. The input integer will be in the range [0, 2^31 - 1]. The function should return true if the number is a palindrome and false otherwise.

## Approach
The approach to solve this problem is to convert the integer into a string and then compare it with its reverse. Alternatively, we can also reverse the integer without converting it to a string by using mathematical operations. We will use the latter approach to avoid string operations.

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
        // if the number is negative, it's not a palindrome
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
        
        // check if the reversed number is equal to the original
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
- We can reverse an integer without converting it to a string by using the modulo operator to get the last digit and then appending it to the reversed number.
- We should handle negative numbers separately because they cannot be palindromes due to the negative sign.
- The time complexity of this solution is O(log(n)) because we are effectively removing one digit from the number in each iteration of the while loop.