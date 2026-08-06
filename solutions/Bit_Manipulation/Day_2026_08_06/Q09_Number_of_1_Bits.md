# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer will be in the range [0, 2^32 - 1]. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 13 is 1101, so the function should return 3.

## Approach
The approach is to use bit manipulation to count the number of 1 bits. We can use the Brian Kernighan's algorithm, which works by subtracting the least significant 1 bit from the number in each iteration. The algorithm repeats until all bits are 0.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n) {
            // subtract the least significant 1 bit from n
            n &= n - 1;
            count++;
        }
        return count;
    }
};
```

## Test Cases
```
Input: 9
Output: 2
Input: 13
Output: 3
```

## Key Takeaways
- Brian Kernighan's algorithm is an efficient way to count the number of 1 bits in a binary representation.
- The algorithm works by subtracting the least significant 1 bit from the number in each iteration.
- The time complexity of the algorithm is O(log n), where n is the input number.