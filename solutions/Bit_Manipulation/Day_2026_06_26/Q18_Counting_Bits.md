# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. The function should return a vector of integers where the `i-th` integer represents the number of bits set in the binary representation of `i`. For example, if `n = 5`, the binary representations are `0 (0), 1 (1), 10 (1), 11 (2), 100 (1), 101 (2), 110 (2), 111 (3)`, and the output should be `[0, 1, 1, 2, 1, 2]`. The input `n` will be in the range `[0, 10^5]`.

## Approach
We can solve this problem using bit manipulation by iterating over all numbers from 0 to `n` and counting the number of set bits in each number. We can use the built-in `__builtin_popcount` function in C++ to count the number of set bits.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> countBits(int n) {
    vector<int> result(n + 1);
    for (int i = 0; i <= n; i++) {
        // count the number of set bits in i
        result[i] = __builtin_popcount(i);
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
- Use bit manipulation to count the number of set bits in a number.
- The `__builtin_popcount` function in C++ can be used to count the number of set bits.
- The time complexity of this solution is O(n) where n is the input number.