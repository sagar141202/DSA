# Gray Code

## Problem Statement
The Gray Code is a sequence of binary numbers where each number differs from the previous one by only one bit. Given a non-negative integer n, generate all the Gray Code sequences of length n. For example, if n = 2, the Gray Code sequences are ["00", "01", "11", "10"].

## Approach
The Gray Code sequence can be generated using recursion and backtracking. We can start with an initial sequence and then recursively generate the next sequence by flipping one bit at a time. The key insight is to use the previous sequence to generate the next one.

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
            // Calculate the Gray Code using bitwise XOR
            int gray = i ^ (i >> 1);
            result.push_back(gray);
        }
        return result;
    }
};

// Alternatively, we can use recursion to generate the Gray Code
class SolutionRecursive {
public:
    vector<int> grayCode(int n) {
        if (n == 0) {
            return {0};
        }
        vector<int> prev = grayCode(n - 1);
        vector<int> result;
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
- The Gray Code sequence can be generated using recursion and backtracking.
- The key insight is to use the previous sequence to generate the next one.
- The time complexity is O(2^n) and the space complexity is O(2^n) due to the recursive nature of the solution.