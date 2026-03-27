# Palindrome Number

## Problem Statement
Given an integer x, determine if it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input integer x will be between -2^31 and 2^31 - 1.

## Approach
The approach to solve this problem is to convert the integer into a string and then compare it with its reverse. Alternatively, we can also reverse the integer without converting it to a string by using arithmetic operations.

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
        // If x is negative, it's not a palindrome
        if (x < 0) return false;
        
        // Convert x to string to easily reverse it
        string str = to_string(x);
        string rev = str;
        reverse(rev.begin(), rev.end());
        
        // Compare the string with its reverse
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
- We can solve this problem by converting the integer to a string and then comparing it with its reverse.
- We can also solve this problem without converting the integer to a string by reversing the integer using arithmetic operations.
- The time complexity of this solution is O(log(n)) because the number of digits in the integer is proportional to the logarithm of the integer.