# Asteroid Collision

## Problem Statement
We are given an array of integers asteroids where asteroids[i] represents the size and direction of an asteroid. A positive integer represents an asteroid traveling to the right, while a negative integer represents an asteroid traveling to the left. When two asteroids collide, the larger asteroid destroys the smaller one and continues moving in the same direction. If the two asteroids are the same size, they both get destroyed. The function should return the state of the asteroids after all collisions.

## Approach
The algorithm uses a stack to keep track of the asteroids. It iterates through the array, pushing asteroids onto the stack if they are moving to the right. If an asteroid is moving to the left, it pops asteroids from the stack that are smaller than the current asteroid. If an asteroid on the stack is the same size as the current asteroid, it gets destroyed along with the current asteroid.

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
            // if asteroid on stack is the same size, they both get destroyed
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // if asteroid on stack is larger, current asteroid gets destroyed
            break;
        }
        // if stack is empty or current asteroid is moving to the right, or the top of the stack is moving to the left
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
- Use a stack to efficiently handle asteroid collisions.
- Be careful with edge cases, such as when two asteroids are the same size.
- Iterate through the array only once to achieve a time complexity of O(n).