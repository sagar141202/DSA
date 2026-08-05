# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The expression is guaranteed to be valid, and there will not be any division by zero. For example, the expression ["2", "1", "+", "3", "*"] evaluates to (2 + 1) * 3 = 9.

## Approach
We can use a stack to store the intermediate results. When we encounter an operand, we push it to the stack. When we encounter an operator, we pop two operands from the stack, apply the operation, and push the result back to the stack. The final result will be the only element left in the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for (const auto& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int b = s.top(); s.pop();
                int a = s.top(); s.pop();
                if (token == "+") s.push(a + b);
                else if (token == "-") s.push(a - b);
                else if (token == "*") s.push(a * b);
                else s.push(a / b);
            } else {
                s.push(stoi(token));
            }
        }
        return s.top();
    }
};
```

## Test Cases
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Input: tokens = ["4","13","5","/","+"]
Output: 6
```

## Key Takeaways
- Use a stack to store intermediate results
- Process operators by popping operands, applying the operation, and pushing the result
- The final result will be the only element left in the stack after processing all tokens