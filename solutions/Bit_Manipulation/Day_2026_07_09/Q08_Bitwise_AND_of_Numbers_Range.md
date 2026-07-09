# Bitwise AND of Numbers Range

## Problem Statement
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive. For example, given the range [5, 7], the output should be 4, because the bitwise AND of 5, 6, and 7 is 4 (5 = 101, 6 = 110, 7 = 111, so 101 & 110 & 111 = 100, which is 4).

## Approach
The algorithm involves finding the common prefix of the binary representations of m and n, then using this prefix to calculate the bitwise AND. This is because the bitwise AND operation will result in zeros for any bits that differ between m and n. By finding the common prefix, we can determine the bits that will be set in the result.

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
        // find the common prefix length
        int shift = 0;
        while (m < n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // calculate the result
        return m << shift;
    }
};
```

## Test Cases
```
Input: m = 5, n = 7
Output: 4
Input: m = 1, n = 10
Output: 0
```

## Key Takeaways
- The bitwise AND operation can be used to find the common prefix of two binary numbers.
- The common prefix can be used to calculate the bitwise AND of a range of numbers.
- The time complexity of this solution is O(log n), where n is the larger number in the range.