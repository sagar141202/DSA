# Bitwise AND of Numbers Range

## Problem Statement
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive. For example, given the range [5, 7], the output should be 4, because the bitwise AND of 5, 6, and 7 is 4 (5 = 101, 6 = 110, 7 = 111, so 101 & 110 & 111 = 100, which is 4).

## Approach
The algorithm involves finding the common prefix of the binary representation of m and n, then appending zeros to get the result. This is because the bitwise AND operation will preserve the common prefix and discard the rest. We can find the common prefix by shifting both m and n to the right until they are equal.

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
        // shift both m and n to the right until they are equal
        int shift = 0;
        while (m != n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // append zeros to the common prefix
        return m << shift;
    }
};

int main() {
    Solution solution;
    cout << solution.rangeBitwiseAnd(5, 7) << endl;  // Output: 4
    return 0;
}
```

## Test Cases
```
Input: m = 5, n = 7
Output: 4
Input: m = 0, n = 0
Output: 0
Input: m = 1, n = 2
Output: 0
```

## Key Takeaways
- The bitwise AND operation preserves the common prefix of the binary representation of two numbers.
- Shifting both numbers to the right until they are equal gives the common prefix.
- Appending zeros to the common prefix gives the result of the bitwise AND operation on the range of numbers.