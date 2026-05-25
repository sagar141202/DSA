# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. The function should return a vector of integers where the `i-th` element is the number of bits set in the binary representation of `i`. For example, given `n = 5`, the binary representations are `0` (0), `1` (1), `10` (1), `11` (2), `100` (1), `101` (2), `110` (2), `111` (3), so the function should return `[0, 1, 1, 2, 1, 2, 2, 3]`. The input `n` will be in the range `[0, 10^5]`.

## Approach
The approach is to use bit manipulation to count the number of bits set in each number from 0 to `n`. We can use the built-in `__builtin_popcount` function in C++ to count the number of bits set in a number. Alternatively, we can use a loop to shift the bits of the number to the right and count the number of bits set.

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
        // Use __builtin_popcount to count the number of bits set in i
        result[i] = __builtin_popcount(i);
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
- The `__builtin_popcount` function can be used to count the number of bits set in a number.
- The time complexity of the solution is O(n) because we need to iterate over all numbers from 0 to `n`.
- The space complexity of the solution is O(n) because we need to store the result for each number from 0 to `n`.