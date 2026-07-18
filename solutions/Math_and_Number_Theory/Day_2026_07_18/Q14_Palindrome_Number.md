# Palindrome Number

## Problem Statement
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise. A palindrome is a number that reads the same backward as forward. For example, 121 is a palindrome while 123 is not. The input will be a 32-bit signed integer, and the output will be a boolean value. Constraints: `-2^31 <= x <= 2^31 - 1`.

## Approach
The algorithm involves converting the integer into a string and comparing it with its reverse. Alternatively, we can also reverse the integer mathematically and compare it with the original number. This approach ensures an efficient solution with minimal computational overhead. We will use the mathematical reversal approach for its efficiency and accuracy.

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
        // Negative numbers cannot be palindrome
        if (x < 0) return false;
        
        // Initialize variables
        int reversed = 0;
        int original = x;
        
        // Reverse the integer
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // Compare the reversed with the original
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

Input: -121
Output: false
```

## Key Takeaways
- Always consider the sign of the number when determining if it's a palindrome.
- Reversing the integer mathematically is more efficient than converting it to a string.
- The time complexity of this solution is O(log(n)) because we are effectively iterating over the digits of the number.