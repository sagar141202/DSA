# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard stack operations: push, pop, and top. The push operation adds an element to the top of the stack, the pop operation removes an element from the top of the stack, and the top operation returns the element at the top of the stack without removing it. The implementation should be efficient in terms of time and space complexity.

## Approach
We can implement a stack using two queues by using one queue as the main storage and the other as a temporary queue to facilitate the stack operations. The push operation can be performed by adding the element to the main queue. The pop and top operations can be performed by moving elements from the main queue to the temporary queue until the last element is reached.

## Complexity
- Time: O(n) for pop and top operations, O(1) for push operation
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
Input: MyStack stack; stack.push(1); stack.push(2); stack.push(3); 
       stack.top(); stack.pop(); stack.empty();
Output: 3, 3, false
```

## Key Takeaways
- Use two queues to implement a stack, with one queue as the main storage and the other as a temporary queue.
- The push operation can be performed in O(1) time complexity by adding the element to the main queue and then moving elements from the main queue to the temporary queue.
- The pop and top operations can be performed in O(n) time complexity by moving elements from the main queue to the temporary queue until the last element is reached.