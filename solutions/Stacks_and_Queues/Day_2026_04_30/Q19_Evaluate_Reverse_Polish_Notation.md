# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input string array contains valid Reverse Polish Notation expressions. The array does not contain empty strings. The input is guaranteed to be valid and will not cause a division by zero. For example, given the tokens ["2", "1", "+", "3", "*"], return 9 because ((2 + 1) * 3) = 9.

## Approach
We can use a stack-based approach to solve this problem by iterating over the tokens and pushing operands onto the stack. When an operator is encountered, we pop the top two elements from the stack, apply the operation, and push the result back onto the stack. The final result will be the only element left in the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <stack>
#include <vector>
#include <string>
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
- Use a stack to store operands and intermediate results.
- Iterate over the tokens and apply operators to the top two elements of the stack.
- Handle division by zero by checking the input constraints.
- The final result will be the only element left in the stack after processing all tokens.