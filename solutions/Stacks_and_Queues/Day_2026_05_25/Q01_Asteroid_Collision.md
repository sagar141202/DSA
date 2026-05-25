# Asteroid Collision

## Problem Statement
We are given an array of integers representing the masses of asteroids, where a positive mass represents an asteroid moving to the right and a negative mass represents an asteroid moving to the left. If two asteroids collide, the asteroid with the larger mass will survive and continue moving in its original direction, while the asteroid with the smaller mass will be destroyed. If the masses of the two asteroids are equal, both will be destroyed. The goal is to determine the state of the asteroids after all collisions have occurred.

## Approach
We can use a stack to keep track of the asteroids. When a new asteroid is encountered, we compare its mass with the mass of the asteroid at the top of the stack. If the new asteroid has a larger mass, we pop the top asteroid from the stack and continue this process until the stack is empty or the new asteroid has a smaller mass.

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
        // Collision occurs when asteroid is moving left (negative mass)
        // and the top of the stack has a positive mass
        bool collision = false;
        while (!stack.empty() && asteroid < 0 && stack.back() > 0) {
            // If the top asteroid has a smaller mass, it gets destroyed
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            }
            // If the top asteroid has the same mass, both get destroyed
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // If the top asteroid has a larger mass, the new asteroid gets destroyed
            collision = true;
            break;
        }
        // If no collision or the new asteroid survived the collision, add it to the stack
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
- Use a stack to efficiently handle collisions between asteroids.
- Compare the masses of asteroids to determine the outcome of collisions.
- Handle edge cases where asteroids have equal masses or one asteroid gets destroyed.