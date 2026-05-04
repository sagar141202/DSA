# Asteroid Collision

## Problem Statement
We are given an array of integers representing asteroids, where a positive value represents the size of an asteroid moving to the right, and a negative value represents the size of an asteroid moving to the left. If two asteroids collide, the larger one will destroy the smaller one. If both asteroids are of the same size, they will both be destroyed. The function should return the state of the asteroids after all collisions have occurred. For example, given the array [5,10,-5], the output should be [5,10] because the -5 asteroid collides with the 10 asteroid and is destroyed. Given the array [8,-8], the output should be [] because both asteroids are of the same size and are destroyed.

## Approach
We can solve this problem using a stack to keep track of the asteroids. We iterate through the array, and for each asteroid, we check if it is moving to the left. If it is, we compare it with the top asteroid on the stack. If the top asteroid is smaller, we pop it from the stack. If the top asteroid is the same size, we pop it from the stack and skip the current asteroid. If the top asteroid is larger, we skip the current asteroid.

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
        // if asteroid is moving to the right or stack is empty, push it to stack
        if (asteroid > 0 || stack.empty() || stack.back() < 0) {
            stack.push_back(asteroid);
        } else {
            // if asteroid is moving to the left and top of stack is moving to the right
            while (!stack.empty() && stack.back() > 0) {
                // if top of stack is smaller, pop it
                if (stack.back() < -asteroid) {
                    stack.pop_back();
                    continue;
                }
                // if top of stack is same size, pop it and skip current asteroid
                if (stack.back() == -asteroid) {
                    stack.pop_back();
                }
                // if top of stack is larger, skip current asteroid
                break;
            }
            // if stack is empty or top of stack is moving to the left, push current asteroid
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
- Use a stack to keep track of the asteroids.
- Iterate through the array and compare each asteroid with the top asteroid on the stack.
- Handle cases where asteroids are of the same size, or where one asteroid is larger than the other.