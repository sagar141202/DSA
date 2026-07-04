# Reverse Integer

## Problem Statement
The problem requires writing a function that takes a 32-bit signed integer as input and returns the integer with its digits reversed. If the reversed integer overflows, the function should return 0. For example, given the input 123, the function should return 321. Given the input -123, the function should return -321. The input is assumed to be a 32-bit signed integer, meaning it is in the range [-2^31, 2^31 - 1].

## Approach
The algorithm involves converting the integer into a string, reversing the string, and then converting it back into an integer. We also need to handle the case where the reversed integer overflows. The function will use a simple iterative approach to reverse the integer.

## Complexity
- Time: O(log|x|)
- Space: O(log|x|)

## C++ Solution
```cpp
#include <climits>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        while (x != 0) {
            // Extract the last digit
            int digit = x % 10;
            // Append the digit to the result
            res = res * 10 + digit;
            // Remove the last digit from x
            x /= 10;
        }
        // Check for overflow
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
- Be careful with integer overflow when reversing the integer.
- Using a long long to store the reversed integer can help detect overflow.
- The time complexity is O(log|x|) because we are processing each digit of the input integer exactly once.