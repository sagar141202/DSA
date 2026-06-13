# Reverse Integer

## Problem Statement
The problem requires reversing a given 32-bit signed integer. The function should take an integer as input and return the reversed integer. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), the function should return 0. For example, given the input 123, the function should return 321. Given the input -123, the function should return -321.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer. We also need to handle the case where the input integer is negative. The function will check for overflow before returning the result.

## Complexity
- Time: O(log(n))
- Space: O(log(n))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long res = 0; // Use long long to check for overflow
        int sign = (x < 0) ? -1 : 1;
        x = abs(x);
        while (x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        res *= sign;
        // Check for overflow
        if (res > INT_MAX || res < INT_MIN) {
            return 0;
        }
        return (int)res;
    }
};

int main() {
    Solution solution;
    cout << solution.reverse(123) << endl;  // Output: 321
    cout << solution.reverse(-123) << endl; // Output: -321
    cout << solution.reverse(120) << endl;  // Output: 21
    return 0;
}
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
- The function uses a while loop to reverse the integer.
- It checks for overflow by comparing the result with the maximum and minimum values of a 32-bit signed integer.
- The function handles negative integers by storing the sign separately and applying it to the result at the end.