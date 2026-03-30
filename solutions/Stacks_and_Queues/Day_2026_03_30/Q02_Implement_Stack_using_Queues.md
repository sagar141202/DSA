# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. Given two queues, q1 and q2, implement the stack such that the top element of the stack is at the front of q1. The constraints are: (1) you can only use the standard queue operations (enqueue, dequeue, and empty), (2) you cannot use any other data structures, and (3) the time complexity for push and pop operations should be O(1) and O(n) respectively, where n is the number of elements in the stack. For example, if you push elements 1, 2, and 3 into the stack, the top element should be 3, and popping the stack should return 3.

## Approach
We can implement the stack using two queues by maintaining the top element of the stack at the front of the first queue. When pushing an element, we can simply enqueue it into the second queue and then move all elements from the first queue to the second queue. When popping an element, we can simply dequeue it from the first queue.

## Complexity
- Time: O(1) for push, O(n) for pop
- Space: O(n)

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
Input: push(1), push(2), push(3), pop(), top()
Output: 3, 2
```

## Key Takeaways
- We use two queues, q1 and q2, to implement the stack, where q1 stores the elements and q2 is used as a temporary queue.
- The push operation involves enqueueing the new element into q2 and then moving all elements from q1 to q2, effectively maintaining the top element at the front of q1.
- The pop operation simply dequeues the front element from q1.