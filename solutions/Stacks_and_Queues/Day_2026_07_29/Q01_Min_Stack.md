# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should handle duplicates and negative numbers. For example, given the sequence of operations `push(1)`, `push(2)`, `push(0)`, `min()`, `pop()`, `top()`, `min()`, the output should be `0`, `1`, `0`. The constraints are that all operations should be performed in O(1) time complexity.

## Approach
We can use two stacks to solve this problem: one for storing the actual elements and another for keeping track of the minimum elements. The algorithm involves pushing and popping elements from both stacks simultaneously to maintain the minimum element at the top of the second stack.

## Complexity
- Time: O(1)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MinStack {
private:
    stack<int> mainStack;
    stack<int> minStack;

public:
    void push(int x) {
        mainStack.push(x);
        if (minStack.empty() || x <= minStack.top()) {
            minStack.push(x);
        }
    }

    void pop() {
        if (!mainStack.empty()) {
            if (mainStack.top() == minStack.top()) {
                minStack.pop();
            }
            mainStack.pop();
        }
    }

    int top() {
        return mainStack.top();
    }

    int getMin() {
        return minStack.top();
    }
};

// Example usage
int main() {
    MinStack minStack;
    minStack.push(1);
    minStack.push(2);
    minStack.push(0);
    cout << minStack.getMin() << endl;  // Output: 0
    minStack.pop();
    cout << minStack.top() << endl;     // Output: 2
    cout << minStack.getMin() << endl;  // Output: 1
    return 0;
}
```

## Test Cases
```
Input: push(1), push(2), push(0), min(), pop(), top(), min()
Output: 0, 2, 1
Input: push(-2), push(0), push(-3), min(), pop(), top(), getMin()
Output: -3, 0, -2
```

## Key Takeaways
- Use two stacks to keep track of the minimum element and the actual elements.
- Push and pop elements from both stacks simultaneously to maintain the minimum element at the top of the second stack.
- Handle edge cases such as empty stacks and duplicates.