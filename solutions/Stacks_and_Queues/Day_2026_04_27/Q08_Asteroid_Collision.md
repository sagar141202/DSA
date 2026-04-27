# Asteroid Collision

## Problem Statement
We are given an array of integers representing asteroids, where a positive integer represents the size of an asteroid moving to the right, and a negative integer represents the size of an asteroid moving to the left. If two asteroids collide, the larger one will remain, and if they are the same size, both will be destroyed. The goal is to determine the state of the asteroids after all collisions have occurred. The input array will contain at most 10000 asteroids, and the size of each asteroid will be between 1 and 1000.

## Approach
We can use a stack to keep track of the asteroids. We iterate through the array, and if the current asteroid is moving to the right or the stack is empty, we push it onto the stack. If the current asteroid is moving to the left, we compare its size with the size of the asteroid at the top of the stack and handle the collision accordingly.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> asteroidCollision(vector<int>& asteroids) {
    stack<int> s;
    for (int asteroid : asteroids) {
        // if asteroid is moving to the right or stack is empty, push it onto the stack
        if (asteroid > 0 || s.empty() || s.top() < 0) {
            s.push(asteroid);
        } else {
            // if asteroid is moving to the left, handle collision
            while (!s.empty() && s.top() > 0 && s.top() < -asteroid) {
                s.pop();
            }
            if (s.empty() || s.top() < 0) {
                s.push(asteroid);
            } else if (s.top() == -asteroid) {
                s.pop();
            }
        }
    }
    vector<int> result;
    while (!s.empty()) {
        result.push_back(s.top());
        s.pop();
    }
    reverse(result.begin(), result.end());
    return result;
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
- Use a stack to keep track of the asteroids.
- Handle collisions by comparing the size of the current asteroid with the size of the asteroid at the top of the stack.
- If the current asteroid is larger, pop the top asteroid from the stack and continue handling collisions until the stack is empty or the top asteroid is larger than the current asteroid.