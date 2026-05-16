# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer n representing the number of bits in the code, find the Gray code sequence of n bits. The sequence should be in the form of a list of integers, where each integer represents a number in the Gray code sequence. For example, for n = 2, the Gray code sequence is [0, 1, 3, 2]. The sequence should be returned in ascending order.

## Approach
The algorithm uses recursion and backtracking to generate the Gray code sequence. It starts with the base case of n = 1 and then recursively generates the sequence for n bits by mirroring the sequence for n-1 bits and prefixing the mirrored sequence with 1. The base case is when n = 1, in which case the sequence is [0, 1].

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
            // Calculate the Gray code using the XOR operation
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
- The Gray code sequence can be generated using the XOR operation.
- The sequence can be generated recursively by mirroring the sequence for n-1 bits and prefixing the mirrored sequence with 1.
- The time and space complexity of the solution is O(2^n), where n is the number of bits in the code.