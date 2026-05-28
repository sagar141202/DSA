# Asteroid Collision

## Problem Statement
We are given an array of integers `asteroids` where each integer represents the size of an asteroid. The asteroids are moving in two directions, either to the left or to the right. If two asteroids collide, the larger one will remain and the smaller one will be destroyed. If they are of the same size, both will be destroyed. The goal is to find the state of the asteroids after all collisions have occurred.

## Approach
The problem can be solved using a stack data structure, where we iterate through the asteroids and push them onto the stack if they are moving to the right. If an asteroid is moving to the left, we pop asteroids from the stack that are smaller than the current asteroid until we find a larger asteroid or the stack is empty.

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
        // If the asteroid is moving to the right or the stack is empty, push it onto the stack
        if (asteroid > 0 || stack.empty() || stack.back() < 0) {
            stack.push_back(asteroid);
        } else {
            // If the asteroid is moving to the left and the top of the stack is moving to the right
            while (!stack.empty() && stack.back() > 0 && stack.back() < -asteroid) {
                stack.pop_back();
            }
            // If the stack is empty or the top of the stack is moving to the left, push the asteroid onto the stack
            if (stack.empty() || stack.back() < 0) {
                stack.push_back(asteroid);
            } 
            // If the top of the stack is equal to the asteroid, pop it from the stack
            else if (stack.back() == -asteroid) {
                stack.pop_back();
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
- Iterate through the asteroids and push them onto the stack if they are moving to the right.
- If an asteroid is moving to the left, pop asteroids from the stack that are smaller than the current asteroid until we find a larger asteroid or the stack is empty.
- If the top of the stack is equal to the asteroid, pop it from the stack.