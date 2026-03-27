# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, if `n = 5`, the binary representations are: `0 (0b0)`, `1 (0b1)`, `2 (0b10)`, `3 (0b11)`, `4 (0b100)`, `5 (0b101)`. The function should return an array where the `i-th` index stores the number of bits set in the binary representation of `i`. The constraints are: `0 <= n <= 10^5`.

## Approach
The approach is to iterate over all numbers from 0 to `n` and use bit manipulation to count the number of set bits in each number. We can use the built-in `__builtin_popcount` function in C++ or implement a custom function to count the set bits.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> countBits(int n) {
    vector<int> result(n + 1);
    for (int i = 0; i <= n; i++) {
        // Use __builtin_popcount to count the number of set bits
        result[i] = __builtin_popcount(i);
    }
    return result;
}

// Alternative implementation without __builtin_popcount
vector<int> countBitsAlternative(int n) {
    vector<int> result(n + 1);
    for (int i = 0; i <= n; i++) {
        int count = 0;
        int num = i;
        // Use bit manipulation to count the number of set bits
        while (num) {
            count += num & 1;
            num >>= 1;
        }
        result[i] = count;
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
- Use bit manipulation to count the number of set bits in a number.
- The `__builtin_popcount` function can be used to count the number of set bits in a number.
- The time complexity is O(n log n) due to the iteration over all numbers and the bit manipulation operation.