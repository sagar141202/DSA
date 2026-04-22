# Counting Bits

## Problem Statement
Given a non-negative integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all non-negative integers up to `n`. For example, given `n = 5`, the binary representations are: `0` (0), `1` (1), `10` (2), `11` (3), `100` (4), and `101` (5). The total number of set bits is 7. The input `n` will be in the range `[0, 10^9]`.

## Approach
We can use bit manipulation to iterate through all numbers up to `n` and count the set bits. The key idea is to use bitwise operations to check if a bit is set. We can use a loop to iterate through each bit position and count the number of set bits at that position.

## Complexity
- Time: O(log n * n)
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
            count += __builtin_popcount(i); // count set bits in i
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
- Use bitwise operations to count set bits in a number.
- The `__builtin_popcount` function in C++ can be used to count the number of set bits in a number.
- This solution has a time complexity of O(log n * n) because we are iterating through all numbers up to `n` and counting the set bits in each number.