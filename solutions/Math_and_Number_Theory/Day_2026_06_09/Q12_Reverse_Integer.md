# Reverse Integer

## Problem Statement
The problem requires reversing a given 32-bit signed integer. The function should take an integer as input and return the reversed integer. If the reversed integer overflows (is outside the range of a 32-bit signed integer), the function should return 0. For example, given the input 123, the function should return 321. Given the input -123, the function should return -321. The input is assumed to be a 32-bit signed integer.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and converting it back to an integer. It also involves checking for overflow by comparing the reversed integer with the maximum and minimum 32-bit signed integer values.

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
        long long res = 0; // using long long to check for overflow
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
- The problem can be solved by converting the integer to a string, reversing the string, and converting it back to an integer, but a more efficient approach is to use the modulo operator to extract the last digit and append it to the result.
- Checking for overflow is crucial in this problem, as the reversed integer may exceed the range of a 32-bit signed integer.
- Using a long long data type to store the result helps in checking for overflow.