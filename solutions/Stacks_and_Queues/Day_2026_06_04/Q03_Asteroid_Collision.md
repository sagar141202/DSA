# Asteroid Collision

## Problem Statement
We are given an array of integers asteroids where asteroids[i] represents the size and direction of the ith asteroid. A positive integer represents an asteroid traveling to the right, and a negative integer represents an asteroid traveling to the left. If two asteroids collide, the larger one will destroy the smaller one, and if they are of equal size, both will be destroyed. The function should return the state of the asteroids after all collisions.

## Approach
The algorithm uses a stack to keep track of the asteroids. It iterates through the array, and for each asteroid, it checks if the stack is empty or the top asteroid is moving in the same direction. If not, it compares the sizes of the asteroids and handles the collision accordingly.

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
        // collision occurs
        while (!stack.empty() && asteroid < 0 && stack.back() > 0) {
            // if asteroid on stack is smaller, it gets destroyed
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            } 
            // if both asteroids are of equal size, both get destroyed
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // if asteroid on stack is larger, current asteroid gets destroyed
            break;
        }
        // if stack is empty or top asteroid is moving in same direction, push current asteroid
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
- Use a stack to efficiently handle asteroid collisions.
- Iterate through the array of asteroids and check for collisions with the top asteroid on the stack.
- Handle collisions based on the sizes of the asteroids.