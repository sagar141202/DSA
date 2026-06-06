# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given an integer n, generate all possible Gray code sequences of length n. For example, if n = 2, the Gray code sequences are ["00", "01", "11", "10"]. If n = 3, the Gray code sequences are ["000", "001", "011", "010", "110", "111", "101", "100"].

## Approach
The algorithm uses recursion and backtracking to generate all possible Gray code sequences. It starts with an initial sequence and then recursively generates all possible sequences by changing one bit at a time. The key intuition is to reflect the sequence when generating the next level of sequences.

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
            // calculate the gray code using bitwise XOR
            int gray = i ^ (i >> 1);
            result.push_back(gray);
        }
        return result;
    }
};
```

## Test Cases
```
Input: n = 2
Output: [0, 1, 3, 2]
Input: n = 3
Output: [0, 1, 3, 2, 6, 7, 5, 4]
```

## Key Takeaways
- The Gray code sequence can be generated using bitwise operations.
- The time complexity is exponential due to the recursive nature of the problem.
- The space complexity is also exponential as we need to store all possible sequences.