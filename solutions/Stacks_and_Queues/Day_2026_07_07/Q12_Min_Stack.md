# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the `MinStack` class: 
- `MinStack()` Initializes the stack.
- `void push(int x)` Pushes element `x` onto the stack.
- `void pop()` Removes the element on top of the stack.
- `int top()` Gets the top element.
- `int getMin()` Retrieves the minimum element in the stack.
The stack will not be empty when `pop`, `top`, or `getMin` is called. The input will not exceed 10000 operations, and all operations will be valid.

## Approach
We will use two stacks to solve this problem, one for storing the actual elements and another for storing the minimum elements. The second stack will be updated whenever a new minimum element is found. This approach allows us to retrieve the minimum element in constant time.

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
        if (mainStack.top() == minStack.top()) {
            minStack.pop();
        }
        mainStack.pop();
    }

    int top() {
        return mainStack.top();
    }

    int getMin() {
        return minStack.top();
    }
};
```

## Test Cases
```
Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
Output: [null,null,null,null,-3,null,0,-2]
Explanation: 
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();     // return 0
minStack.getMin(); // return -2
```

## Key Takeaways
- Use of two stacks to store actual and minimum elements.
- The second stack is updated only when a new minimum element is found, allowing for constant time retrieval of the minimum element.
- This approach ensures efficient use of space and time, with O(1) time complexity for all operations and O(n) space complexity.