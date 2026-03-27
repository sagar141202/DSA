# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range. For example, given the range [5, 7], the bitwise AND is 5 & 6 & 7 = 4, and given the range [2, 4], the bitwise AND is 2 & 3 & 4 = 0.

## Approach
The algorithm uses the property of bitwise AND operation to find the common prefix of binary representation of m and n. The bitwise AND of all numbers in the range [m, n] will be the common prefix of m and n.

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
        // find the common prefix of m and n
        int shift = 0;
        while (m < n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // the bitwise AND of all numbers in the range [m, n] is the common prefix of m and n
        return m << shift;
    }
};

int main() {
    Solution solution;
    cout << solution.rangeBitwiseAnd(5, 7) << endl;  // Output: 4
    cout << solution.rangeBitwiseAnd(2, 4) << endl;   // Output: 0
    return 0;
}
```

## Test Cases
```
Input: m = 5, n = 7
Output: 4
Input: m = 2, n = 4
Output: 0
```

## Key Takeaways
- The bitwise AND of all numbers in the range [m, n] can be calculated by finding the common prefix of binary representation of m and n.
- The common prefix can be found by shifting m and n to the right until they are equal.
- The bitwise AND of all numbers in the range [m, n] is the common prefix of m and n shifted back to its original position.