# Asteroid Collision

## Problem Statement
We are given an array of integers `asteroids` where each integer represents the size of an asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. When two asteroids collide, the larger one remains, and the smaller one is destroyed. If the two asteroids are of equal size, both are destroyed. The function should return the state of the asteroids after all collisions have occurred.

## Approach
We use a stack to store the asteroids. When a new asteroid is encountered, we check if it collides with the top asteroid on the stack. If it does, we compare their sizes and update the stack accordingly. This process continues until there are no more collisions.

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
        // Collision occurs when asteroid is moving left and top of stack is moving right
        while (!stack.empty() && asteroid < 0 && stack.back() > 0) {
            // If asteroid on top of stack is smaller, it gets destroyed
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            }
            // If asteroid on top of stack is equal, both get destroyed
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // If asteroid on top of stack is larger, new asteroid gets destroyed
            break;
        }
        // If the stack is empty or the asteroid is moving right, or the top of the stack is moving left, we add it to the stack
        if (stack.empty() || asteroid > 0 || stack.back() < 0) {
            stack.push_back(asteroid);
        }
    }
    return stack;
}
```

## Test Cases
```
Input: asteroids = [5,10,-5]
Output: [5,10]
Input: asteroids = [8,-8]
Output: []
Input: asteroids = [10,2,-5]
Output: [10]
Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
```

## Key Takeaways
- Use a stack to efficiently handle asteroid collisions.
- Compare the sizes of asteroids when a collision occurs to determine the outcome.
- Handle edge cases where the stack is empty or the asteroid is moving in the same direction as the top of the stack.