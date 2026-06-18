# Asteroid Collision

## Problem Statement
We are given an array of integers asteroids where asteroids[i] represents the size and direction of the ith asteroid. A positive integer represents an asteroid moving to the right, while a negative integer represents an asteroid moving to the left. If two asteroids collide, the larger one will remain and the smaller one will be destroyed. If they are of equal size, both will be destroyed. The function should return the state of the asteroids after all collisions.

## Approach
We can use a stack to keep track of the asteroids. We iterate through the asteroids array, and for each asteroid, we check if it collides with the top asteroid on the stack. If it does, we compare their sizes and update the stack accordingly.

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
        bool collision = true;
        while (!stack.empty() && asteroid < 0 && stack.back() > 0) {
            // If asteroid on stack is smaller, it gets destroyed
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            }
            // If asteroid on stack is of equal size, both get destroyed
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // If asteroid on stack is larger, current asteroid gets destroyed
            collision = false;
            break;
        }
        // If no collision or current asteroid survives collision, add it to stack
        if (collision) {
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
- Iterate through the asteroids array and check for collisions with the top asteroid on the stack.
- Update the stack based on the comparison of asteroid sizes.