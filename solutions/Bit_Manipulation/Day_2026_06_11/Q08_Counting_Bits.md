# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, if `n = 5`, the binary representations are: 0 (0), 1 (1), 10 (2), 11 (3), 100 (4), and 101 (5). The function should return an array where the `i-th` index stores the number of bits set in the binary representation of `i`. The constraints are: `0 <= n <= 10^5`.

## Approach
The approach is to use bit manipulation to count the number of set bits in each number. We can use the built-in `__builtin_popcount` function in C++ or implement our own function using bitwise operations. We will iterate over all numbers from 0 to `n` and store the count of set bits in an array.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> countBits(int n) {
    vector<int> res(n + 1);
    for (int i = 0; i <= n; i++) {
        // use __builtin_popcount to count the number of set bits
        res[i] = __builtin_popcount(i);
    }
    return res;
}

// alternative implementation without __builtin_popcount
vector<int> countBitsAlternative(int n) {
    vector<int> res(n + 1);
    for (int i = 0; i <= n; i++) {
        int count = 0;
        int num = i;
        // use bitwise operations to count the number of set bits
        while (num) {
            count += num & 1;
            num >>= 1;
        }
        res[i] = count;
    }
    return res;
}
```

## Test Cases
```
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
```

## Key Takeaways
- Use bit manipulation to count the number of set bits in a number.
- The `__builtin_popcount` function in C++ can be used to count the number of set bits.
- Bitwise operations can be used to implement the count function manually.