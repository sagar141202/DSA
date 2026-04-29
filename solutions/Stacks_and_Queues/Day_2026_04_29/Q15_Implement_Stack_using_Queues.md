# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. Given two queues, `q1` and `q2`, where `q1` is used to store the elements and `q2` is used to support the pop operation, design a class `Stack` with methods `push(int x)` and `int pop()`. The `push(int x)` method adds an element `x` to the stack, and the `int pop()` method removes an element from the stack and returns it. If the stack is empty, the `pop()` method should return `-1`. The stack should follow the LIFO (Last-In-First-Out) principle.

## Approach
We will use two queues, `q1` and `q2`, to implement the stack. The `push` operation will add an element to the end of `q1`. For the `pop` operation, we will transfer all elements from `q1` to `q2` except the last one, which will be removed and returned.

## Complexity
- Time: O(n) for pop operation, O(1) for push operation
- Space: O(n) where n is the number of elements in the stack

## C++ Solution
```cpp
#include <queue>
using namespace std;

class Stack {
private:
    queue<int> q1;
    queue<int> q2;

public:
    // Push element x onto stack
    void push(int x) {
        q1.push(x);
    }

    // Removes the element on top of the stack and returns that element
    int pop() {
        if (q1.empty()) {
            return -1; // return -1 if stack is empty
        }

        // transfer all elements from q1 to q2 except the last one
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }

        // store the last element (top of the stack)
        int top = q1.front();
        q1.pop();

        // swap q1 and q2
        swap(q1, q2);

        return top;
    }
};
```

## Test Cases
```
Input: push(1), push(2), push(3), pop(), pop()
Output: 3, 2
```

## Key Takeaways
- We use two queues, `q1` and `q2`, to implement the stack.
- The `push` operation is straightforward and adds an element to the end of `q1`.
- The `pop` operation involves transferring elements from `q1` to `q2` and removing the last element from `q1`.