# Reverse Integer

## Problem Statement
The problem requires reversing a given 32-bit integer. The integer can be positive or negative, and the reversed integer should also be a 32-bit integer. If the reversed integer overflows, the function should return 0. For example, given the integer 123, the function should return 321. Given the integer -123, the function should return -321.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and converting it back to an integer. We also need to handle the case where the reversed integer overflows. We can achieve this by checking if the reversed integer is within the range of a 32-bit integer.

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
- Always check for overflow when dealing with integers.
- Be mindful of the data type you are using to store the result.
- The while loop is used to extract each digit from the input number.