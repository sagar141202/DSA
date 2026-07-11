# Asteroid Collision

## Problem Statement
We are given an array of integers representing asteroids, where a positive value represents the size of an asteroid moving to the right, and a negative value represents the size of an asteroid moving to the left. Each asteroid is moving at the same speed. If two asteroids collide, the larger asteroid will destroy the smaller one, and if they are of equal size, both will be destroyed. The task is to determine the state of the asteroids after all collisions have occurred. The input array will contain at most 10000 asteroids, and the size of each asteroid will be in the range [-1000, 1000]. For example, given the array [5,10,-5], the output will be [5,10] because the -5 asteroid collides with the 10 asteroid and is destroyed.

## Approach
We will use a stack to keep track of the asteroids. We iterate over the array, and for each asteroid, we check if it is moving to the left (negative value) and the top of the stack is moving to the right (positive value). If so, we compare their sizes and handle the collision accordingly. This approach ensures that we process the asteroids in the order they collide.

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
        // Collision occurs when asteroid is moving left and top of stack is moving right
        while (!stack.empty() && asteroid < 0 && stack.back() > 0) {
            // If asteroid on top of stack is smaller, it gets destroyed
            if (stack.back() < -asteroid) {
                stack.pop_back();
                continue;
            }
            // If asteroid on top of stack is equal, both get destroyed
            else if (stack.back() == -asteroid) {
                stack.pop_back();
            }
            // If asteroid on top of stack is larger, the current asteroid gets destroyed
            break;
        }
        // If the stack is empty or the current asteroid is moving right, or the top of the stack is moving left, we push it to the stack
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
Input: [-2,-1,1,2]
Output: [-2,-1,1,2]
```

## Key Takeaways
- Use a stack to keep track of the asteroids.
- Handle collisions by comparing the sizes of the asteroids and updating the stack accordingly.
- The final state of the asteroids is the contents of the stack after all collisions have occurred.