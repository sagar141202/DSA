# Next Greater Element I

## Problem Statement
The problem "Next Greater Element I" involves finding the next greater element for each element in the given array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no greater element is found, return -1. The next greater element of an element `x` is the first element to the right of `x` that is greater than `x`. The constraint is that `1 <= nums1.length <= 1000` and `1 <= nums2.length <= 1000`.

## Approach
To solve this problem, we can use a stack-based approach to keep track of the elements in `nums2` and find the next greater element for each element in `nums1`. We iterate over `nums2` and use a stack to store the indices of the elements. When we encounter an element greater than the top of the stack, we pop the stack and update the result.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a map to store the next greater element for each element in nums2
    unordered_map<int, int> nextGreater;
    stack<int> s;

    // Iterate over nums2 to fill the map
    for (int num : nums2) {
        // While the stack is not empty and the top of the stack is less than the current number
        while (!s.empty() && s.top() < num) {
            // Pop the stack and update the map
            nextGreater[s.top()] = num;
            s.pop();
        }
        // Push the current number onto the stack
        s.push(num);
    }

    // Create a result vector to store the next greater element for each element in nums1
    vector<int> result;
    for (int num : nums1) {
        // If the map contains the current number, push the next greater element into the result
        if (nextGreater.count(num)) {
            result.push_back(nextGreater[num]);
        } else {
            // If not, push -1 into the result
            result.push_back(-1);
        }
    }
    return result;
}
```

## Test Cases
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

## Key Takeaways
- Use a stack-based approach to find the next greater element for each element in `nums2`.
- Create a map to store the next greater element for each element in `nums2`.
- Iterate over `nums1` to find the next greater element for each element using the map.