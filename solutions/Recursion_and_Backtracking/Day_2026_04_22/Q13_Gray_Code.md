# Gray Code

## Problem Statement
The Gray Code is a sequence of binary numbers where only one bit is changed between each pair of successive numbers. Given a non-negative integer n, generate all the Gray Code sequences of length n. For example, if n = 2, the Gray Code sequences are ["00", "01", "11", "10"]. If n = 3, the Gray Code sequences are ["000", "001", "011", "010", "110", "111", "101", "100"]. The sequence should be in ascending order.

## Approach
The algorithm uses recursion and backtracking to generate all possible Gray Code sequences by changing one bit at a time. We start with the base case of n = 1 and then recursively generate the sequences for n > 1. The key insight is to reflect the sequences for n-1 and append 0 and 1 to generate the sequences for n.

## Complexity
- Time: O(2^n)
- Space: O(2^n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        for (int i = 0; i < (1 << n); i++) {
            result.push_back(i ^ (i >> 1));
        }
        return result;
    }
};
```

## Test Cases
```
Input: 2
Output: [0, 1, 3, 2]
Input: 3
Output: [0, 1, 3, 2, 6, 7, 5, 4]
```

## Key Takeaways
- The Gray Code sequence has a simple formula: `i ^ (i >> 1)`, where `i` is the decimal number and `^` is the bitwise XOR operator.
- The sequence can be generated iteratively without using recursion, making it more efficient for large inputs.
- The time complexity is exponential due to the nature of the Gray Code sequence, which has 2^n elements for n bits.