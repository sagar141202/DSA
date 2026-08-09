# Asteroid Collision

## Problem Statement
We are given an array of integers `asteroids` where each integer represents the size of an asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. When two asteroids collide, the larger asteroid will destroy the smaller one. If the two asteroids are of the same size, they will both be destroyed. The function should return the state of the asteroids after all collisions have occurred. For example, given the array `asteroids = [5,10,-5]`, the output should be `[5,10]` because the `-5` asteroid collides with the `5` asteroid and they both get destroyed, and then the `10` asteroid remains. The constraints are that the length of the array `asteroids` is at most `10000`, and each integer in the array is between `-1000` and `1000`.

## Approach
We can solve this problem by using a stack to keep track of the asteroids that have not been destroyed yet. We iterate through the array, and for each asteroid, we check if it is moving to the left. If it is, we check if the stack is empty or if the top asteroid on the stack is moving to the left. If either condition is true, we push the asteroid onto the stack. If not, we compare the size of the asteroid with the top asteroid on the stack. If the asteroid is larger, we pop the top asteroid from the stack and repeat the process until the stack is empty or the top asteroid is larger. If the sizes are equal, we pop the top asteroid from the stack.

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
        // If the asteroid is moving to the right or the stack is empty, push it onto the stack
        if (asteroid > 0 || st.empty() || st.top() < 0) {
            st.push(asteroid);
        } else {
            // While the stack is not empty and the top asteroid is moving to the right and is smaller than the current asteroid
            while (!st.empty() && st.top() > 0 && st.top() < -asteroid) {
                st.pop();
            }
            // If the stack is empty or the top asteroid is moving to the left, push the current asteroid onto the stack
            if (st.empty() || st.top() < 0) {
                st.push(asteroid);
            } 
            // If the top asteroid is the same size as the current asteroid, pop the top asteroid from the stack
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
- Use a stack to keep track of the asteroids that have not been destroyed yet.
- Iterate through the array and check for collisions between asteroids moving in opposite directions.
- Compare the sizes of the asteroids and destroy the smaller one in case of a collision.