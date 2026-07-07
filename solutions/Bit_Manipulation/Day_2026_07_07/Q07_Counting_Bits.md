# Counting Bits

## Problem Statement
Given a positive integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, if `n = 5`, the binary representations are 0 (0), 1 (1), 10 (2), 11 (3), 100 (4), and 101 (5). The total number of set bits is 0 + 1 + 1 + 2 + 1 + 2 = 7. The function should return this total count.

## Approach
The approach involves iterating over all numbers from 0 to `n` and counting the set bits in each number's binary representation. We can use bit manipulation to achieve this efficiently. The idea is to use bitwise operations to count the number of set bits.

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
            // Use __builtin_popcount to count set bits
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
```

## Key Takeaways
- Use `__builtin_popcount` for counting set bits in a number.
- Iterate over the range of numbers to accumulate the total count of set bits.
- Time complexity is dominated by the iteration and the bit counting operation.