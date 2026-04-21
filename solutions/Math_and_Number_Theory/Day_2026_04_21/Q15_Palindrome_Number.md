# Palindrome Number

## Problem Statement
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise. A palindrome is a number or a text phrase that reads the same backwards as forwards. For example, "12321" is a palindrome number. The input will be a 32-bit signed integer. If `x` is negative, it cannot be a palindrome because of the negative sign.

## Approach
The algorithm checks if the integer is negative and returns false if so. Then it reverses the integer and checks if it's equal to the original number. This approach works because a palindrome number reads the same forwards and backwards.

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
        // If x is negative, it's not a palindrome
        if (x < 0) return false;
        
        // Convert integer to string to easily reverse it
        string str = to_string(x);
        string rev = str;
        reverse(rev.begin(), rev.end());
        
        // Check if the string is equal to its reverse
        return str == rev;
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
- Always consider the constraints of the problem, such as the 32-bit signed integer constraint in this case.
- Negative numbers cannot be palindromes due to the negative sign.
- There are multiple approaches to solve this problem, including converting the integer to a string, reversing the integer mathematically, or using a two-pointer technique.