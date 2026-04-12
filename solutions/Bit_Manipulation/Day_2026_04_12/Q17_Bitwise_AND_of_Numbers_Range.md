# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, find the bitwise AND of all numbers in this range. The bitwise AND of two numbers is the number formed by taking the bitwise AND of their corresponding bits. For example, the bitwise AND of 5 (101) and 3 (011) is 1 (001).

## Approach
The algorithm involves finding the common prefix of the binary representation of m and n, then appending zeros to get the result. This is because the bitwise AND operation will result in zeros for any bits that are different between m and n.

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
        // find the number of common prefix bits
        int shift = 0;
        while (m < n) {
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
    cout << solution.rangeBitwiseAnd(1, 2) << endl;   // Output: 0
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
- The bitwise AND operation can be used to find the common prefix of two binary numbers.
- Shifting the bits of a number to the right is equivalent to dividing it by 2.
- The number of common prefix bits can be found by shifting the bits of the two numbers to the right until they are equal.