# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, if `n = 5`, the binary representations are: `0 (0b0)`, `1 (0b1)`, `2 (0b10)`, `3 (0b11)`, `4 (0b100)`, `5 (0b101)`. The total number of set bits is `0 + 1 + 1 + 2 + 1 + 2 = 7`.

## Approach
The approach is to iterate over all numbers from 0 to `n` and for each number, count the number of set bits using bit manipulation. We can use the built-in `__builtin_popcount` function in C++ or implement our own function using bit manipulation.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            // count the number of set bits in i
            result[i] = result[i >> 1] + (i & 1);
        }
        return result;
    }
};
```

## Test Cases
```
Input: n = 5
Output: [0,1,1,2,1,2]
```

## Key Takeaways
- The `>>` operator is used for right shift, which is equivalent to dividing the number by 2.
- The `&` operator is used for bitwise AND, which is used to check if a bit is set.
- The `__builtin_popcount` function can be used to count the number of set bits in a number, but it's not necessary in this case.