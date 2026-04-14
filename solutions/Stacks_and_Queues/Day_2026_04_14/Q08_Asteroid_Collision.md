# Asteroid Collision

## Problem Statement
We are given an array asteroids where asteroids[i] represents the size and direction of the ith asteroid. The size will be a positive integer, and the direction will be either 1 (moving to the right) or -1 (moving to the left). If two asteroids collide, the larger one will remain, and the smaller one will be destroyed. If both asteroids are of the same size, they will both be destroyed. The function should return the state of the asteroids after all collisions.

## Approach
We use a stack to track the asteroids. When a new asteroid is encountered, we check if it collides with the top asteroid on the stack. If it does, we compare their sizes and update the stack accordingly. This process continues until there are no more collisions.

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
        bool collision = false;
        while (!stack.empty() && asteroid < 0 && stack.back() > 0) {
            // If asteroid on stack is smaller, it gets destroyed
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            }
            // If both asteroids are of same size, they both get destroyed
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // If asteroid on stack is larger, new asteroid gets destroyed
            collision = true;
            break;
        }
        // If no collision or asteroid survived collision, add it to stack
        if (!collision) {
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
```

## Key Takeaways
- Use a stack to track the asteroids and handle collisions efficiently.
- Compare the sizes of colliding asteroids to determine the outcome.
- Handle cases where asteroids have the same size and both get destroyed.