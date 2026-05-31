# Counting Bits

## Problem Statement
Given a non-negative integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. The function should return an array of size `n + 1`, where the `i-th` index stores the number of bits set in the binary representation of `i`. For example, given `n = 5`, the binary representations are: `0` (0), `1` (1), `10` (2), `11` (2), `100` (2), `101` (2). The function should return `[0, 1, 1, 2, 1, 2]`.

## Approach
The approach involves using bit manipulation to count the number of set bits in each number from 0 to `n`. We can use the bitwise AND operator `&` and the bitwise right shift operator `>>` to achieve this.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> countBits(int n) {
    vector<int> result(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        // use bitwise AND and right shift to count set bits
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
- The bitwise right shift operator `>>` can be used to divide a number by 2.
- The bitwise AND operator `&` can be used to check if a bit is set in a number.
- Dynamic programming can be used to store the results of sub-problems and avoid redundant calculations.