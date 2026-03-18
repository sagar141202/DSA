# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n`, generate all the `2^n` possible Gray codes of length `n`. For example, if `n = 2`, the Gray codes are `["00", "01", "11", "10"]`. If `n = 3`, the Gray codes are `["000", "001", "011", "010", "110", "111", "101", "100"]`. The output should be a list of all possible Gray codes in any order.

## Approach
The Gray code can be generated using recursion and backtracking. We start with the base case where `n = 1` and then recursively generate the Gray codes for `n > 1` by prefixing `0` and `1` to the Gray codes of `n - 1`. We use the property of Gray code that two successive values differ in only one bit.

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

// Alternative recursive solution
class SolutionRecursive {
public:
    vector<string> grayCode(int n) {
        vector<string> result;
        generateGrayCode(n, "", result);
        return result;
    }

    void generateGrayCode(int n, string current, vector<string>& result) {
        if (n == 0) {
            result.push_back(current);
            return;
        }
        generateGrayCode(n - 1, "0" + current, result);
        generateGrayCode(n - 1, "1" + current, result);
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
- The Gray code can be generated using bitwise operations, specifically the XOR operator.
- The recursive approach can be used to generate the Gray code by prefixing `0` and `1` to the Gray codes of `n - 1`.
- The time and space complexity of the solution is O(2^n) due to the recursive nature of the problem.