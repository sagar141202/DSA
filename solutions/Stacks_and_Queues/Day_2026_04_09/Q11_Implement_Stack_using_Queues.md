# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The stack is empty if both queues are empty. For example, if we push elements 1, 2, and 3, the top of the stack should be 3. If we pop an element, it should return 3, and the top of the stack should be 2.

## Approach
We will use two queues to implement the stack. The first queue will store the elements of the stack, and the second queue will be used to rotate the elements when a new element is pushed. When an element is pushed, it will be added to the second queue, and then all elements from the first queue will be moved to the second queue. This way, the most recently added element will be at the front of the first queue, which will be the top of the stack.

## Complexity
- Time: O(n) for push operation, O(1) for pop operation
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
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
Input: MyStack stack; stack.push(1); stack.push(2); stack.push(3); stack.pop();
Output: 3
Input: MyStack stack; stack.push(1); stack.push(2); stack.top();
Output: 2
Input: MyStack stack; stack.empty();
Output: true
```

## Key Takeaways
- We use two queues to implement a stack, where one queue stores the elements and the other queue is used to rotate the elements when a new element is pushed.
- The push operation takes O(n) time, where n is the number of elements in the stack, because we need to rotate all elements when a new element is pushed.
- The pop operation takes O(1) time, because we simply remove the front element from the first queue.