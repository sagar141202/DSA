# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n (inclusive), find the XOR of all numbers in this range. The range is defined by a single integer n. For example, if n = 4, the XOR of all numbers in the range is 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4. The input n will be a non-negative integer.

## Approach
The XOR operation has the property that a ^ a = 0 and a ^ 0 = a. We can use this property to simplify the calculation. We can iterate over the range and XOR each number.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// solution with comments
class Solution {
public:
    int xorOperation(int n) {
        int result = 0;
        // iterate over the range
        for (int i = 0; i <= n; i++) {
            // XOR each number
            result ^= i;
        }
        return result;
    }
};
```

## Test Cases
```
Input: n = 4
Output: 4
Input: n = 5
Output: 1
```

## Key Takeaways
- The XOR operation can be used to find the parity of a set of numbers.
- The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which can be used to simplify calculations.
- This problem can be solved using a simple iterative approach with a time complexity of O(n).