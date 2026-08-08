# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, whereas a stack is a Last-In-First-Out (LIFO) data structure. The queue should support the following operations: `enqueue(x)` - add an element `x` to the end of the queue, `dequeue()` - remove an element from the front of the queue, and `isEmpty()` - check if the queue is empty. The input will be a sequence of these operations, and the output should be the result of each `dequeue` operation. The constraints are: 1 <= number of operations <= 10^5, and the input elements will be integers between 1 and 10^9.

## Approach
We will use two stacks to implement the queue. The first stack will store the new elements, and the second stack will store the elements in the correct order. When an element is added to the queue, it will be pushed onto the first stack. When an element is removed from the queue, we will pop elements from the first stack and push them onto the second stack until the first stack is empty, then we will pop the top element from the second stack.

## Complexity
- Time: O(1) for `enqueue` and `isEmpty` operations, O(n) for `dequeue` operation in the worst case, where n is the number of elements in the queue.
- Space: O(n), where n is the number of elements in the queue.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Queue {
private:
    stack<int> stackNewestOnTop; // stack to store new elements
    stack<int> stackOldestOnTop; // stack to store elements in correct order

public:
    void enqueue(int value) {
        // add new element to the top of the first stack
        stackNewestOnTop.push(value);
    }

    int dequeue() {
        // if both stacks are empty, the queue is empty
        if (stackNewestOnTop.empty() && stackOldestOnTop.empty()) {
            return -1; // or throw an exception
        }

        // if the second stack is empty, pop elements from the first stack and push them onto the second stack
        if (stackOldestOnTop.empty()) {
            while (!stackNewestOnTop.empty()) {
                stackOldestOnTop.push(stackNewestOnTop.top());
                stackNewestOnTop.pop();
            }
        }

        // pop the top element from the second stack
        int value = stackOldestOnTop.top();
        stackOldestOnTop.pop();
        return value;
    }

    bool isEmpty() {
        // check if both stacks are empty
        return stackNewestOnTop.empty() && stackOldestOnTop.empty();
    }
};

int main() {
    Queue queue;
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    cout << queue.dequeue() << endl; // prints 1
    cout << queue.dequeue() << endl; // prints 2
    cout << queue.isEmpty() << endl; // prints 0 (false)
    return 0;
}
```

## Test Cases
```
Input: enqueue(1), enqueue(2), enqueue(3), dequeue(), dequeue(), isEmpty()
Output: 1, 2, 0
```

## Key Takeaways
- We can implement a queue using two stacks, where the first stack stores new elements and the second stack stores elements in the correct order.
- The `enqueue` operation has a time complexity of O(1), while the `dequeue` operation has a time complexity of O(n) in the worst case.
- The space complexity of the implementation is O(n), where n is the number of elements in the queue.