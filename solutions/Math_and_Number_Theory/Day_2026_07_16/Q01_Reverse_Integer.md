# Reverse Integer

## Problem Statement
The problem requires writing a function that takes a 32-bit signed integer as input and returns the integer obtained by reversing the order of its digits. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), the function should return 0. For example, given the input 123, the function should return 321. Given the input -123, the function should return -321. The input is assumed to be a valid 32-bit signed integer.

## Approach
The algorithm involves converting the integer into a string, reversing the string, and then converting it back into an integer. We also need to handle the case where the reversed integer overflows. This can be done by checking if the reversed integer is within the range of a 32-bit signed integer.

## Complexity
- Time: O(log|x|)
- Space: O(log|x|)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long res = 0; // use long long to avoid overflow
        while (x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        // check for overflow
        if (res > INT_MAX || res < INT_MIN) {
            return 0;
        }
        return (int)res;
    }
};
```

## Test Cases
```
Input: 123
Output: 321
Input: -123
Output: -321
Input: 120
Output: 21
Input: 1534236469
Output: 0
```

## Key Takeaways
- The key to this problem is to avoid overflow when reversing the integer.
- Using a long long data type can help avoid overflow when reversing the integer.
- Always validate the input and output to ensure they are within the expected range.