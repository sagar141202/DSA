# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, find the bitwise AND of all numbers in the range. The bitwise AND operation compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0. For example, the bitwise AND of 5 (101) and 3 (011) is 1 (001).

## Approach
The algorithm uses bit manipulation to find the common prefix of the binary representation of m and n. This common prefix is the bitwise AND of all numbers in the range [m, n]. We shift both m and n to the right until they are equal, which gives us the common prefix.

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
        // return the common prefix (m) shifted back to its original position
        return m << shift;
    }
};

int main() {
    Solution solution;
    cout << solution.rangeBitwiseAnd(5, 7) << endl;  // Output: 4
    cout << solution.rangeBitwiseAnd(1, 2) << endl;    // Output: 0
    return 0;
}
```

## Test Cases
```
Input: m = 5, n = 7
Output: 4
Input: m = 1, n = 2
Output: 0
```

## Key Takeaways
- The bitwise AND operation can be used to find the common prefix of the binary representation of two numbers.
- Shifting both numbers to the right until they are equal gives us the common prefix.
- The common prefix is the bitwise AND of all numbers in the range [m, n].