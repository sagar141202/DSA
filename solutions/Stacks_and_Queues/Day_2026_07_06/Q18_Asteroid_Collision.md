# Asteroid Collision

## Problem Statement
We are given an array of integers `asteroids` where each integer represents the size of an asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. If two asteroids collide, the larger one will destroy the smaller one. If they are of the same size, both will be destroyed. The function should return the state of the asteroids after all collisions have occurred.

## Approach
We will use a stack to track the asteroids. We iterate through the asteroids, and if the stack is empty or the top asteroid is moving to the left and the current asteroid is moving to the right, we push the current asteroid to the stack. If the top asteroid is moving to the right and the current asteroid is moving to the left, we compare their sizes and handle the collision accordingly.

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
        // If the asteroid is moving to the right or the stack is empty, push it to the stack
        if (asteroid > 0 || stack.empty() || stack.back() < 0) {
            stack.push_back(asteroid);
        } else {
            // If the asteroid is moving to the left and the top asteroid is moving to the right
            while (!stack.empty() && stack.back() > 0) {
                // If the top asteroid is smaller than the current asteroid, pop it from the stack
                if (stack.back() < -asteroid) {
                    stack.pop_back();
                    continue;
                }
                // If the top asteroid is the same size as the current asteroid, pop it from the stack and break the loop
                else if (stack.back() == -asteroid) {
                    stack.pop_back();
                }
                // If the top asteroid is larger than the current asteroid, break the loop
                break;
            }
            // If the stack is empty or the top asteroid is moving to the left, push the current asteroid to the stack
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
- Use a stack to efficiently track the asteroids and handle collisions.
- Compare the sizes of the asteroids when they collide to determine the outcome.
- Handle the cases where the asteroids are of the same size or one is larger than the other.