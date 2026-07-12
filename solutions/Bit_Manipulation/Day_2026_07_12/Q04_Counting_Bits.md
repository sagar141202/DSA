# Counting Bits

## Problem Statement
Given a non-negative integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. The function should return an array where the `i-th` index contains the number of bits set in the binary representation of `i`. For example, if `n = 5`, the binary representations are `0 (0), 1 (1), 10 (1), 11 (2), 100 (1)`, and `101 (2)`, so the function should return `[0, 1, 1, 2, 1, 2]`. The input `n` will be in the range `[0, 10^5]`.

## Approach
The approach is to use dynamic programming and bit manipulation to calculate the number of bits set for each number up to `n`. We can use the fact that the number of bits set in `i` is equal to the number of bits set in `i / 2` plus the least significant bit of `i`.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> countBits(int n) {
    vector<int> result(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        // calculate the number of bits set in i
        result[i] = result[i >> 1] + (i & 1);
    }
    return result;
}
```

## Test Cases
```
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
Input: n = 10
Output: [0, 1, 1, 2, 1, 2, 2, 1, 2, 2, 3]
```

## Key Takeaways
- Bit manipulation can be used to efficiently calculate the number of bits set in a number.
- Dynamic programming can be used to store and reuse the results of subproblems to improve efficiency.
- The least significant bit of a number can be obtained using the bitwise AND operator `&` with 1.