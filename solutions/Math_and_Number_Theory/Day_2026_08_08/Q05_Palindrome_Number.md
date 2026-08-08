# Palindrome Number

## Problem Statement
Given a non-negative integer, determine if it is a palindrome. A palindrome is a number or a text phrase that reads the same backwards as forwards. For example, "12321" is a palindrome number, but "123456" is not. The input will be a 32-bit signed integer, and the output should be a boolean value indicating whether the number is a palindrome or not. The constraints are: the input integer will be in the range [-2^31, 2^31 - 1].

## Approach
To solve this problem, we can convert the integer to a string and compare it with its reverse. Alternatively, we can also solve this problem mathematically by reversing the number and comparing it with the original number. This approach avoids the need for string conversion and is more efficient.

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
        // If x is negative, it cannot be a palindrome
        if (x < 0) return false;
        
        // Initialize variables to store the reversed number
        int reversed = 0;
        int original = x;
        
        // Reverse the number
        while (x != 0) {
            reversed = reversed * 10 + x % 10;
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

Input: -121
Output: false

Input: 10
Output: false
```

## Key Takeaways
- We should handle the case where the input number is negative separately, as negative numbers cannot be palindromes.
- The time complexity of this solution is O(log(n)), where n is the input number, because we are effectively iterating over the digits of the number.
- The space complexity is O(1), as we are only using a constant amount of space to store the reversed number and the original number.