# Palindrome Number

## Problem Statement
Determine whether an integer is a palindrome. A palindrome is an integer that remains the same when its digits are reversed. The input will be a 32-bit signed integer. For example, input 121 is a palindrome, but input -121 is not.

## Approach
The approach is to reverse the integer and compare it with the original number. If they are equal, then the number is a palindrome. We can reverse the integer by taking the last digit of the number using the modulus operator and appending it to the reversed number.

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
        // handle negative numbers
        if (x < 0) return false;
        
        // initialize variables
        int reversed = 0;
        int original = x;
        
        // reverse the integer
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // compare the reversed number with the original
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
- To check if a number is a palindrome, we need to reverse the number and compare it with the original.
- We can reverse a number by taking the last digit of the number using the modulus operator and appending it to the reversed number.
- Negative numbers cannot be palindromes because of the negative sign.