# Asteroid Collision

## Problem Statement
We are given an array of integers `asteroids` where each integer represents the size of an asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. When two asteroids collide, the larger asteroid will destroy the smaller one. If the two asteroids are of the same size, they will both be destroyed. The function should return the state of the asteroids after all collisions have occurred. The input array `asteroids` will have a length between 1 and 1000, and each integer in the array will be between -1000 and 1000.

## Approach
We use a stack to keep track of the asteroids. We iterate over the array and push each asteroid onto the stack. If the top asteroid on the stack is moving to the right and the current asteroid is moving to the left, we compare their sizes and handle the collision accordingly. We continue this process until no more collisions can occur.

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
        // Collision occurs when top of stack is positive and current asteroid is negative
        while (!stack.empty() && stack.back() > 0 && asteroid < 0) {
            // If current asteroid is larger, destroy top of stack and continue
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            }
            // If current asteroid is smaller, destroy it and break loop
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            break;
        }
        // If stack is empty or top of stack is negative, push current asteroid
        if (stack.empty() || stack.back() < 0 || asteroid > 0) {
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
- Use a stack to efficiently handle asteroid collisions
- Compare sizes of asteroids to determine the outcome of a collision
- Handle edge cases where asteroids have the same size or are moving in the same direction