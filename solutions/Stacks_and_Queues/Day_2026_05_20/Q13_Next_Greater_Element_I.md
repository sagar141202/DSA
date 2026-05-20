# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is -1. The input array `nums1` is a subset of `nums2`. The function should return an array of the same length as `nums1` where each element at index `i` is the next greater element of `nums1[i]` in `nums2`.

## Approach
The algorithm uses a stack to keep track of the elements in `nums2` that do not have a next greater element yet. It iterates over `nums2` and for each element, it pops all the elements from the stack that are smaller than the current element and updates the next greater element for these popped elements. The function then uses a map to store the next greater element for each element in `nums2` and finally constructs the result array by looking up the next greater element for each element in `nums1`.

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
    stack<int> st;
    
    // Iterate over nums2 to find the next greater element for each element
    for (int num : nums2) {
        // Pop all the elements from the stack that are smaller than the current element
        while (!st.empty() && st.top() < num) {
            nextGreater[st.top()] = num;
            st.pop();
        }
        // Push the current element to the stack
        st.push(num);
    }
    
    // Construct the result array by looking up the next greater element for each element in nums1
    vector<int> result;
    for (int num : nums1) {
        // If the next greater element exists, add it to the result array
        if (nextGreater.find(num) != nextGreater.end()) {
            result.push_back(nextGreater[num]);
        } 
        // If the next greater element does not exist, add -1 to the result array
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
Output: [-1,3,-1]
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

## Key Takeaways
- Use a stack to keep track of the elements that do not have a next greater element yet.
- Use a map to store the next greater element for each element in `nums2`.
- Iterate over `nums2` to find the next greater element for each element and construct the result array by looking up the next greater element for each element in `nums1`.