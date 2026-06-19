# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in the binary representation of the number. The input is guaranteed to be a 32-bit unsigned integer. For example, the binary representation of 9 is 1001, so the function should return 2. The function should be efficient and handle large inputs.

## Approach
The approach is to use bit manipulation to count the number of 1 bits in the binary representation of the number. We can use the Brian Kernighan's algorithm, which works by subtracting the least significant 1 bit from the number in each iteration. The algorithm repeats until all 1 bits are removed from the number.

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
- Use bit manipulation to efficiently count the number of 1 bits in the binary representation of a number.
- Brian Kernighan's algorithm is a simple and efficient way to count the number of 1 bits.
- The time complexity of the algorithm is O(log n), where n is the input number.