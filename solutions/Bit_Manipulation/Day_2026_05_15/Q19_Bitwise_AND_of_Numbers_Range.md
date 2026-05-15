# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range. For example, if the input is [5, 7], the output should be 4, which is the result of 5 & 6 & 7. The constraints are 0 <= m <= n <= 2147483647.

## Approach
The algorithm involves finding the common prefix of the binary representation of m and n. This is because the bitwise AND operation will preserve the common prefix and discard the rest. We can use bit manipulation to find the common prefix.

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
        // find the common prefix by shifting both numbers to the right
        int shift = 0;
        while (m < n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // restore the common prefix and discard the rest
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
- The bitwise AND operation preserves the common prefix of the binary representation of two numbers.
- We can use bit manipulation to find the common prefix by shifting both numbers to the right.
- The time complexity is O(log n) because we are shifting the numbers to the right until they are equal.