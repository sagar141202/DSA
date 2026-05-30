# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should be able to handle duplicate elements and should not use any extra space that scales with input size other than the stack itself. The constraints are: -2^31 <= x <= 2^31 - 1, where x is the value of the element to be pushed. The example usage is: MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); // return -3 minStack.pop(); minStack.top(); // return 0 minStack.getMin(); // return -2.

## Approach
We will use two stacks, one to store the actual elements and another to store the minimum elements seen so far. The min stack will be updated whenever a smaller element is pushed onto the main stack. This way, the top of the min stack will always contain the minimum element in the main stack.

## Complexity
- Time: O(1)
- Space: O(n)

## C++ Solution
```cpp
#include <stack>
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
        if (!mainStack.empty()) {
            return mainStack.top();
        }
        return -1; // or throw an exception
    }

    int getMin() {
        if (!minStack.empty()) {
            return minStack.top();
        }
        return -1; // or throw an exception
    }
};
```

## Test Cases
```
Input: 
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
Output: 
minStack.getMin(); // return -3
minStack.pop();
minStack.top(); // return 0
minStack.getMin(); // return -2
```

## Key Takeaways
- We use two stacks to keep track of the minimum element in the main stack.
- The min stack is updated only when a smaller element is pushed onto the main stack.
- The time complexity of all operations (push, pop, top, getMin) is O(1) because we are using stacks.