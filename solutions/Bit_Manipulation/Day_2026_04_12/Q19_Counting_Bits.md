# Counting Bits

## Problem Statement
Given a non-negative integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. The function should return an array where the i-th index contains the number of bits set in the binary representation of `i`. For example, given `n = 5`, the binary representations are: 0 (0), 1 (1), 10 (1), 11 (2), 100 (1), 101 (2), 110 (2), 111 (3), 1000 (1). So the output should be `[0, 1, 1, 2, 1, 2]`. The constraints are: `0 <= n <= 10^5`.

## Approach
We can use bit manipulation to solve this problem by iterating over all numbers from 0 to `n` and counting the number of set bits in each number. We can use the built-in `__builtin_popcount` function or implement our own function to count the number of set bits. Alternatively, we can use dynamic programming to store the number of set bits for each number and build up the solution.

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
Input: n = 10
Output: [0, 1, 1, 2, 1, 2, 2, 1, 2, 2, 3]
```

## Key Takeaways
- Use bit manipulation to count the number of set bits in a number.
- Use dynamic programming to store the number of set bits for each number and build up the solution.
- The `__builtin_popcount` function can be used to count the number of set bits in a number, but it may not be available in all compilers.