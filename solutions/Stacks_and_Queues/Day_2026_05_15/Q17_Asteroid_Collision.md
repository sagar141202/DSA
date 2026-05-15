# Asteroid Collision

## Problem Statement
We are given an array of integers representing asteroids in a row. Each integer represents the size of the asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. If two asteroids collide, the larger one will destroy the smaller one. If both asteroids are of the same size, they will destroy each other. The task is to determine the state of the asteroids after all collisions have occurred. The input array will contain at most 10000 asteroids, and the size of each asteroid will be between -1000 and 1000.

## Approach
We can use a stack to store the asteroids. We iterate through the array, and for each asteroid, we check if the stack is empty or the top asteroid is moving in the same direction. If it is, we push the asteroid onto the stack. If the top asteroid is moving in the opposite direction, we compare their sizes and handle the collision accordingly.

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
            // if asteroid on stack is same size, both get destroyed
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // if asteroid on stack is larger, current asteroid gets destroyed
            break;
        }
        // if stack is empty or top asteroid is moving in same direction, push asteroid onto stack
        if (stack.empty() || asteroid > 0 || stack.back() < 0) {
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
- Handle edge cases such as same-sized asteroids and empty stacks
- Use a while loop to handle multiple collisions between asteroids