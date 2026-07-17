# Asteroid Collision

## Problem Statement
We are given an array of integers asteroids where asteroids[i] represents the size and direction of an asteroid. A positive value represents an asteroid moving to the right, while a negative value represents an asteroid moving to the left. If two asteroids collide, the larger asteroid will destroy the smaller one. If both asteroids are the same size, they will both be destroyed. The function should return the state of the asteroids after all collisions have occurred. For example, given the input asteroids = [5,10,-5], the output should be [5,10] because the -5 asteroid collides with the 10 asteroid and is destroyed. If the input is asteroids = [8,-8], the output should be [] because the two asteroids are the same size and destroy each other.

## Approach
The solution uses a stack to track the asteroids that have not been destroyed yet. We iterate over the asteroids, and for each asteroid, we check if it is moving to the left. If it is, we compare it with the top asteroid on the stack. If the top asteroid is smaller, we remove it from the stack. If the top asteroid is the same size, we remove both asteroids. If the top asteroid is larger, the current asteroid is destroyed and we move on to the next one.

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
        // if asteroid is moving to the right or stack is empty, push it to stack
        if (asteroid > 0 || stack.empty() || stack.back() < 0) {
            stack.push_back(asteroid);
        } else {
            // asteroid is moving to the left, collide with top asteroid on stack
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
- Use a stack to track the asteroids that have not been destroyed yet.
- Iterate over the asteroids and handle collisions based on the direction and size of the asteroids.
- The time complexity is O(n) because we are iterating over the asteroids once, and the space complexity is O(n) because in the worst case, we might need to store all asteroids in the stack.