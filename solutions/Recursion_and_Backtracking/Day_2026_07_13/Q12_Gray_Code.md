# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given an integer `n`, generate all `n`-bit Gray codes in ascending order. For example, if `n = 2`, the output should be `["00", "01", "11", "10"]`. If `n = 3`, the output should be `["000", "001", "011", "010", "110", "111", "101", "100"]`. The input `n` will be between 1 and 16.

## Approach
The algorithm uses recursion and backtracking to generate all possible Gray codes. We start with the base case where `n = 1` and then recursively generate the Gray codes for `n` by reflecting and prefixing the Gray codes for `n-1`. This approach ensures that the generated codes differ by only one bit.

## Complexity
- Time: O(2^n)
- Space: O(2^n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
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
        
        for (const string& code : prev) {
            result.push_back("0" + code);
        }
        
        reverse(prev.begin(), prev.end());
        
        for (const string& code : prev) {
            result.push_back("1" + code);
        }
    }
};

int main() {
    Solution solution;
    vector<string> result = solution.grayCode(3);
    for (const string& code : result) {
        cout << code << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 2
Output: ["00", "01", "11", "10"]
Input: 3
Output: ["000", "001", "011", "010", "110", "111", "101", "100"]
```

## Key Takeaways
- The Gray code sequence has the property that each code differs from the previous one by only one bit.
- The recursive approach can be used to generate the Gray codes by reflecting and prefixing the previous codes.
- The time complexity of the solution is exponential due to the recursive nature of the problem.