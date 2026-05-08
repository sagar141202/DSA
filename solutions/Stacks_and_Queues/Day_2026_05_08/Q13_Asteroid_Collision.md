# Asteroid Collision

## Problem Statement
We are given an array of integers asteroids where asteroids[i] represents the size and direction of the ith asteroid. A positive integer represents an asteroid traveling to the right, and a negative integer represents an asteroid traveling to the left. If two asteroids collide, the larger one will remain, and the smaller one will be destroyed. If they are the same size, both will be destroyed. The function should return the state of the asteroids after all collisions.

## Approach
We use a stack to keep track of the asteroids. If a new asteroid is moving to the right, we push it to the stack. If it's moving to the left, we compare it with the top asteroid in the stack and handle the collision accordingly. The process continues until the stack is empty or the new asteroid is moving to the right.

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
            // If asteroid is smaller, it gets destroyed
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            }
            // If asteroid is equal, both get destroyed
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // If asteroid is larger, top of stack gets destroyed
            collision = false;
            break;
        }
        // If no collision or asteroid survived collision, push it to stack
        if (collision && asteroid > 0 || asteroid < 0) {
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
```

## Key Takeaways
- Use a stack to efficiently handle asteroid collisions.
- Compare the size and direction of asteroids to determine the outcome of collisions.
- Handle edge cases where asteroids have the same size or are moving in the same direction.