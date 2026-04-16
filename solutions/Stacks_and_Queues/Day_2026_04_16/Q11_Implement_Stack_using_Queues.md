# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. A stack is a LIFO (Last In First Out) data structure, meaning the last element added to the stack will be the first one to be removed. The stack should support the following operations: push, pop, top, and empty. The push operation adds an element to the top of the stack, the pop operation removes the top element from the stack, the top operation returns the top element of the stack, and the empty operation checks if the stack is empty. The input will be a series of push, pop, top, and empty operations, and the output should be the result of each operation.

## Approach
We can implement a stack using two queues by using one queue as the main stack and the other queue as a temporary queue. When pushing an element, we add it to the main queue. When popping an element, we move all elements except the last one to the temporary queue, remove the last element from the main queue, and then move all elements back to the main queue.

## Complexity
- Time: O(n) for pop operation, O(1) for push, top, and empty operations
- Space: O(n) where n is the number of elements in the stack

## C++ Solution
```cpp
#include <queue>
using namespace std;

class MyStack {
public:
    queue<int> q1, q2;
    
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
        if (q1.empty()) return -1;
        int x = q1.front();
        q1.pop();
        return x;
    }
    
    int top() {
        if (q1.empty()) return -1;
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
- We use two queues to implement a stack.
- The push operation involves adding an element to the end of the main queue and then moving all elements to the temporary queue.
- The pop operation involves removing the front element from the main queue.
- The top operation involves returning the front element from the main queue.
- The empty operation involves checking if the main queue is empty.