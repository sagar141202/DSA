# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. The function should return a vector of size `n + 1`, where the `i-th` index represents the number of set bits in the binary representation of `i`. For example, given `n = 5`, the binary representations are `0` (0), `1` (1), `10` (1), `11` (2), `100` (1), and `101` (2), so the function should return `[0, 1, 1, 2, 1, 2]`. The input `n` will be in the range `[0, 10^5]`.

## Approach
The approach is to use bit manipulation to count the set bits for each number from 0 to `n`. We can use the built-in `__builtin_popcount` function in C++ or implement our own function to count the set bits. The algorithm iterates over all numbers from 0 to `n` and counts the set bits for each number.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> countBits(int n) {
    vector<int> result(n + 1, 0);
    for (int i = 0; i <= n; i++) {
        // count the set bits using built-in function
        result[i] = __builtin_popcount(i);
    }
    return result;
}

// alternative implementation without built-in function
vector<int> countBitsAlternative(int n) {
    vector<int> result(n + 1, 0);
    for (int i = 0; i <= n; i++) {
        int count = 0;
        int num = i;
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
Input: n = 10
Output: [0, 1, 1, 2, 1, 2, 2, 1, 2, 2, 3]
```

## Key Takeaways
- Use bit manipulation to count the set bits in the binary representation of a number.
- The `__builtin_popcount` function in C++ can be used to count the set bits.
- The time complexity is O(n log n) due to the iteration over all numbers from 0 to `n` and the bit manipulation operations.