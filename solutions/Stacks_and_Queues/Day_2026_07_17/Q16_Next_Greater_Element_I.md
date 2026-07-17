# Next Greater Element I

## Problem Statement
The problem "Next Greater Element I" involves finding the next greater element for each element in an array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no such element exists, return -1. The next greater element of an element `x` is the first element to the right of `x` that is greater than `x`. The constraint is that the elements in `nums1` are unique. For example, given `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the output should be `[3,-1,3]`.

## Approach
We can use a stack to store the elements of `nums2` and iterate through `nums1` to find the next greater element. The stack will help us keep track of the elements that we have seen so far but haven't found a greater element yet. We use a map to store the next greater element for each element in `nums2`.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a stack to store the elements of nums2
    stack<int> st;
    // Create a map to store the next greater element for each element in nums2
    unordered_map<int, int> mp;
    
    // Iterate through nums2 to find the next greater element for each element
    for (int num : nums2) {
        // While the stack is not empty and the top element is less than the current element
        while (!st.empty() && st.top() < num) {
            // Pop the top element from the stack and store the next greater element in the map
            mp[st.top()] = num;
            st.pop();
        }
        // Push the current element onto the stack
        st.push(num);
    }
    
    // Create a result vector to store the next greater element for each element in nums1
    vector<int> result;
    // Iterate through nums1 to find the next greater element for each element
    for (int num : nums1) {
        // If the element exists in the map, push the next greater element into the result vector
        if (mp.find(num) != mp.end()) {
            result.push_back(mp[num]);
        } 
        // If the element does not exist in the map, push -1 into the result vector
        else {
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
- Use a stack to keep track of the elements that we have seen so far but haven't found a greater element yet.
- Use a map to store the next greater element for each element in `nums2`.
- Iterate through `nums1` to find the next greater element for each element using the map.