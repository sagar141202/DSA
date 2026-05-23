# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings, where each string is either an integer or an operator. For example, the expression "3+4*2" can be represented as ["3", "+", "4", "*", "2"]. The expression "10/2" can be represented as ["10", "/", "2"]. The division operator / only performs integer division. The input array does not contain any division by zero. The input array is not empty. The input array contains between 1 and 30 elements. The elements in the input array contain only digits 0-9, +, -, *, or /. The elements in the input array are not empty.

## Approach
We will use a stack to store the intermediate results. We iterate over the input array and if the current element is a number, we push it to the stack. If the current element is an operator, we pop two numbers from the stack, apply the operation, and push the result back to the stack. At the end, the stack will contain a single element which is the result of the expression.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <stack>
#include <vector>
#include <string>

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<int> stack;
        for (const auto& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int b = stack.top();
                stack.pop();
                int a = stack.top();
                stack.pop();
                if (token == "+") {
                    stack.push(a + b);
                } else if (token == "-") {
                    stack.push(a - b);
                } else if (token == "*") {
                    stack.push(a * b);
                } else {
                    stack.push(a / b);
                }
            } else {
                stack.push(std::stoi(token));
            }
        }
        return stack.top();
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
- Use a stack to store intermediate results.
- Iterate over the input array and apply operators to the top two elements of the stack.
- At the end, the stack will contain a single element which is the result of the expression.
- The time complexity is O(n) where n is the number of elements in the input array.
- The space complexity is O(n) where n is the number of elements in the input array.