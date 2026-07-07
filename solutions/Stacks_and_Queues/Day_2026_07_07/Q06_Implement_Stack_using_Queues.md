# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard stack operations: push, pop, and top. The push operation adds an element to the top of the stack, the pop operation removes an element from the top of the stack, and the top operation returns the element at the top of the stack without removing it. You can only use queues for this implementation. The input will be a series of commands where 'push' adds an element to the stack, 'pop' removes an element from the stack, and 'top' returns the top element of the stack. The constraints are that the input will consist of at most 100 commands and each element will be an integer between 1 and 100.

## Approach
We will use two queues to implement the stack. One queue will be used to store the elements and the other queue will be used to rotate the elements to the front when a push or pop operation is performed. This way, the front of the queue will always represent the top of the stack. We will use the standard queue operations: enqueue and dequeue.

## Complexity
- Time: O(n) for pop operation in the worst case, O(1) for push and top operations
- Space: O(n) where n is the number of elements in the stack

## C++ Solution
```cpp
#include <queue>
using namespace std;

class MyStack {
private:
    queue<int> q1;
    queue<int> q2;
public:
    MyStack() {}

    void push(int x) {
        q2.push(x);
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        swap(q1, q2);
    }

    int pop() {
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        int top = q1.front();
        q1.pop();
        return top;
    }

    int top() {
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        return q1.front();
    }

    bool empty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), top(), pop(), empty()
Output: 2, 2, false
```

## Key Takeaways
- Use two queues to implement a stack, one for storing elements and the other for rotating elements to the front.
- The front of the queue represents the top of the stack.
- The time complexity of the pop operation is O(n) in the worst case, where n is the number of elements in the stack.