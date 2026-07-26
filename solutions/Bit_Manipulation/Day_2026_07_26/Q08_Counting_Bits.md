# Counting Bits

## Problem Statement
Given a non-negative integer `n`, count the number of bits that are set (i.e., 1) in its binary representation. For example, given `n = 9` (which is `1001` in binary), the function should return `2` because there are two bits set. The input `n` will be in the range `[0, 10^9]`.

## Approach
The approach is to use bit manipulation to count the number of set bits in the binary representation of `n`. We can use the Brian Kernighan's algorithm, which works by subtracting the least significant bit from `n` in each iteration.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countBits(int n) {
        int count = 0;
        while (n) {
            // Subtract the least significant bit from n
            n &= (n - 1);
            count++;
        }
        return count;
    }
};
```

## Test Cases
```
Input: n = 9
Output: 2
Input: n = 15
Output: 4
```

## Key Takeaways
- Brian Kernighan's algorithm is an efficient way to count the number of set bits in a binary representation.
- The algorithm works by subtracting the least significant bit from `n` in each iteration, effectively removing one set bit at a time.
- The time complexity of the algorithm is O(log n) because we are essentially counting the number of bits in the binary representation of `n`.