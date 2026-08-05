# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The problem has the following constraints: (1) the stack should be implemented using only two queues, (2) the push and pop operations should have a time complexity of O(n) in the worst case, and (3) the space complexity should be O(n), where n is the number of elements in the stack. For example, if we push the elements 1, 2, and 3 onto the stack, the top of the stack should be 3, and popping the stack should return 3.

## Approach
We will use two queues, q1 and q2, to implement the stack. The push operation will add an element to the end of q1, and then we will move all elements from q1 to q2, except the newly added element, which will be at the front of q1. The pop operation will simply remove the front element from q1.

## Complexity
- Time: O(n)
- Space: O(n)

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
        q1.push(x);
        while (!q2.empty()) {
            q1.push(q2.front());
            q2.pop();
        }
        queue<int> temp = q1;
        q1 = q2;
        q2 = temp;
    }

    int pop() {
        if (q2.empty()) {
            return -1; // or throw an exception
        }
        int top = q2.front();
        q2.pop();
        return top;
    }

    int top() {
        if (q2.empty()) {
            return -1; // or throw an exception
        }
        return q2.front();
    }

    bool empty() {
        return q2.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), push(3), pop(), top()
Output: 3, 2
```

## Key Takeaways
- We can implement a stack using two queues, where the push operation has a time complexity of O(n) due to the movement of elements between queues.
- The pop operation has a time complexity of O(1) since we simply remove the front element from the queue.
- The space complexity is O(n), where n is the number of elements in the stack.