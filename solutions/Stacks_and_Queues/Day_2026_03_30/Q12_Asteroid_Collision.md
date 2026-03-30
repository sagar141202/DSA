# Asteroid Collision

## Problem Statement
We are given an array of integers representing asteroids, where each integer represents the size of the asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. If two asteroids collide, the larger one will destroy the smaller one. If they are of the same size, both will be destroyed. The goal is to find the state of the asteroids after all collisions have occurred. For example, given the array [5,10,-5], the output will be [5,10] because the -5 asteroid will be destroyed by the 5 asteroid. Given the array [8,-8], the output will be [] because both asteroids will be destroyed.

## Approach
We can solve this problem using a stack to keep track of the asteroids. We iterate over the array, and for each asteroid, we check if it is moving to the left. If it is, we keep popping asteroids from the stack until we find an asteroid that is larger than the current one or the stack is empty. If the stack is empty or the top asteroid is moving to the left, we push the current asteroid onto the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> asteroidCollision(vector<int>& asteroids) {
    stack<int> st;
    for (int asteroid : asteroids) {
        // if asteroid is moving to the right, push it to the stack
        if (asteroid > 0) {
            st.push(asteroid);
        } else {
            // if asteroid is moving to the left, pop asteroids from the stack until we find a larger one
            while (!st.empty() && st.top() > 0 && st.top() < -asteroid) {
                st.pop();
            }
            // if the stack is empty or the top asteroid is moving to the left, push the current asteroid to the stack
            if (st.empty() || st.top() < 0) {
                st.push(asteroid);
            } 
            // if the top asteroid is of the same size as the current asteroid, pop it from the stack
            else if (st.top() == -asteroid) {
                st.pop();
            }
        }
    }
    vector<int> result;
    while (!st.empty()) {
        result.push_back(st.top());
        st.pop();
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
Input: [-2,-1,1,2]
Output: [-2,-1,1,2]
```

## Key Takeaways
- Use a stack to keep track of the asteroids.
- Iterate over the array and handle each asteroid based on its direction.
- Handle collisions by popping asteroids from the stack until a larger one is found or the stack is empty.