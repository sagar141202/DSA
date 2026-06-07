# Asteroid Collision

## Problem Statement
We are given an array of asteroids where each asteroid is represented by an integer. The integer represents the size of the asteroid. A positive integer indicates that the asteroid is moving to the right, while a negative integer indicates that the asteroid is moving to the left. When two asteroids collide, the asteroid with the larger size survives and continues moving in its original direction. If the two asteroids have the same size, they both get destroyed. The task is to determine the state of the asteroids after all collisions have occurred. The input array will contain at most 10000 asteroids.

## Approach
We use a stack to keep track of the asteroids that have not been destroyed yet. When a new asteroid is encountered, we check if it will collide with the asteroid at the top of the stack. If it does, we compare their sizes and handle the collision accordingly. This process continues until no more collisions can occur.

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
        // collision occurs when asteroid is moving left and top of stack is moving right
        bool collision = asteroid < 0 && !stack.empty() && stack.back() > 0;
        while (collision) {
            // if asteroid on top of stack is smaller, it gets destroyed
            if (stack.back() < -asteroid) {
                stack.pop_back();
                collision = asteroid < 0 && !stack.empty() && stack.back() > 0;
            }
            // if both asteroids have the same size, they both get destroyed
            else if (stack.back() == -asteroid) {
                stack.pop_back();
                collision = false;
            }
            // if asteroid on top of stack is larger, new asteroid gets destroyed
            else {
                collision = false;
            }
        }
        // if no collision or new asteroid survived, add it to the stack
        if (!collision || stack.empty() || stack.back() < 0) {
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
Input: [-2,-1,1,2]
Output: [-2,-1,1,2]
```

## Key Takeaways
- Use a stack to efficiently handle asteroid collisions.
- Handle collisions by comparing the sizes of the asteroids and updating the stack accordingly.
- The solution has a time complexity of O(n) and a space complexity of O(n), where n is the number of asteroids.