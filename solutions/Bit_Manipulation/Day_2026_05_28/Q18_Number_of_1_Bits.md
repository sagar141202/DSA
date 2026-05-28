# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer will be between 0 and 4294967295 (2^32 - 1). For example, if the input is 9 (which is 1001 in binary), the function should return 2, because there are two 1 bits in the binary representation of 9.

## Approach
The algorithm uses bit manipulation to count the number of 1 bits in the binary representation of the input integer. It works by continuously clearing the least significant 1 bit in the integer until all bits are 0. The number of iterations required to clear all bits is equal to the number of 1 bits in the original integer.

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
            // clear the least significant 1 bit
            n &= (n - 1);
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
Input: 15
Output: 4
```

## Key Takeaways
- The expression `n & (n - 1)` clears the least significant 1 bit in `n`.
- The time complexity is O(log n) because in the worst case, we need to iterate log(n) times to clear all bits in the integer `n`.
- The space complexity is O(1) because we only use a constant amount of space to store the input and the count of 1 bits.