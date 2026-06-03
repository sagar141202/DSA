# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should have the basic methods: push, pop, and isEmpty. The push method adds an element to the top of the stack, the pop method removes an element from the top of the stack, and the isEmpty method checks if the stack is empty. The stack can contain any type of elements. For example, if we push elements 1, 2, and 3 in that order, the top of the stack should be 3, and popping the stack should return 3, then 2, then 1.

## Approach
We can use two queues to implement a stack. The first queue will be used to store the elements, and the second queue will be used as a temporary buffer to reverse the order of elements when pushing or popping. When pushing an element, we will add it to the end of the first queue, then move all elements from the first queue to the second queue, and finally swap the two queues. When popping an element, we will simply remove the front element from the first queue.

## Complexity
- Time: O(n) for push and pop operations in the worst case, where n is the number of elements in the stack
- Space: O(n) for storing the elements in the queues

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

    bool isEmpty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), push(3), pop(), pop()
Output: 3, 2
```

## Key Takeaways
- We can use two queues to implement a stack by using one queue for storing elements and the other queue as a temporary buffer.
- The time complexity of push and pop operations is O(n) in the worst case, where n is the number of elements in the stack.
- The space complexity is O(n) for storing the elements in the queues.