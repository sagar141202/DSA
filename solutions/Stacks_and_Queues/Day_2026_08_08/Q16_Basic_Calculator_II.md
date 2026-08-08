# Basic Calculator II

## Problem Statement
Given a string s which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers and operators (+, -, \*, /) with no parentheses. Operators have the usual precedence, and the expression is evaluated from left to right. For example, 3+2\*2 = 7 and 1+2+3\*4 = 15. Assume that the input expression is always valid and does not contain any spaces.

## Approach
We will use a stack-based approach to evaluate the expression. We will iterate through the string from left to right, using two stacks to store the numbers and operators. When we encounter an operator with higher or equal precedence, we will pop the operator and the top two numbers from the stacks, perform the operation, and push the result back into the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    int calculate(string s) {
        stack<int> nums;
        char sign = '+';
        int currNum = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isdigit(s[i])) {
                currNum = currNum * 10 + (s[i] - '0');
            }
            if (!isdigit(s[i]) && !isspace(s[i]) || i == s.length() - 1) {
                if (sign == '+') {
                    nums.push(currNum);
                } else if (sign == '-') {
                    nums.push(-currNum);
                } else if (sign == '*') {
                    nums.top() *= currNum;
                } else if (sign == '/') {
                    nums.top() /= currNum;
                }
                sign = s[i];
                currNum = 0;
            }
        }
        int result = 0;
        while (!nums.empty()) {
            result += nums.top();
            nums.pop();
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
- Use a stack to store the intermediate results.
- Iterate through the string from left to right and update the stack accordingly.
- Use a variable to keep track of the current operator.