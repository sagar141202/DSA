# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, if `n = 5`, the binary representations are: `0 (0b0)`, `1 (0b1)`, `2 (0b10)`, `3 (0b11)`, `4 (0b100)`, `5 (0b101)`. The total number of set bits is `0 + 1 + 1 + 2 + 1 + 2 = 7`.

## Approach
The approach is to iterate over all numbers from 0 to `n` and use bit manipulation to count the number of set bits in each number. We will use the built-in `__builtin_popcount` function in C++ to count the number of set bits.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countBits(int n) {
        int count = 0;
        for (int i = 0; i <= n; i++) {
            // __builtin_popcount returns the number of set bits in i
            count += __builtin_popcount(i);
        }
        return count;
    }
};
```

## Test Cases
```
Input: n = 5
Output: 7
Input: n = 15
Output: 22
```

## Key Takeaways
- The `__builtin_popcount` function is used to count the number of set bits in a given integer.
- This solution has a time complexity of O(n) because we are iterating over all numbers from 0 to `n`.
- The space complexity is O(1) because we are using a constant amount of space to store the count of set bits.