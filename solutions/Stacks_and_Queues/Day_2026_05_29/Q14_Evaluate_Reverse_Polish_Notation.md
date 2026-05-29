# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the expression in Reverse Polish Notation. The output should be the result of the evaluated expression. For example, the input ["2", "1", "+", "3", "*"] should return 9, because the expression is equivalent to (2 + 1) * 3. The input will not contain any division by zero.

## Approach
We will use a stack to store the operands and then pop them when we encounter an operator. The algorithm will iterate through the expression, pushing operands onto the stack and performing operations when it encounters an operator. The result will be the only element left in the stack after processing the entire expression.

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
        for (const string& token : tokens) {
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
Input: ["2","1","+","3","*"]
Output: 9
Input: ["4","13","5","/","+"]
Output: 6
Input: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

## Key Takeaways
- Use a stack to store operands in Reverse Polish Notation.
- Iterate through the expression and perform operations when encountering an operator.
- The result will be the only element left in the stack after processing the entire expression.