# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. Given two queues, q1 and q2, implement the stack such that the top element of the stack is the front element of q1. The stack should be able to handle duplicate elements and should not use any other data structure except the two queues. The push operation should add an element to the top of the stack, and the pop operation should remove the top element from the stack. The implementation should handle edge cases such as an empty stack.

## Approach
We will use two queues to implement the stack, where one queue will be used to store the elements and the other queue will be used to support the push and pop operations. When an element is pushed onto the stack, it will be added to the end of the first queue. When an element is popped from the stack, all elements except the front element will be moved to the second queue, and then the front element will be removed from the first queue.

## Complexity
- Time: O(n) for pop operation and O(1) for push operation
- Space: O(n) where n is the number of elements in the stack

## C++ Solution
```cpp
#include <queue>
using namespace std;

class Stack {
private:
    queue<int> q1;
    queue<int> q2;

public:
    void push(int x) {
        // Add the element to the end of q1
        q1.push(x);
    }

    void pop() {
        // Check if the stack is empty
        if (q1.empty()) {
            return;
        }

        // Move all elements except the front element to q2
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }

        // Remove the front element from q1
        int front = q1.front();
        q1.pop();

        // Swap q1 and q2
        queue<int> temp = q1;
        q1 = q2;
        q2 = temp;
    }

    int top() {
        // Check if the stack is empty
        if (q1.empty()) {
            return -1;
        }

        // Move all elements except the front element to q2
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }

        // Get the front element from q1
        int front = q1.front();

        // Add the front element back to q1
        q2.push(front);
        q1 = q2;
        queue<int> temp;
        q2 = temp;

        return front;
    }

    bool empty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), push(3), pop(), top()
Output: 2
```

## Key Takeaways
- We can implement a stack using two queues by using one queue to store the elements and the other queue to support the push and pop operations.
- The time complexity of the pop operation is O(n) because we need to move all elements except the front element to the other queue.
- The space complexity is O(n) where n is the number of elements in the stack.