# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. The function should return a vector of size `n+1`, where the `i-th` index contains the number of set bits in the binary representation of `i`. For example, given `n = 5`, the function should return `[0, 1, 1, 2, 1, 2]`, because the binary representations of numbers from 0 to 5 are `000, 001, 010, 011, 100, 101`, and the number of set bits in each representation are `0, 1, 1, 2, 1, 2`, respectively. The input `n` will be in the range `[0, 10^5]`.

## Approach
We can use bit manipulation to solve this problem by iterating over all numbers from 0 to `n` and counting the number of set bits in each number. We can use the built-in `__builtin_popcount` function in C++ to count the number of set bits. Alternatively, we can use a loop to iterate over each bit in the number and count the number of set bits.

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
        // Use __builtin_popcount to count the number of set bits
        result[i] = __builtin_popcount(i);
    }
    return result;
}

// Alternatively, we can use a loop to count the number of set bits
vector<int> countBitsAlternative(int n) {
    vector<int> result(n + 1, 0);
    for (int i = 0; i <= n; i++) {
        int count = 0;
        int num = i;
        while (num) {
            // If the least significant bit is 1, increment the count
            count += num & 1;
            // Right shift the number by 1 bit
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
- The `__builtin_popcount` function in C++ can be used to count the number of set bits in a number.
- Bit manipulation can be used to solve problems involving binary representations of numbers.
- The time complexity of the solution is O(n log n) due to the iteration over all numbers from 0 to `n` and the bit manipulation operations.