# Asteroid Collision

## Problem Statement
We are given an array of integers representing asteroids, where each integer represents the size of an asteroid. A positive integer represents an asteroid moving to the right, and a negative integer represents an asteroid moving to the left. If two asteroids collide, the larger asteroid will destroy the smaller one. If the two asteroids are of the same size, they will both be destroyed. The task is to determine the state of the asteroids after all collisions have occurred. The input array will contain at most 10000 asteroids, and the size of each asteroid will be between 1 and 10000.

## Approach
We can solve this problem by using a stack to keep track of the asteroids. We iterate through the array, and for each asteroid, we check if it collides with the asteroid at the top of the stack. If it does, we compare their sizes and update the stack accordingly. This process continues until there are no more collisions.

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
        // if asteroid is moving to the right, or stack is empty, or top of stack is moving to the left
        if (asteroid > 0 || st.empty() || st.top() < 0) {
            st.push(asteroid);
        } else {
            // while stack is not empty, top of stack is moving to the right, and top of stack is smaller than current asteroid
            while (!st.empty() && st.top() > 0 && st.top() < -asteroid) {
                st.pop();
            }
            // if stack is empty or top of stack is moving to the left
            if (st.empty() || st.top() < 0) {
                st.push(asteroid);
            } 
            // if top of stack is same size as current asteroid
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

int main() {
    vector<int> asteroids = {5,10,-5};
    vector<int> result = asteroidCollision(asteroids);
    for (int i : result) {
        cout << i << " ";
    }
    return 0;
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
- Compare the sizes of the asteroids when a collision occurs and update the stack accordingly.
- Handle the cases where the asteroids are of the same size or one is larger than the other.