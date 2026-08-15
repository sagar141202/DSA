# Palindrome Number

## Problem Statement
A palindrome number is a number that remains the same when its digits are reversed. Given a non-negative integer, determine if it is a palindrome number or not. The integer can be very large and may not fit in the memory. The constraints are: the input integer is non-negative, and the input integer can be very large.

## Approach
The approach to solve this problem is to convert the integer to a string and then compare it with its reverse. Alternatively, we can also solve this problem without converting the integer to a string by reversing the integer and comparing it with the original number.

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
        // Handle negative numbers
        if (x < 0) return false;
        
        // Initialize variables
        int reversed = 0;
        int original = x;
        
        // Reverse the number
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // Compare the reversed number with the original number
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
- A palindrome number remains the same when its digits are reversed.
- We can solve this problem by converting the integer to a string and comparing it with its reverse, or by reversing the integer and comparing it with the original number.
- The time complexity of this problem is O(log(n)) because we are iterating over the digits of the number, and the space complexity is O(1) because we are using a constant amount of space.