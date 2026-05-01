# Gray Code

## Problem Statement
The Gray Code is a sequence of binary numbers where each number differs from the previous one by only one bit. Given a non-negative integer `n`, generate all the Gray Code sequences of length `n`. For example, if `n = 2`, the Gray Code sequence is `[00, 01, 11, 10]`. If `n = 3`, the Gray Code sequence is `[000, 001, 011, 010, 110, 111, 101, 100]`. The sequence should be returned as a list of integers.

## Approach
The problem can be solved using recursion and backtracking. We start with the base case where `n = 1` and then recursively generate the Gray Code sequence for `n > 1` by reflecting and prefixing the previous sequence. The key idea is to use the property of Gray Code that each number differs from the previous one by only one bit.

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
- The Gray Code sequence can be generated using the property that each number differs from the previous one by only one bit.
- The sequence can be generated using recursion and backtracking, but a more efficient approach is to use bitwise XOR to calculate the Gray Code directly.
- The time and space complexity of the solution is O(2^n), where n is the length of the Gray Code sequence.