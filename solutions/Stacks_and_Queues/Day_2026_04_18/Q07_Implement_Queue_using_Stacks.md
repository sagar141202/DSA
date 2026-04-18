# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element that is added will be the first one to be removed. The queue should support the following operations: `enqueue(element)`, `dequeue()`, `isEmpty()`, and `size()`. The `enqueue(element)` operation adds an element to the end of the queue, the `dequeue()` operation removes an element from the front of the queue, the `isEmpty()` operation checks if the queue is empty, and the `size()` operation returns the number of elements in the queue. The input will be a series of operations, and the output will be the result of each operation.

## Approach
We can use two stacks to implement a queue. The first stack will be used to store new elements, and the second stack will be used to store elements in the correct order. When an element is added to the queue, it will be pushed onto the first stack. When an element is removed from the queue, the elements will be popped from the first stack and pushed onto the second stack, effectively reversing the order of the elements.

## Complexity
- Time: O(1) for `enqueue` and `isEmpty`, O(n) for `dequeue` in the worst case
- Space: O(n)

## C++ Solution
```cpp
#include <stack>
using namespace std;

class Queue {
private:
    stack<int> stack1;
    stack<int> stack2;

public:
    void enqueue(int element) {
        // Add an element to the end of the queue
        stack1.push(element);
    }

    int dequeue() {
        // Remove an element from the front of the queue
        if (stack2.empty()) {
            // If the second stack is empty, move elements from the first stack to the second stack
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        if (stack2.empty()) {
            // If the queue is empty, throw an exception
            throw runtime_error("Queue is empty");
        }
        int element = stack2.top();
        stack2.pop();
        return element;
    }

    bool isEmpty() {
        // Check if the queue is empty
        return stack1.empty() && stack2.empty();
    }

    int size() {
        // Return the number of elements in the queue
        return stack1.size() + stack2.size();
    }
};
```

## Test Cases
```
Input: 
enqueue(1)
enqueue(2)
enqueue(3)
dequeue()
isEmpty()
size()
Output: 
1
false
2
```

## Key Takeaways
- A queue can be implemented using two stacks, where one stack is used to store new elements and the other stack is used to store elements in the correct order.
- The `dequeue` operation has a time complexity of O(n) in the worst case, where n is the number of elements in the queue.
- The `enqueue` and `isEmpty` operations have a time complexity of O(1).