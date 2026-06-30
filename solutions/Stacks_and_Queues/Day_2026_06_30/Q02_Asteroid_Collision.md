# Asteroid Collision

## Problem Statement
We are given an array of integers representing asteroids, where each integer represents the size of the asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. When two asteroids collide, the larger asteroid destroys the smaller one. If the two asteroids are the same size, they both get destroyed. The task is to determine the state of the asteroids after all collisions have occurred. The input array will contain at most 10000 asteroids, and the size of each asteroid will be between 1 and 10000.

## Approach
We can use a stack to keep track of the asteroids. We iterate through the array, and for each asteroid, we check if it collides with the asteroid at the top of the stack. If it does, we compare their sizes and update the stack accordingly. This process continues until there are no more collisions.

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
        // collision occurs when asteroid is moving left and top of stack is moving right
        bool collision = asteroid < 0 && !st.empty() && st.top() > 0;
        while (collision) {
            // if asteroid on top of stack is smaller, it gets destroyed
            if (st.top() < -asteroid) {
                st.pop();
                collision = asteroid < 0 && !st.empty() && st.top() > 0;
            }
            // if asteroid on top of stack is same size, both get destroyed
            else if (st.top() == -asteroid) {
                st.pop();
                collision = false;
            }
            // if asteroid on top of stack is larger, current asteroid gets destroyed
            else {
                collision = false;
            }
        }
        // if no collision or asteroid survived collision, add it to stack
        if (!collision || st.empty() || asteroid > 0) {
            st.push(asteroid);
        }
    }
    vector<int> result(st.size());
    int i = st.size() - 1;
    while (!st.empty()) {
        result[i--] = st.top();
        st.pop();
    }
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
- Use a stack to keep track of the asteroids and handle collisions efficiently.
- Iterate through the array and check for collisions between each asteroid and the top of the stack.
- Update the stack based on the size of the asteroids involved in the collision.