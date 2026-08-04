# Asteroid Collision

## Problem Statement
We are given an array of integers `asteroids` where each integer represents the size of an asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. If two asteroids collide, the larger one will destroy the smaller one. If both asteroids are of the same size, they will both be destroyed. The function should return the state of the asteroids after all collisions have occurred. For example, given the input `asteroids = [5,10,-5]`, the output should be `[5,10]` because the `-5` asteroid collides with the `5` asteroid and they both get destroyed, but then the `10` asteroid does not collide with any other asteroid. The constraints are that the length of the asteroids array is between 1 and 1000, and each asteroid's size is between -1000 and 1000.

## Approach
We can use a stack to solve this problem by iterating over the asteroids array and pushing each asteroid onto the stack if it is moving to the right or if the stack is empty. If the asteroid is moving to the left, we compare its size with the size of the asteroid at the top of the stack and pop the stack if the top asteroid is smaller. We continue this process until the stack is empty or the top asteroid is larger than the current asteroid.

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
        // If the asteroid is moving to the right or the stack is empty, push it onto the stack
        if (asteroid > 0 || stack.empty() || stack.back() < 0) {
            stack.push_back(asteroid);
        } else {
            // While the stack is not empty and the top asteroid is smaller than the current asteroid
            while (!stack.empty() && stack.back() > 0 && stack.back() < -asteroid) {
                stack.pop_back();
            }
            // If the stack is empty or the top asteroid is moving to the left, push the current asteroid onto the stack
            if (stack.empty() || stack.back() < 0) {
                stack.push_back(asteroid);
            } else if (stack.back() == -asteroid) {
                // If the top asteroid is the same size as the current asteroid, pop the stack
                stack.pop_back();
            }
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
- Use a stack to keep track of the asteroids that have not been destroyed.
- Iterate over the asteroids array and push each asteroid onto the stack if it is moving to the right or if the stack is empty.
- If an asteroid is moving to the left, compare its size with the size of the asteroid at the top of the stack and pop the stack if the top asteroid is smaller.