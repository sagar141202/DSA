# Asteroid Collision

## Problem Statement
We are given an array asteroids where asteroids[i] represents the size and direction of an asteroid. If the size is positive, the asteroid is moving to the right, and if it is negative, the asteroid is moving to the left. When two asteroids collide, the larger one will destroy the smaller one. If both asteroids have the same size, they will both be destroyed. The task is to return the state of the asteroids after all collisions have occurred. The input array will have between 1 and 10000 elements, and each element will be between -1000 and 1000.

## Approach
We use a stack to keep track of the asteroids that have not been destroyed yet. For each asteroid, we check if it will collide with the asteroid at the top of the stack. If it does, we compare their sizes and update the stack accordingly. This process continues until there are no more collisions.

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
                // if top of stack is smaller, remove it
                if (stack.back() < -asteroid) {
                    stack.pop_back();
                    continue;
                } 
                // if top of stack is equal, remove both
                else if (stack.back() == -asteroid) {
                    stack.pop_back();
                }
                // if top of stack is larger, asteroid is destroyed
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
- Compare the size of each asteroid with the top of the stack to determine the outcome of a collision.
- Handle the cases where an asteroid is destroyed, or both asteroids are destroyed when they have the same size.