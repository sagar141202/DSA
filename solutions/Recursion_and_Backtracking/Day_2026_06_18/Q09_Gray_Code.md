# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given an integer `n`, generate all the Gray code sequences of length `n`. For example, if `n = 2`, the output should be `["00", "01", "11", "10"]`. The input `n` is guaranteed to be a positive integer.

## Approach
The problem can be solved using recursion and backtracking. We can generate the Gray code sequence by reflecting and prefixing the previous sequence. The base case is when `n` equals 1, in which case the sequence is `["0", "1"]`. For larger `n`, we can generate the sequence by prefixing "0" to the previous sequence and "1" to the reflected previous sequence.

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
Input: n = 2
Output: [0, 1, 3, 2]
Input: n = 3
Output: [0, 1, 3, 2, 6, 7, 5, 4]
```

## Key Takeaways
- The Gray code sequence can be generated using the formula `gray = i ^ (i >> 1)`, where `i` is the decimal number and `gray` is the corresponding Gray code.
- The time complexity of the solution is O(2^n) because we need to generate 2^n Gray code sequences.
- The space complexity of the solution is O(2^n) because we need to store 2^n Gray code sequences in the result vector.