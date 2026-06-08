# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, if `n = 5`, the binary representations are: `0 (0b0)`, `1 (0b1)`, `2 (0b10)`, `3 (0b11)`, `4 (0b100)`, `5 (0b101)`. The total number of set bits is `7`.

## Approach
The approach is to iterate over all numbers from 0 to `n` and use bit manipulation to count the number of set bits in each number. We can use the built-in `__builtin_popcount` function in C++ or implement our own function to count the set bits.

## Complexity
- Time: O(n log n)
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
            // Use __builtin_popcount to count the number of set bits
            count += __builtin_popcount(i);
        }
        return count;
    }
};

// Alternatively, we can implement our own function to count the set bits
class Solution {
public:
    int countBits(int n) {
        int count = 0;
        for (int i = 0; i <= n; i++) {
            int j = i;
            while (j) {
                count += j & 1;
                j >>= 1;
            }
        }
        return count;
    }
};
```

## Test Cases
```
Input: n = 5
Output: 7
Input: n = 10
Output: 17
```

## Key Takeaways
- We can use bit manipulation to count the number of set bits in a number.
- The `__builtin_popcount` function in C++ can be used to count the number of set bits in a number.
- We can also implement our own function to count the set bits using a while loop and bitwise operations.