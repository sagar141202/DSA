# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, if `n = 5`, the binary representations are: 0 (0), 1 (1), 10 (2), 11 (3), 100 (4), and 101 (5). The total number of set bits is 7. The function should take an integer `n` as input and return the total count of set bits.

## Approach
We will use bit manipulation to solve this problem. The idea is to iterate over all numbers from 0 to `n` and for each number, count the number of set bits using Brian Kernighan's algorithm. This algorithm works by subtracting the least significant set bit from the number in each iteration until the number becomes 0.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countBits(int n) {
        int count = 0;
        for (int i = 0; i <= n; i++) {
            int num = i;
            while (num) {
                // Brian Kernighan's algorithm: subtracting the least significant set bit
                num &= (num - 1);
                count++;
            }
        }
        return count;
    }
};
```

## Test Cases
```
Input: n = 5
Output: 7
Input: n = 10
Output: 17
```

## Key Takeaways
- Bit manipulation is a crucial concept in competitive programming and can be used to solve a variety of problems.
- Brian Kernighan's algorithm is an efficient way to count the number of set bits in a binary number.
- The time complexity of the solution is O(n log n) due to the iteration over all numbers from 0 to `n` and the while loop inside it.