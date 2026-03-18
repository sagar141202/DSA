# Reverse Integer

## Problem Statement
The problem requires writing a function that takes a 32-bit signed integer as input and returns the integer obtained by reversing the order of its digits. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), the function should return 0. For example, the reverse of 123 is 321, and the reverse of -456 is -654. The input integer can be any 32-bit signed integer, and the function should handle both positive and negative integers.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer. We also need to handle the sign of the integer and check for overflow.

## Complexity
- Time: O(log|x|)
- Space: O(log|x|)

## C++ Solution
```cpp
#include <climits>
class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        while(x) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        return (res > INT_MAX || res < INT_MIN) ? 0 : res;
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
- We use a long long to store the reversed integer to check for overflow.
- The time complexity is O(log|x|) because we are processing each digit of the input integer once.
- The space complexity is O(log|x|) because in the worst case, we might need to store all the digits of the input integer in the result.