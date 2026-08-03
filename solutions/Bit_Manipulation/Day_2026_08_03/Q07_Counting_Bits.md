# Counting Bits

## Problem Statement
Given a positive integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, given `n = 5`, the binary representations are: `0 (0b0)`, `1 (0b1)`, `2 (0b10)`, `3 (0b11)`, `4 (0b100)`, and `5 (0b101)`. The total number of set bits is `7`. The constraint is `0 <= n <= 10^5`.

## Approach
The algorithm uses bit manipulation to count the set bits. It iterates through all numbers from 0 to `n` and uses bitwise operations to count the set bits in each number. The key idea is to use the bitwise AND operator (`&`) to check if a bit is set.

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
            // use bitwise operation to count set bits
            result[i] = result[i >> 1] + (i & 1);
        }
        return result;
    }
};
```

## Test Cases
```
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
```

## Key Takeaways
- Use bitwise operations to efficiently count set bits in a number.
- The expression `i >> 1` is equivalent to `i / 2` and `i & 1` checks if the least significant bit is set.