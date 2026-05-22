# Asteroid Collision

## Problem Statement
We are given an array of integers representing asteroids, where each integer represents the size of an asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. If two asteroids collide, the larger one will destroy the smaller one. If the two asteroids are of the same size, they will both be destroyed. The goal is to determine the state of the asteroids after all collisions have occurred.

## Approach
We will use a stack to keep track of the asteroids. We iterate through the array, and for each asteroid, we check if it collides with the asteroid at the top of the stack. If it does, we compare their sizes and update the stack accordingly.

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
        // collision occurs when asteroid is moving left and top of stack is moving right
        bool collision = false;
        while (!stack.empty() && asteroid < 0 && stack.back() > 0) {
            // if asteroid is larger than top of stack, destroy top of stack
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            }
            // if asteroid is same size as top of stack, destroy both
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // if asteroid is smaller than top of stack, destroy asteroid
            collision = true;
            break;
        }
        // if no collision or asteroid is larger, add to stack
        if (!collision) {
            stack.push_back(asteroid);
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
- Use a stack to keep track of the asteroids.
- Iterate through the array and check for collisions with the top of the stack.
- Update the stack based on the size of the asteroids in the collision.