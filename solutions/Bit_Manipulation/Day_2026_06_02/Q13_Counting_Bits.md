# Counting Bits

## Problem Statement
Given an integer `n`, write a function that returns an array where the `i-th` index stores the number of bits that are set (i.e., 1) in the binary representation of `i`. The function should take an integer `n` as input and return an array of size `n+1`. For example, if `n = 5`, the output should be `[0, 1, 1, 2, 1, 2]` because the binary representations of numbers from 0 to 5 are `000, 001, 010, 011, 100, 101` respectively.

## Approach
The approach is to iterate over all numbers from 0 to `n` and for each number, count the number of set bits in its binary representation. This can be done using bit manipulation techniques. We can use the built-in `__builtin_popcount` function in C++ or implement our own function to count the number of set bits.

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
        // count the number of set bits in i
        result[i] = __builtin_popcount(i);
    }
    return result;
}

// or without using __builtin_popcount
vector<int> countBits(int n) {
    vector<int> result(n + 1, 0);
    for (int i = 0; i <= n; i++) {
        int count = 0;
        int j = i;
        // count the number of set bits in i
        while (j) {
            count += j & 1;
            j >>= 1;
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
- Bit manipulation can be used to count the number of set bits in a binary representation of a number.
- The `__builtin_popcount` function in C++ can be used to count the number of set bits in a number.
- The time complexity of the solution is O(n log n) because we are iterating over all numbers from 0 to `n` and for each number, we are counting the number of set bits which takes O(log n) time.