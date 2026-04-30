# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return the result. The expression contains non-negative integers and operators `+`, `-`, `*`, `/`. The integer division should truncate toward zero. You cannot use any additional stack data structure, the recursive function call stack is also not allowed. For example, `3+2*2` = 7, ` 3/2 ` = 1, ` 3+5 / 2 ` = 5. Note that you should not use any additional stack data structure, the recursive function call stack is also not allowed.

## Approach
We use a simple iteration approach to solve this problem. We iterate over the string from left to right and update the result based on the current operator and the next number. We also maintain the last operator and the last number to handle the operator precedence.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int calculate(string s) {
        int num = 0;
        int result = 0;
        int lastSign = 1;
        int lastNum = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            } else if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') {
                if (lastSign == '*') {
                    result += lastNum * num;
                } else if (lastSign == '/') {
                    result += lastNum / num;
                } else {
                    result += lastSign * num;
                }
                lastSign = (s[i] == '+' ? 1 : -1);
                if (s[i] == '*') {
                    lastSign = lastSign * -1;
                    lastNum = num;
                } else if (s[i] == '/') {
                    lastSign = lastSign * -1;
                    lastNum = num;
                } else {
                    lastNum = num;
                }
                num = 0;
            }
        }
        if (lastSign == '*') {
            result += lastNum * num;
        } else if (lastSign == '/') {
            result += lastNum / num;
        } else {
            result += lastSign * num;
        }
        return result;
    }
};
```

## Test Cases
```
Input: "3+2*2"
Output: 7
Input: " 3/2 "
Output: 1
Input: " 3+5 / 2 "
Output: 5
```

## Key Takeaways
- We can solve this problem by simply iterating over the string and maintaining the last operator and the last number.
- We should handle the operator precedence by checking the current operator and updating the result accordingly.
- The time complexity of this solution is O(n) where n is the length of the string.