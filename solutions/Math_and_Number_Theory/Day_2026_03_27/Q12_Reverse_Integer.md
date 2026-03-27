# Reverse Integer

## Problem Statement
The problem requires reversing a 32-bit signed integer. Given an integer, the task is to reverse its digits while preserving the sign. For example, if the input is 123, the output should be 321. If the input is -456, the output should be -654. The reversed integer should be within the range of a 32-bit signed integer, i.e., between -2^31 and 2^31 - 1. If the reversed integer overflows, the function should return 0.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer while preserving the sign. Alternatively, it can be solved mathematically by continuously taking the last digit of the number and appending it to the reversed number.

## Complexity
- Time: O(log|x|)
- Space: O(1)

## C++ Solution
```cpp
#include <climits>
class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        while(x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        // check for overflow
        if(res > INT_MAX || res < INT_MIN) {
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
Input: -456
Output: -654
Input: 120
Output: 21
Input: 1534236469
Output: 0
```

## Key Takeaways
- Always consider the case of integer overflow when dealing with 32-bit integers.
- Be mindful of the sign of the input integer when reversing it.
- Use of long long data type helps in checking for overflow before casting back to int.