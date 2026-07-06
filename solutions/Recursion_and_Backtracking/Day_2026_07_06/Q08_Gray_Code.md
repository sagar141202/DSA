# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n` representing the number of bits in the code, find the Gray code sequence of `n` bits. The sequence should be in the form of a list of integers, where each integer represents a Gray code. For example, for `n = 2`, the Gray code sequence is `[0, 1, 3, 2]`. The sequence should be in ascending order.

## Approach
The Gray code sequence can be generated using recursion and backtracking. We can start with the base case where `n = 1`, and then recursively generate the sequence for `n > 1` by reflecting and prefixing the previous sequence.

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
            // Calculate the Gray code using bitwise XOR
            int gray = i ^ (i >> 1);
            result.push_back(gray);
        }
        return result;
    }
};

// Alternatively, recursive approach
class SolutionRecursive {
public:
    vector<int> grayCode(int n) {
        if (n == 1) {
            return {0, 1};
        }
        vector<int> prev = grayCode(n - 1);
        vector<int> result;
        // Reflect and prefix the previous sequence
        for (int i = 0; i < prev.size(); i++) {
            result.push_back(prev[i]);
        }
        for (int i = prev.size() - 1; i >= 0; i--) {
            result.push_back(prev[i] | (1 << (n - 1)));
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
- The Gray code sequence can be generated using both iterative and recursive approaches.
- The iterative approach uses bitwise XOR to calculate the Gray code, while the recursive approach reflects and prefixes the previous sequence.
- The time and space complexity of both approaches are O(2^n), where n is the number of bits in the code.