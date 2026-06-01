# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given an integer n, generate all possible Gray codes of length n. For example, if n = 2, the output should be ["00", "01", "11", "10"]. If n = 3, the output should be ["000", "001", "011", "010", "110", "111", "101", "100"]. The constraints are 1 <= n <= 16.

## Approach
The algorithm uses recursion and backtracking to generate all possible Gray codes. It starts with the base case of n = 1 and then recursively generates the Gray codes for n = 2, 3, and so on. The key idea is to reflect the Gray codes of the previous length and append a 0 or 1 to the beginning of each code.

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
- The Gray code can be generated using the XOR operator and right shift operator.
- The time complexity is exponential due to the recursive nature of the problem.
- The space complexity is also exponential as we need to store all possible Gray codes.