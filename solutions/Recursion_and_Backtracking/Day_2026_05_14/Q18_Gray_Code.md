# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer n, generate all the Gray codes of n bits. For example, if n = 2, the output should be ["00", "01", "11", "10"]. If n = 3, the output should be ["000", "001", "011", "010", "110", "111", "101", "100"]. The input n is guaranteed to be a non-negative integer.

## Approach
The algorithm uses recursion and backtracking to generate all possible Gray codes. It starts with the base case of n = 1 and then constructs the Gray codes for n bits by reflecting and prefixing the codes for n-1 bits.

## Complexity
- Time: O(2^n)
- Space: O(2^n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        for (int i = 0; i < (1 << n); i++) {
            // calculate the Gray code using bitwise XOR operation
            int gray = i ^ (i >> 1);
            result.push_back(gray);
        }
        return result;
    }
};
```

## Test Cases
```
Input: 2
Output: [0, 1, 3, 2]
Input: 3
Output: [0, 1, 3, 2, 6, 7, 5, 4]
```

## Key Takeaways
- The Gray code can be calculated using a bitwise XOR operation.
- The recursive approach can be avoided by using a simple iterative solution.
- The time complexity is O(2^n) due to the generation of all possible Gray codes.