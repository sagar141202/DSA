# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers from m to n, find the bitwise AND of all numbers in this range. The range is defined as [m, n] where 0 <= m <= n <= 2^31 - 1. For example, given m = 5 and n = 7, the bitwise AND of all numbers in this range is 4.

## Approach
The algorithm finds the common prefix of the binary representation of m and n, then constructs the result by shifting 1 to the left by the length of the common prefix and subtracting 1. This is because the bitwise AND of all numbers in a range will have the common prefix of the binary representation of the numbers in the range.

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
        // find the common prefix of the binary representation of m and n
        int shift = 0;
        while (m < n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // construct the result by shifting 1 to the left by the length of the common prefix and subtracting 1
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
Input: m = 1, n = 2
Output: 0
```

## Key Takeaways
- The bitwise AND of all numbers in a range will have the common prefix of the binary representation of the numbers in the range.
- The common prefix can be found by shifting the numbers to the right until they are equal.
- The result can be constructed by shifting 1 to the left by the length of the common prefix.