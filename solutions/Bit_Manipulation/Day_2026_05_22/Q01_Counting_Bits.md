# Counting Bits

## Problem Statement
Given an integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, given `n = 5`, the binary representations are: `0` (0), `1` (1), `10` (2), `11` (3), `100` (4), and `101` (5). The total number of set bits is 7. The input `n` will be in the range `[0, 10^9]`.

## Approach
We can use a simple iterative approach to count the set bits for each number from 0 to `n`. Alternatively, we can use Brian Kernighan's algorithm to optimize the solution. This algorithm works by subtracting the least significant bit from the number in each iteration, effectively counting the number of bits set.

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
            // Brian Kernighan's algorithm
            int j = i;
            while (j) {
                // subtract the least significant bit
                j &= (j - 1);
                count++;
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
- Brian Kernighan's algorithm can be used to count the number of set bits in a number.
- The time complexity of the solution depends on the number of bits in the input number `n`.