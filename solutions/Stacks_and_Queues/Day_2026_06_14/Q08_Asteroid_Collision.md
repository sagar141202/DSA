# Asteroid Collision

## Problem Statement
We are given an array of integers `asteroids` where each integer represents the size of an asteroid. A positive integer represents an asteroid moving to the right, while a negative integer represents an asteroid moving to the left. When two asteroids collide, the larger one will destroy the smaller one. If both asteroids are of the same size, they will both be destroyed. We need to find the state of the asteroids after all collisions have occurred. The input array will contain at most 10000 asteroids, and the size of each asteroid will be between 1 and 1000.

## Approach
We will use a stack to keep track of the asteroids that have not been destroyed yet. When a new asteroid is encountered, we will compare its size with the size of the asteroid at the top of the stack. If the new asteroid is larger, we will pop the asteroid from the stack and continue this process until the stack is empty or the new asteroid is smaller.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> asteroidCollision(vector<int>& asteroids) {
    vector<int> stack;
    for (int asteroid : asteroids) {
        // if asteroid is moving to the right or stack is empty, push it to stack
        if (asteroid > 0 || stack.empty() || stack.back() < 0) {
            stack.push_back(asteroid);
        } else {
            // if asteroid is moving to the left and top of stack is moving to the right
            while (!stack.empty() && stack.back() > 0) {
                // if asteroid is smaller than top of stack, it will be destroyed
                if (stack.back() < -asteroid) {
                    stack.pop_back();
                    continue;
                }
                // if asteroid is same size as top of stack, both will be destroyed
                else if (stack.back() == -asteroid) {
                    stack.pop_back();
                }
                // if asteroid is larger than top of stack, top of stack will be destroyed
                break;
            }
            // if stack is empty or top of stack is moving to the left, push asteroid to stack
            if (stack.empty() || stack.back() < 0) {
                stack.push_back(asteroid);
            }
        }
    }
    return stack;
}
```

## Test Cases
```
Input: [5,10,-5]
Output: [5,10]
Input: [8,-8]
Output: []
Input: [10,2,-5]
Output: [10]
Input: [-2,-1,1,2]
Output: [-2,-1,1,2]
```

## Key Takeaways
- Use a stack to keep track of the asteroids that have not been destroyed yet.
- Compare the size of each new asteroid with the size of the asteroid at the top of the stack to determine the outcome of the collision.
- The time complexity is O(n) where n is the number of asteroids, and the space complexity is also O(n) as in the worst case, all asteroids will be stored in the stack.