# Asteroid Collision

## Problem Statement
We are given an array of integers asteroids where asteroids[i] represents the size and direction of the ith asteroid. A positive integer represents an asteroid moving to the right, while a negative integer represents an asteroid moving to the left. If two asteroids collide, the larger one will remain, and the smaller one will be destroyed. If they are of the same size, both will be destroyed. The function should return the state of the asteroids after all collisions.

## Approach
The problem can be solved using a stack data structure. We iterate over the asteroids array and push each asteroid onto the stack. If a collision occurs, we compare the sizes of the asteroids and update the stack accordingly.

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
        // If the asteroid is moving to the right, or the stack is empty, or the top of the stack is moving to the left, we push it onto the stack
        if (asteroid > 0 || stack.empty() || stack.back() < 0) {
            stack.push_back(asteroid);
        } else {
            // If the asteroid is moving to the left and the top of the stack is moving to the right, we compare their sizes
            while (!stack.empty() && stack.back() > 0 && asteroid < 0) {
                // If the top of the stack is smaller, we pop it from the stack
                if (stack.back() < -asteroid) {
                    stack.pop_back();
                    continue;
                }
                // If the top of the stack is equal, we pop it from the stack and break the loop
                else if (stack.back() == -asteroid) {
                    stack.pop_back();
                }
                // If the top of the stack is larger, we break the loop
                break;
            }
            // If the stack is empty or the top of the stack is moving to the left, we push the asteroid onto the stack
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
- Use a stack data structure to keep track of the asteroids.
- Compare the sizes of the asteroids when a collision occurs.
- Update the stack accordingly based on the sizes of the asteroids.