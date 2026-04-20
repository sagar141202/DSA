# XOR of all Numbers in Range

## Problem Statement
Given a range of integers from 0 to n (inclusive), find the XOR of all numbers in this range. The input n is a non-negative integer, and the output should be the XOR of all numbers from 0 to n. For example, if n = 3, the output should be 0 ^ 1 ^ 2 ^ 3 = 4, and if n = 5, the output should be 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1.

## Approach
The approach to solve this problem involves understanding the properties of XOR operation and identifying patterns in the XOR of numbers in a range. By analyzing the bits of the numbers, we can derive a formula to calculate the XOR of all numbers in the range. The key observation is that the XOR of all numbers from 0 to n can be calculated by considering the number of times each bit position is set in the numbers of the range.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorOfRange(int n) {
        // Calculate the XOR of all numbers in the range
        int xorResult = 0;
        for (int i = 0; i <= n; i++) {
            xorResult ^= i;
        }
        return xorResult;
    }
    
    // Optimized solution using bitwise operations
    int xorOfRangeOptimized(int n) {
        if (n % 4 == 0) return n;
        if (n % 4 == 1) return 1;
        if (n % 4 == 2) return n + 1;
        return 0;
    }
};
```

## Test Cases
```
Input: n = 3
Output: 4
Input: n = 5
Output: 1
Input: n = 7
Output: 7
```

## Key Takeaways
- The XOR operation has a property that `a ^ a = 0` and `a ^ 0 = a`, which can be used to simplify the calculation.
- The XOR of all numbers in a range can be calculated using bitwise operations and pattern observation.
- The optimized solution uses the fact that the XOR of all numbers in a range of length 4 is equal to the last number in the range.