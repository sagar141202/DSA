# Palindrome Number

## Problem Statement
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise. A palindrome is a number or a text phrase that reads the same backwards as forwards. For example, "121" is a palindrome, while "123" is not. Assume that the input is a 32-bit signed integer. If the input is negative, it cannot be a palindrome because of the negative sign, so return `false` for negative inputs.

## Approach
The approach is to convert the integer into a string and then compare it with its reverse. Alternatively, we can also solve this problem mathematically by reversing the integer and comparing it with the original number.

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
        // If x is negative, it cannot be a palindrome
        if (x < 0) return false;
        
        // Convert the integer into a string
        string str = to_string(x);
        
        // Initialize two pointers, one at the start and one at the end of the string
        int left = 0, right = str.size() - 1;
        
        // Compare characters from the start and end, moving towards the center
        while (left < right) {
            if (str[left] != str[right]) return false;
            left++;
            right--;
        }
        
        // If the loop completes without finding any mismatches, the number is a palindrome
        return true;
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
- To check if an integer is a palindrome, we can convert it into a string and compare it with its reverse.
- Alternatively, we can reverse the integer mathematically by repeatedly taking the last digit and appending it to the reverse, then removing the last digit from the original number.
- We should handle the case where the input is negative separately, as negative numbers cannot be palindromes due to the negative sign.