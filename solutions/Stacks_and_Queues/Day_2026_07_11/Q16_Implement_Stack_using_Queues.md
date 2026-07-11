# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The problem has the following constraints: (1) the input will contain a sequence of push and pop operations, (2) the input will not contain any invalid operations (e.g., popping from an empty stack), and (3) the maximum number of elements in the stack at any time will be 10^5. For example, given the sequence of operations [push(1), push(2), pop, push(3), pop, pop], the output should be [1, 3].

## Approach
We can implement a stack using two queues by utilizing the fact that a queue is a First-In-First-Out (FIFO) data structure. To achieve the Last-In-First-Out (LIFO) behavior of a stack, we can use one queue to store the elements and the other queue to temporary hold the elements when we need to push or pop an element. We will use the standard queue operations enqueue and dequeue to implement the push and pop operations of the stack.

## Complexity
- Time: O(n) for the pop operation in the worst case, where n is the number of elements in the queue, and O(1) for the push operation.
- Space: O(n) for storing the elements in the queues, where n is the maximum number of elements in the stack.

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
        int front = q1.front();
        q1.pop();
        return front;
    }
    
    int top() {
        return q1.front();
    }
    
    bool empty() {
        return q1.empty();
    }
};

int main() {
    MyStack stack;
    stack.push(1);
    stack.push(2);
    cout << stack.pop() << endl;  // prints 2
    stack.push(3);
    cout << stack.pop() << endl;  // prints 3
    cout << stack.pop() << endl;   // prints 1
    return 0;
}
```

## Test Cases
```
Input: push(1), push(2), pop, push(3), pop, pop
Output: 2, 3, 1
Input: push(1), pop, push(2), push(3), pop
Output: 1, 3
```

## Key Takeaways
- We can use two queues to implement a stack by utilizing the FIFO behavior of the queues to achieve the LIFO behavior of the stack.
- The push operation involves adding the new element to the second queue, moving all elements from the first queue to the second queue, and then swapping the two queues.
- The pop operation simply involves removing the front element from the first queue.