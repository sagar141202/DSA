# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The implementation should be efficient in terms of time and space complexity. For example, given the operations `push(1)`, `push(2)`, `pop()`, `push(3)`, `pop()`, the output should be `2`, `3`.

## Approach
We can use two queues to implement a stack. One queue will store the elements, and the other queue will be used to reverse the order of elements when a new element is added. When an element is pushed, we add it to the second queue and then move all elements from the first queue to the second queue.

## Complexity
- Time: O(n) for push operation (in the worst case when we need to move all elements from one queue to another), O(1) for pop operation
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
    // Push element x onto stack
    void push(int x) {
        q2.push(x);
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        swap(q1, q2);
    }

    // Removes the element on top of the stack
    void pop() {
        if (q1.empty()) {
            return;
        }
        q1.pop();
    }

    // Get the top element
    int top() {
        if (q1.empty()) {
            return -1;
        }
        return q1.front();
    }

    // Return whether the stack is empty
    bool empty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), pop(), push(3), pop()
Output: 2, 3
```

## Key Takeaways
- We use two queues to implement a stack, which allows for efficient push and pop operations.
- The push operation involves adding an element to the second queue and then moving all elements from the first queue to the second queue, resulting in a time complexity of O(n) in the worst case.
- The pop operation simply removes the front element from the first queue, resulting in a time complexity of O(1).