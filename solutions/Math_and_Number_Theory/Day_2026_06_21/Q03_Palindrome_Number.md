# Palindrome Number

## Problem Statement
Given an integer `x`, determine if it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input will be an integer, and the output should be a boolean value indicating whether the number is a palindrome or not. The constraints are that the input integer `x` will be within the range of -2^31 to 2^31 - 1.

## Approach
The approach to solve this problem is to convert the integer into a string, then compare the string with its reverse. If they are the same, the number is a palindrome. Alternatively, we can also solve this problem mathematically by reversing the number and comparing it with the original number.

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
        // Negative numbers cannot be palindrome
        if (x < 0) return false;
        
        // Convert the number to string
        string str = to_string(x);
        
        // Initialize two pointers
        int left = 0, right = str.size() - 1;
        
        // Compare characters from both ends
        while (left < right) {
            if (str[left] != str[right]) return false;
            left++;
            right--;
        }
        
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
- We can solve this problem by converting the number to a string and comparing it with its reverse.
- We can also solve this problem mathematically by reversing the number and comparing it with the original number.
- Negative numbers cannot be palindrome numbers because of the negative sign.