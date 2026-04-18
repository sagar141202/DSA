# Asteroid Collision

## Problem Statement
We are given an array of integers representing asteroids, where a positive value represents the size of an asteroid moving to the right and a negative value represents the size of an asteroid moving to the left. If two asteroids collide, the larger one will destroy the smaller one. If both asteroids are of the same size, they will both be destroyed. The function should return the state of the asteroids after all collisions have occurred. For example, given the array [5,10,-5], the output should be [5,10] because the -5 asteroid collides with the 5 asteroid and they both get destroyed, and then the 10 asteroid is left alone.

## Approach
The algorithm uses a stack to keep track of the asteroids. It iterates over the array, pushing each asteroid onto the stack if it's moving to the right or if the stack is empty. If an asteroid is moving to the left, it checks the top of the stack and pops it if the top asteroid is smaller. If the top asteroid is the same size, it pops the top asteroid and skips the current asteroid. If the stack is empty or the top asteroid is smaller, it pushes the current asteroid onto the stack.

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
            // While the stack is not empty and the top asteroid is smaller than the current asteroid
            while (!stack.empty() && stack.back() > 0 && stack.back() < -asteroid) {
                stack.pop_back();
            }
            // If the stack is empty or the top asteroid is moving to the left, push the current asteroid to the stack
            if (stack.empty() || stack.back() < 0) {
                stack.push_back(asteroid);
            } 
            // If the top asteroid is the same size as the current asteroid, skip the current asteroid
            else if (stack.back() == -asteroid) {
                stack.pop_back();
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
- Handle the cases where an asteroid is moving to the right, to the left, or is the same size as the top asteroid on the stack.
- Iterate over the array and update the stack accordingly.