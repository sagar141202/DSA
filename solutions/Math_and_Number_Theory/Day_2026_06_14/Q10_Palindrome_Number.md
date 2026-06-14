# Palindrome Number

## Problem Statement
Given an integer `x`, determine if it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input `x` will be a 32-bit signed integer, and it can be negative. If `x` is negative, it cannot be a palindrome number because of the negative sign.

## Approach
The approach is to convert the integer into a string and compare it with its reverse. Alternatively, we can also extract the last digit of the number and compare it with the first digit, then move towards the center.

## Complexity
- Time: O(log(n))
- Space: O(log(n))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // if x is negative, it cannot be a palindrome
        if (x < 0) return false;
        
        // convert integer to string
        string str = to_string(x);
        
        // compare string with its reverse
        string rev = str;
        reverse(rev.begin(), rev.end());
        
        // return true if they are equal, false otherwise
        return str == rev;
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
- A negative number cannot be a palindrome number due to the negative sign.
- We can solve this problem by converting the integer to a string and comparing it with its reverse.
- Alternatively, we can extract the digits from the number and compare them from both ends towards the center.