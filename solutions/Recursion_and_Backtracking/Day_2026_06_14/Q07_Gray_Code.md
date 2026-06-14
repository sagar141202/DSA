# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given an integer `n`, generate all `n`-bit Gray codes in ascending order. For example, given `n = 2`, the output should be `["00", "01", "11", "10"]`. The input `n` will be in the range `[1, 16]`.

## Approach
The problem can be solved using recursion and backtracking by generating all possible binary codes and then filtering out the ones that do not satisfy the Gray code property. However, a more efficient approach is to use the reflective property of Gray codes, where the `n`-bit Gray code can be generated from the `(n-1)`-bit Gray code.

## Complexity
- Time: O(2^n)
- Space: O(2^n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> grayCode(int n) {
        vector<string> result;
        for (int i = 0; i < (1 << n); i++) {
            int gray = i ^ (i >> 1);
            string binary = "";
            for (int j = n - 1; j >= 0; j--) {
                binary += (gray >> j) & 1 ? '1' : '0';
            }
            result.push_back(binary);
        }
        return result;
    }
};
```

## Test Cases
```
Input: n = 2
Output: ["00", "01", "11", "10"]
Input: n = 3
Output: ["000", "001", "011", "010", "110", "111", "101", "100"]
```

## Key Takeaways
- The Gray code can be generated using the formula `gray = i ^ (i >> 1)`, where `i` is the decimal number and `gray` is the corresponding Gray code.
- The reflective property of Gray codes can be used to generate the `n`-bit Gray code from the `(n-1)`-bit Gray code.
- The time complexity of the solution is O(2^n) because there are 2^n possible Gray codes for `n` bits.