# Counting Bits

## Problem Statement
Given a non-negative integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, given `n = 5`, the binary representations are `0 (0b0)`, `1 (0b1)`, `2 (0b10)`, `3 (0b11)`, `4 (0b100)`, and `5 (0b101)`. The total number of set bits is `0 + 1 + 1 + 2 + 1 + 2 = 7`. The function should return this total count. The input `n` will be in the range `[0, 10^9]`.

## Approach
The approach involves iterating over all numbers from 0 to `n` and for each number, counting the number of set bits using bit manipulation. We utilize the built-in `__builtin_popcount` function in C++ to count the number of set bits in a number. Alternatively, we can also use bitwise operations to achieve this.

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
            // Using __builtin_popcount to count set bits
            count += __builtin_popcount(i);
        }
        return count;
    }
};

// Alternatively, without using __builtin_popcount
class Solution {
public:
    int countBits(int n) {
        int count = 0;
        for (int i = 0; i <= n; i++) {
            int j = i;
            while (j) {
                // Using bitwise AND to check if the least significant bit is set
                count += j & 1;
                // Right shift to move to the next bit
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
```

## Key Takeaways
- The `__builtin_popcount` function in C++ can be used to count the number of set bits in a number.
- Bitwise operations like `&` and `>>` can be used to manually count set bits in a number.
- The time complexity of the solution depends on the input range and the method used to count set bits.