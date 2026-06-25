# Reverse Integer

## Problem Statement
The problem requires reversing a 32-bit signed integer. Given an integer, reverse the digits and return the reversed integer. If the reversed integer overflows (is outside the range of a 32-bit signed integer), return 0. The input integer can be positive or negative. For example, given the integer 123, the reversed integer is 321. Given the integer -123, the reversed integer is -321. The integer can be in the range [-2^31, 2^31 - 1].

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer. We also need to handle the case where the reversed integer overflows. The solution will iterate over the input integer, appending each digit to a new integer while checking for overflow.

## Complexity
- Time: O(log|x|)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int reverse(int x) {
        long long res = 0; // Use long long to detect overflow
        while (x != 0) {
            res = res * 10 + x % 10; // Append the last digit of x to res
            x /= 10; // Remove the last digit of x
        }
        // Check for overflow
        if (res > INT_MAX || res < INT_MIN) {
            return 0;
        }
        return (int)res; // Cast res to int
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
- Use long long to detect overflow when reversing the integer.
- Handle the case where the input integer is negative by preserving the sign.
- Check for overflow after reversing the integer to ensure it is within the 32-bit signed integer range.