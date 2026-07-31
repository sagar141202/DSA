# Asteroid Collision

## Problem Statement
We are given an array `asteroids` where each element represents the size of an asteroid. A positive size indicates the asteroid is moving to the right, while a negative size indicates it's moving to the left. When two asteroids collide, the larger one survives and continues moving in its original direction. If both asteroids have the same size, they both get destroyed. Our goal is to find the state of the asteroids after all collisions have occurred.

## Approach
We can use a stack to keep track of the asteroids. When a collision occurs, we compare the sizes of the top asteroid on the stack and the current asteroid. If the top asteroid is smaller, it gets destroyed and we continue checking the next asteroid on the stack.

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
        // Collision occurs when asteroid is moving left and stack is not empty and top asteroid is moving right
        while (!stack.empty() && asteroid < 0 && stack.back() > 0) {
            // If asteroid is larger than top asteroid, top asteroid gets destroyed
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            }
            // If asteroid is smaller than top asteroid, asteroid gets destroyed
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // If asteroid is smaller than top asteroid, asteroid gets destroyed and we break the loop
            break;
        }
        // If stack is empty or asteroid is moving right or top asteroid is moving left, we push asteroid to stack
        if (stack.empty() || asteroid > 0 || stack.back() < 0) {
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
- Use a stack to keep track of the asteroids.
- When a collision occurs, compare the sizes of the top asteroid on the stack and the current asteroid.
- Handle cases where asteroids have the same size and get destroyed.