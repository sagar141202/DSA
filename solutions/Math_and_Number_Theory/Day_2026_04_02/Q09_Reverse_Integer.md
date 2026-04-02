# Reverse Integer

## Problem Statement
The problem requires reversing a given 32-bit signed integer. The function should take an integer as input, reverse its digits, and return the reversed integer. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), the function should return 0. For example, given the input 123, the function should return 321. Given the input -123, the function should return -321. The input integer can be in the range [-2^31, 2^31 - 1].

## Approach
The algorithm involves converting the integer to a string, reversing the string, and converting it back to an integer. We also need to handle overflow cases where the reversed integer exceeds the range of a 32-bit signed integer. The approach can be implemented using a simple loop that checks for overflow after each digit is processed.

## Complexity
- Time: O(log|x|) where x is the input integer, as the number of digits in x is proportional to log|x|.
- Space: O(log|x|) for storing the reversed integer as a string.

## C++ Solution
```cpp
#include <climits>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long res = 0; // using long long to handle overflow
        while (x) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        // check for overflow
        if (res > INT_MAX || res < INT_MIN) {
            return 0;
        }
        return res;
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
- Always consider potential overflows when working with integers, especially when reversing or manipulating large numbers.
- Using a long long data type can help detect potential overflows when the reversed integer exceeds the range of a 32-bit signed integer.
- The time complexity is logarithmic in the size of the input integer, as we process each digit once.