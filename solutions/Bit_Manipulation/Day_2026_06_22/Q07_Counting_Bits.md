# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all integers from 0 to `n`. For example, if `n = 5`, the binary representations are `0 (0b0)`, `1 (0b1)`, `2 (0b10)`, `3 (0b11)`, `4 (0b100)`, and `5 (0b101)`. The total number of set bits is `0 + 1 + 1 + 2 + 1 + 2 = 7`. The function should return this total count.

## Approach
The approach is to iterate over all integers from 0 to `n` and for each integer, count the number of set bits in its binary representation. This can be done by using bitwise operations to check each bit. We use a loop to iterate over each integer and the built-in `__builtin_popcount` function or a manual loop to count set bits.

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

// Manual way to count set bits without __builtin_popcount
class SolutionManual {
public:
    int countBits(int n) {
        int count = 0;
        for (int i = 0; i <= n; i++) {
            int num = i;
            while (num) {
                count += num & 1; // Check the least significant bit
                num >>= 1; // Right shift to check the next bit
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
- Use bitwise operations to efficiently count set bits in integers.
- The `__builtin_popcount` function is a convenient way to count set bits, but understanding how to do it manually is also important.
- The time complexity of this solution is O(n log n) because we are iterating over `n` numbers and for each number, we are potentially checking up to `log n` bits.