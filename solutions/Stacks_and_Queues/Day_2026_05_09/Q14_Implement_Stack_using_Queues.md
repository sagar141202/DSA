# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. Given two queues, q1 and q2, we need to implement the stack operations using these queues. The constraints are that we can only use the enqueue and dequeue operations on the queues. For example, if we have a stack with elements [1, 2, 3], the pop operation should return 3, and the stack should be left with elements [1, 2]. The push operation should add an element to the top of the stack.

## Approach
We will use two queues to implement the stack. The push operation will enqueue the new element into the first queue. The pop operation will dequeue all elements from the first queue and enqueue them into the second queue, except for the last element, which will be returned as the top element of the stack.

## Complexity
- Time: O(n) for pop operation, O(1) for push operation
- Space: O(n) for storing the elements in the queues

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Stack {
private:
    queue<int> q1;
    queue<int> q2;
public:
    void push(int x) {
        // simply enqueue the new element into q1
        q1.push(x);
    }

    int pop() {
        // check if q1 is empty
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        
        // dequeue all elements from q1 and enqueue them into q2, except for the last element
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        
        // the last element is the top of the stack, return it
        int top = q1.front();
        q1.pop();
        
        // swap q1 and q2
        queue<int> temp = q1;
        q1 = q2;
        q2 = temp;
        
        return top;
    }

    int top() {
        // similar to pop, but don't remove the top element
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        
        int top = q1.front();
        q2.push(q1.front());
        q1.pop();
        
        queue<int> temp = q1;
        q1 = q2;
        q2 = temp;
        
        return top;
    }

    bool empty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), push(3), pop(), top()
Output: 3, 2
```

## Key Takeaways
- We can implement a stack using two queues by using the enqueue and dequeue operations.
- The push operation has a time complexity of O(1), while the pop operation has a time complexity of O(n).
- The space complexity is O(n) for storing the elements in the queues.