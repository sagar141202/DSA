# Counting Bits

## Problem Statement
Given a non-negative integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all non-negative integers up to `n`. For example, given `n = 5`, the binary representations are: `0` (0), `1` (1), `10` (2), `11` (3), `100` (4), and `101` (5). The total number of set bits is 7.

## Approach
The approach involves using bit manipulation to calculate the number of set bits for each number up to `n`. We can utilize the concept of Brian Kernighan's algorithm to count the number of set bits in a given number.

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
        vector<int> res(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            // use bit manipulation to calculate the number of set bits
            res[i] = res[i >> 1] + (i & 1);
        }
        return res;
    }
};
```

## Test Cases
```
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
```

## Key Takeaways
- Use bit manipulation to calculate the number of set bits in a given number.
- Utilize the concept of dynamic programming to store and reuse the results of subproblems.
- The `i >> 1` operation is equivalent to dividing `i` by 2, and `i & 1` checks if the least significant bit of `i` is 1.