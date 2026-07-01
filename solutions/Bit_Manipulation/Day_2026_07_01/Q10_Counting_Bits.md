# Counting Bits

## Problem Statement
Given a positive integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, if `n = 5`, the binary representations are: 0 (0), 1 (1), 10 (2), 11 (3), 100 (4), and 101 (5). The total number of set bits is 7. The input `n` is a 32-bit integer, and the output should be an integer.

## Approach
The algorithm uses bit manipulation to count the set bits in each number. It iterates over all numbers from 0 to `n`, and for each number, it counts the set bits using Brian Kernighan's algorithm. This approach ensures an efficient solution with minimal computational overhead.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            // Brian Kernighan's algorithm to count set bits
            result[i] = result[i & (i - 1)] + 1;
        }
        return result;
    }
};
```

## Test Cases
```
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
```

## Key Takeaways
- Brian Kernighan's algorithm is used to count the set bits in a number, which works by subtracting 1 from the number and performing a bitwise AND operation with the original number.
- The result of `i & (i - 1)` gives the number with the least significant set bit removed, allowing us to recursively count the set bits.
- The time complexity of O(n log n) is due to the iteration over all numbers from 0 to `n` and the bit manipulation operations.