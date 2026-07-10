# Reverse Integer

## Problem Statement
The problem requires writing a function that takes a 32-bit signed integer as input and returns the integer obtained by reversing the order of its digits. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), the function should return 0. For example, the reverse of 123 is 321, and the reverse of -456 is -654. The input is assumed to be a valid 32-bit signed integer.

## Approach
The algorithm involves converting the integer into a string, reversing the string, and then converting it back into an integer. We also need to handle the case where the reversed integer overflows. The function will check for overflow by comparing the reversed integer with the maximum and minimum 32-bit signed integer values.

## Complexity
- Time: O(log|x|)
- Space: O(log|x|)

## C++ Solution
```cpp
#include <climits>
class Solution {
public:
    int reverse(int x) {
        long long res = 0; // using long long to handle potential overflow
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
Input: -456
Output: -654
Input: 1534236469
Output: 0
```

## Key Takeaways
- We use a long long data type to handle potential overflow when reversing the integer.
- The time complexity is O(log|x|) because we are processing each digit of the input integer exactly once.
- The space complexity is also O(log|x|) due to the space required to store the reversed integer.