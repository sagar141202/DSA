# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard stack operations: push, pop, top, and empty. The push operation adds an element to the top of the stack, the pop operation removes the top element from the stack, the top operation returns the top element of the stack without removing it, and the empty operation checks if the stack is empty. The queues should be used to implement the stack, and the solution should be efficient in terms of time and space complexity. For example, given the operations ["MyStack", "push", "push", "top", "pop", "empty"], the output should be [null, null, null, 2, 2, false] for the input [[], [1], [2], [], [], []].

## Approach
We can implement a stack using two queues by using one queue to store the elements and the other queue to temporarily hold the elements when we need to add or remove an element from the top of the stack. We can use the enqueue and dequeue operations of the queues to implement the push and pop operations of the stack.

## Complexity
- Time: O(1) for push, O(n) for pop, top, and empty
- Space: O(n)

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
Input: MyStack stack = new MyStack();
       stack.push(1);
       stack.push(2);
       stack.top(); // returns 2
       stack.pop(); // returns 2
       stack.empty(); // returns false
Output: [null, null, null, 2, 2, false]
```

## Key Takeaways
- We can implement a stack using two queues by using one queue to store the elements and the other queue to temporarily hold the elements when we need to add or remove an element from the top of the stack.
- The push operation takes O(n) time complexity because we need to move all elements from one queue to the other.
- The pop, top, and empty operations take O(1) time complexity because we can directly access the front element of the queue.