# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element that is added will be the first one to be removed. The queue should support the following operations: `enqueue(element)`, `dequeue()`, `isEmpty()`, and `size()`. The input will be a series of these operations, and the output should be the result of each operation. For example, if we have the operations `enqueue(1)`, `enqueue(2)`, `dequeue()`, `enqueue(3)`, `dequeue()`, the output should be `1`, `2`.

## Approach
We can use two stacks to implement a queue. The first stack will be used to store the elements as they are added, and the second stack will be used to store the elements in the correct order for removal. When an element is added, it is pushed onto the first stack. When an element is removed, the elements are popped from the first stack and pushed onto the second stack, effectively reversing the order.

## Complexity
- Time: O(1) for `enqueue` and `isEmpty` operations, O(n) for `dequeue` operation in the worst case
- Space: O(n), where n is the number of elements in the queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Queue {
private:
    stack<int> stack1;
    stack<int> stack2;

public:
    void enqueue(int element) {
        // Add element to the first stack
        stack1.push(element);
    }

    int dequeue() {
        // If the second stack is empty, pop all elements from the first stack and push them onto the second stack
        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        // Pop the top element from the second stack
        int top = stack2.top();
        stack2.pop();
        return top;
    }

    bool isEmpty() {
        // Check if both stacks are empty
        return stack1.empty() && stack2.empty();
    }

    int size() {
        // Return the total number of elements in both stacks
        return stack1.size() + stack2.size();
    }
};

int main() {
    Queue queue;
    queue.enqueue(1);
    queue.enqueue(2);
    cout << queue.dequeue() << endl;  // Output: 1
    queue.enqueue(3);
    cout << queue.dequeue() << endl;  // Output: 2
    return 0;
}
```

## Test Cases
```
Input: enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue()
Output: 1, 2
```

## Key Takeaways
- We can use two stacks to implement a queue, with one stack storing the elements as they are added and the other stack storing the elements in the correct order for removal.
- The `dequeue` operation has a time complexity of O(n) in the worst case because we need to pop all elements from the first stack and push them onto the second stack.
- The `enqueue` and `isEmpty` operations have a time complexity of O(1) because we only need to push an element onto the first stack or check if both stacks are empty.