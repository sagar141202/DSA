# Next Greater Element I

## Problem Statement
The problem "Next Greater Element I" states that we are given two arrays, `nums1` and `nums2`, where `nums1` is a subset of `nums2`. We need to find the next greater element for each element in `nums1` in the array `nums2`. If there is no greater element, we return -1. The next greater element of an element `x` is the first element to the right of `x` that is greater than `x`. The arrays `nums1` and `nums2` contain distinct elements.

## Approach
We can use a stack to store the elements of `nums2` and iterate over `nums2` to find the next greater element for each element. We use a hashmap to store the next greater element for each element in `nums2` and then use this hashmap to find the next greater element for each element in `nums1`.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        // Create a hashmap to store the next greater element for each element in nums2
        unordered_map<int, int> nextGreater;
        stack<int> st;
        
        // Iterate over nums2 to find the next greater element for each element
        for (int num : nums2) {
            // While the stack is not empty and the top element is less than the current element
            while (!st.empty() && st.top() < num) {
                // Update the next greater element for the top element
                nextGreater[st.top()] = num;
                // Pop the top element from the stack
                st.pop();
            }
            // Push the current element onto the stack
            st.push(num);
        }
        
        // Create a result vector to store the next greater element for each element in nums1
        vector<int> result;
        for (int num : nums1) {
            // If the next greater element for num is found in the hashmap, add it to the result vector
            if (nextGreater.find(num) != nextGreater.end()) {
                result.push_back(nextGreater[num]);
            } else {
                // If not found, add -1 to the result vector
                result.push_back(-1);
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

## Key Takeaways
- Use a stack to store the elements of `nums2` and iterate over `nums2` to find the next greater element for each element.
- Use a hashmap to store the next greater element for each element in `nums2` and then use this hashmap to find the next greater element for each element in `nums1`.
- The time complexity is O(n + m) where n and m are the lengths of `nums1` and `nums2` respectively.