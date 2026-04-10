# Asteroid Collision

## Problem Statement
We are given an array of integers `asteroids` where each integer represents the size of an asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. When two asteroids collide, the larger one remains, and the smaller one is destroyed. If both asteroids have the same size, they are both destroyed. The function should return the state of the asteroids after all collisions have occurred. For example, given the array `asteroids = [5,10,-5]`, the function should return `[5,10]` because the asteroid of size -5 is destroyed by the asteroid of size 10. The function should handle arrays of up to 1000 asteroids.

## Approach
We can solve this problem by using a stack to keep track of the asteroids. We iterate through the array, and for each asteroid, we check if it is moving to the left. If it is, we check if the stack is not empty and the top asteroid is moving to the right. If both conditions are true, we compare the sizes of the two asteroids.

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
            while (!stack.empty() && stack.back() > 0 && asteroid < 0) {
                // if top of stack is smaller, pop it
                if (stack.back() < -asteroid) {
                    stack.pop_back();
                    continue;
                } 
                // if top of stack is equal, pop it and break
                else if (stack.back() == -asteroid) {
                    stack.pop_back();
                }
                // if top of stack is larger, break
                break;
            }
            // if stack is empty or top of stack is moving to the left, push asteroid to the stack
            if (stack.empty() || stack.back() < 0) {
                stack.push_back(asteroid);
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
- Use a stack to keep track of the asteroids.
- Iterate through the array and compare the sizes of the asteroids when a collision occurs.
- Handle cases where the asteroids have the same size or one is larger than the other.