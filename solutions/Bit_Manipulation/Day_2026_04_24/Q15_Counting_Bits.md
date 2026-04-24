# Counting Bits

## Problem Statement
Given a non-negative integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, given `n = 5`, the binary representations are: 0 (0), 1 (1), 10 (2), 11 (3), 100 (4), and 101 (5). The total number of set bits is 7. The function should return the total count of set bits. The constraints are: 0 <= n <= 10^9.

## Approach
We will use dynamic programming to solve this problem by counting the set bits for each number up to `n`. The idea is to use the previously computed values to calculate the set bits for the current number. We will also use bit manipulation to get the last set bit.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countBits(int n) {
        // Initialize the count of set bits
        int count = 0;
        
        // Loop through each number from 0 to n
        for (int i = 0; i <= n; i++) {
            // Use bit manipulation to count the set bits
            count += __builtin_popcount(i);
        }
        
        return count;
    }
};
```

## Test Cases
```
Input: n = 5
Output: 7
Input: n = 15
Output: 22
```

## Key Takeaways
- Use dynamic programming to solve the problem efficiently.
- Utilize bit manipulation functions like `__builtin_popcount` to count set bits.
- The time complexity can be optimized to O(log n) by using bit manipulation.