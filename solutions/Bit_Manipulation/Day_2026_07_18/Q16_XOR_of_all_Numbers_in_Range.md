# XOR of all Numbers in Range

## Problem Statement
Given a range of integers from 0 to n (inclusive), find the XOR of all numbers in this range. The range is defined by a single integer n, where n is a non-negative integer. For example, if n = 3, the XOR of all numbers in the range is 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the XOR is 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4, since 4 is not included in the XOR operation due to its binary representation not contributing to the final result when XORed with other numbers.

## Approach
The algorithm uses the property of XOR that a ^ a = 0 and a ^ 0 = a. We can observe a pattern where the XOR of all numbers up to n depends on the last two bits of n. If the last two bits are 00, the XOR is n. If the last two bits are 01, the XOR is 1. If the last two bits are 10, the XOR is n + 1. If the last two bits are 11, the XOR is 0.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorOperation(int n) {
        if (n % 4 == 0) return n;
        else if (n % 4 == 1) return 1;
        else if (n % 4 == 2) return n + 1;
        else return 0;
    }
};
```

## Test Cases
```
Input: n = 3
Output: 4
Input: n = 4
Output: 4
Input: n = 5
Output: 1
```

## Key Takeaways
- The XOR operation has a cyclical pattern when applied to consecutive integers.
- The last two bits of n determine the result of the XOR operation.
- This problem can be solved in constant time using bitwise operations and pattern observation.