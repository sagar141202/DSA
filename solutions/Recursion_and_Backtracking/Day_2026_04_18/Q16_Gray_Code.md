# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer n, generate all the Gray codes of n bits. The output should be in ascending order. For example, if n = 2, the output should be ["00", "01", "11", "10"]. If n = 1, the output should be ["0", "1"].

## Approach
The algorithm uses recursion and backtracking to generate the Gray codes. It starts with the base case of n = 1 and then recursively generates the Gray codes for n bits by prefixing the Gray codes of (n-1) bits with 0 and 1. The key insight is to reverse the second half of the Gray codes of (n-1) bits when prefixing with 1.

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

// Alternatively, a recursive approach can be used
class SolutionRecursive {
public:
    vector<string> grayCode(int n) {
        vector<string> result;
        generateGrayCode(n, result);
        return result;
    }

    void generateGrayCode(int n, vector<string>& result) {
        if (n == 1) {
            result.push_back("0");
            result.push_back("1");
            return;
        }
        
        vector<string> prev;
        generateGrayCode(n - 1, prev);
        
        // Prefix the previous Gray codes with 0
        for (const string& code : prev) {
            result.push_back("0" + code);
        }
        
        // Reverse the previous Gray codes and prefix with 1
        for (int i = prev.size() - 1; i >= 0; i--) {
            result.push_back("1" + prev[i]);
        }
    }
};
```

## Test Cases
```
Input: n = 2
Output: [0, 1, 3, 2]
Input: n = 1
Output: [0, 1]
```

## Key Takeaways
- The Gray code can be generated using a simple bitwise XOR operation.
- A recursive approach can also be used to generate the Gray code by prefixing the previous Gray codes with 0 and 1.
- The time and space complexity of the solution is O(2^n) due to the recursive nature of the problem.