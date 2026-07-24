# Asteroid Collision

## Problem Statement
We are given an array of integers representing asteroids, where a positive value represents the size of an asteroid moving to the right and a negative value represents the size of an asteroid moving to the left. When two asteroids collide, the smaller one is destroyed. If both asteroids are of the same size, both are destroyed. The task is to determine the state of the asteroids after all collisions have occurred.

## Approach
The algorithm uses a stack to keep track of the asteroids. We iterate over the array and push each asteroid onto the stack. If the top asteroid on the stack is moving to the right and the current asteroid is moving to the left, we compare their sizes and handle the collision accordingly.

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
            // If current asteroid is larger, destroy top of stack
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            }
            // If both asteroids are of the same size, destroy both
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // If current asteroid is smaller, destroy it
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
- Iterate over the array and push each asteroid onto the stack
- Handle collisions by comparing the sizes of the top asteroid on the stack and the current asteroid