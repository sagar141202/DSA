# Asteroid Collision

## Problem Statement
We are given an array of integers `asteroids` where each integer represents the size of an asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. When two asteroids collide, the larger one will destroy the smaller one. If both asteroids are of the same size, they will both be destroyed. The function should return the state of the asteroids after all collisions have occurred. For example, given the input `asteroids = [5,10,-5]`, the output should be `[5,10]` because the asteroid of size -5 collides with the asteroid of size 5 and they both get destroyed, and then the asteroid of size 10 does not collide with any other asteroid. The input array `asteroids` will contain at most 10000 asteroids.

## Approach
We use a stack to store the asteroids. We iterate over the asteroids, and for each asteroid, we check if it collides with the asteroid at the top of the stack. If it does, we compare their sizes and update the stack accordingly. We continue this process until there are no more collisions. The stack will contain the state of the asteroids after all collisions have occurred.

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
        bool destroyed = false;
        // check for collision with the top asteroid on the stack
        while (!stack.empty() && asteroid < 0 && stack.back() > 0) {
            if (stack.back() < -asteroid) {
                // top asteroid on the stack is destroyed
                stack.pop_back();
                continue;
            } else if (stack.back() == -asteroid) {
                // both asteroids are destroyed
                stack.pop_back();
            }
            // asteroid is destroyed
            destroyed = true;
            break;
        }
        if (!destroyed) {
            // asteroid is not destroyed, add it to the stack
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
Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
```

## Key Takeaways
- Use a stack to store the asteroids and check for collisions.
- Handle the cases where the asteroid at the top of the stack is destroyed, the asteroid is destroyed, or both asteroids are destroyed.
- The time complexity is O(n) where n is the number of asteroids, and the space complexity is O(n) for the stack.