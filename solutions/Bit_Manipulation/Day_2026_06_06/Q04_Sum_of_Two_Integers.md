# Sum of Two Integers

## Problem Statement
Given two integers `a` and `b`, find their sum without using the arithmetic operators `+` and `-`. The integers can be positive, negative, or zero, and the sum should be calculated using only bit manipulation operations. For example, if `a = 1` and `b = 2`, the output should be `3`. If `a = -1` and `b = 2`, the output should be `1`.

## Approach
The approach is to use bitwise XOR (`^`) to find the sum of `a` and `b` without considering the carry, and then use bitwise AND (`&`) to find the carry. The process is repeated until there is no carry left.

## Complexity
- Time: O(log(max(a, b)))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int getSum(int a, int b) {
        // If b is 0, return a
        if (b == 0) return a;
        // Calculate the sum without considering the carry using XOR
        int sum = a ^ b;
        // Calculate the carry using AND and left shift
        int carry = (a & b) << 1;
        // Recursively call the function with the sum and carry
        return getSum(sum, carry);
    }
};

int main() {
    Solution solution;
    int a = 1, b = 2;
    cout << "Sum: " << solution.getSum(a, b) << endl;
    return 0;
}
```

## Test Cases
```
Input: a = 1, b = 2
Output: 3
Input: a = -1, b = 2
Output: 1
Input: a = 0, b = 0
Output: 0
```

## Key Takeaways
- Bitwise XOR (`^`) can be used to find the sum of two numbers without considering the carry.
- Bitwise AND (`&`) can be used to find the carry.
- The process of calculating the sum and carry should be repeated until there is no carry left.