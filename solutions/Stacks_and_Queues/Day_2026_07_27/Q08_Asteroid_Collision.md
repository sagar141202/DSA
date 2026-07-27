# Asteroid Collision

## Problem Statement
We are given an array of integers `asteroids` where each integer represents the size of an asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. When two asteroids collide, the larger one will destroy the smaller one. If the two asteroids are of the same size, they will both be destroyed. The function should return the state of the asteroids after all collisions have occurred. For example, if the input is `asteroids = [5,10,-5]`, the output should be `[5,10]` because the asteroid of size 5 moving to the left will collide with the asteroid of size 5 moving to the right and they will both be destroyed. However, if the input is `asteroids = [8,-8]`, the output should be `[]` because the two asteroids will collide and destroy each other.

## Approach
The algorithm uses a stack to keep track of the asteroids. It iterates over the array of asteroids, and for each asteroid, it checks if the stack is empty or if the top asteroid on the stack is moving to the left. If the stack is not empty and the top asteroid is moving to the right, it compares the sizes of the two asteroids and handles the collision accordingly.

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
        // if asteroid is moving to the right or stack is empty, push it to the stack
        if (asteroid > 0 || stack.empty() || stack.back() < 0) {
            stack.push_back(asteroid);
        } else {
            // if asteroid is moving to the left and top of stack is moving to the right
            while (!stack.empty() && stack.back() > 0 && stack.back() < -asteroid) {
                stack.pop_back();
            }
            if (stack.empty() || stack.back() < 0) {
                stack.push_back(asteroid);
            } else if (stack.back() == -asteroid) {
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
Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
```

## Key Takeaways
- Use a stack to keep track of the asteroids.
- Handle collisions by comparing the sizes of the asteroids and updating the stack accordingly.
- Return the final state of the stack as the result.