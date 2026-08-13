# Bitwise AND of Numbers Range

## Problem Statement
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive. For example, given the range [5, 7], the output should be 4, because 5 & 6 & 7 = 4, and given the range [2, 4], the output should be 0, because 2 & 3 & 4 = 0.

## Approach
The algorithm involves finding the common prefix of the binary representations of m and n. This common prefix can be used to calculate the bitwise AND of all numbers in the range. We can achieve this by shifting both m and n to the right until they are equal.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        // shift m and n to the right until they are equal
        int shift = 0;
        while (m < n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // the common prefix is the bitwise AND of all numbers in the range
        return m << shift;
    }
};
```

## Test Cases
```
Input: m = 5, n = 7
Output: 4
Input: m = 2, n = 4
Output: 0
```

## Key Takeaways
- The bitwise AND of a range of numbers can be calculated by finding the common prefix of the binary representations of the numbers.
- Shifting numbers to the right is equivalent to dividing them by 2, which helps in finding the common prefix.
- The common prefix can be used to calculate the bitwise AND of all numbers in the range by shifting it back to the left.