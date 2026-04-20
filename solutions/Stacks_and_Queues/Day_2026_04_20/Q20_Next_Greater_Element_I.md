# Next Greater Element I

## Problem Statement
The problem "Next Greater Element I" involves finding the next greater element for each element in the given array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no greater element is found, return -1. The arrays `nums1` and `nums2` contain distinct integers, and the length of `nums1` is less than or equal to the length of `nums2`. For example, given `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the output should be `[3,-1,3]`.

## Approach
The algorithm uses a stack to keep track of the elements in `nums2` that we have seen so far but have not found a greater element yet. We iterate over `nums2` and for each element, we pop all the elements from the stack that are smaller than the current element and update the result for these elements. Then, we push the current element onto the stack.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a map to store the next greater element for each element in nums2
    unordered_map<int, int> map;
    stack<int> st;
    
    // Iterate over nums2
    for (int num : nums2) {
        // While the stack is not empty and the top element is smaller than the current element
        while (!st.empty() && st.top() < num) {
            // Update the map with the next greater element
            map[st.top()] = num;
            st.pop();
        }
        // Push the current element onto the stack
        st.push(num);
    }
    
    // Create the result vector
    vector<int> result;
    for (int num : nums1) {
        // If the map contains the next greater element, add it to the result
        if (map.find(num) != map.end()) {
            result.push_back(map[num]);
        } else {
            // Otherwise, add -1 to the result
            result.push_back(-1);
        }
    }
    
    return result;
}
```

## Test Cases
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [3,-1,3]
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

## Key Takeaways
- Use a stack to keep track of the elements that we have seen so far but have not found a greater element yet.
- Use a map to store the next greater element for each element in `nums2`.
- Iterate over `nums2` to fill the map and then iterate over `nums1` to find the next greater element for each element.