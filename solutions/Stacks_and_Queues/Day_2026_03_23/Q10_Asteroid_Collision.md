# Asteroid Collision

## Problem Statement
We are given an array of integers asteroids where asteroids[i] represents the size and direction of the ith asteroid. A positive integer represents an asteroid traveling to the right, while a negative integer represents an asteroid traveling to the left. If two asteroids collide, the larger asteroid will destroy the smaller one, and if they are of equal size, both will be destroyed. The function should return the state of the asteroids after all collisions.

## Approach
We can use a stack to keep track of the asteroids. We iterate through the asteroids, and if the current asteroid is moving to the right, we push it onto the stack. If it's moving to the left, we keep popping asteroids from the stack until we find a larger asteroid or the stack is empty.

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
            // if asteroid on stack is smaller, remove it
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            } 
            // if asteroid on stack is equal, remove both
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // if asteroid on stack is larger, remove current asteroid
            break;
        }
        // if stack is empty or top of stack is moving left, push current asteroid
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
Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
```

## Key Takeaways
- Use a stack to efficiently keep track of the asteroids.
- Handle collisions by comparing the sizes of the asteroids and removing the smaller one.
- Consider edge cases where the asteroids are of equal size or the stack is empty.