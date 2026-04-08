# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. The function should return a vector of integers, where the `i-th` integer in the vector represents the number of bits set in the binary representation of `i`. For example, given `n = 5`, the binary representations are: `0` (0), `1` (1), `10` (1), `11` (2), `100` (1), `101` (2), `110` (2), `111` (3). The function should return `[0, 1, 1, 2, 1, 2, 2, 3]`. The input `n` will be in the range `[0, 10^5]`.

## Approach
The approach is to use bit manipulation to count the number of set bits for each number from 0 to `n`. We can use the built-in `__builtin_popcount` function in C++ to count the number of set bits. Alternatively, we can use a simple loop to count the number of set bits by shifting the bits to the right and checking the least significant bit.

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
        // count the number of set bits using bit manipulation
        result[i] = result[i >> 1] + (i & 1);
    }
    return result;
}
```

## Test Cases
```
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
```

## Key Takeaways
- Use bit manipulation to count the number of set bits for each number.
- The `__builtin_popcount` function can be used to count the number of set bits, but it's not necessary in this case.
- The time complexity is O(n log n) because we need to iterate over all numbers from 0 to `n` and count the number of set bits for each number.