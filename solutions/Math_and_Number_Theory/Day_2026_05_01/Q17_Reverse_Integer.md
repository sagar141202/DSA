# Reverse Integer

## Problem Statement
The problem requires reversing a given 32-bit signed integer. The function should take an integer as input and return the reversed integer. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), the function should return 0. The input integer can be positive, negative, or zero. For example, if the input is 123, the output should be 321. If the input is -123, the output should be -321.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer. We also need to handle the case where the reversed integer overflows.

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
        long long res = 0; // use long long to handle overflow
        while (x != 0) {
            res = res * 10 + x % 10; // extract last digit and append to result
            x /= 10; // remove last digit
        }
        if (res > INT_MAX || res < INT_MIN) { // check for overflow
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
Input: 0
Output: 0
```

## Key Takeaways
- Use long long to handle potential overflow when reversing the integer.
- Check for overflow after reversing the integer by comparing it with INT_MAX and INT_MIN.
- The time complexity is O(log|x|) because we are processing each digit of the input integer once.