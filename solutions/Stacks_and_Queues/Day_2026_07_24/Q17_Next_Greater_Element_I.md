# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no such element exists, return -1. The next greater element of an element x is the first element to its right that is greater than x. The arrays are non-empty and contain only positive integers. For example, given `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the output should be `[(-1, 3, -1)]` because for the element 4 in `nums1`, there is no greater element in `nums2`, for the element 1, the next greater element is 3, and for the element 2, there is no greater element in `nums2`.

## Approach
We use a stack to keep track of the elements in `nums2` that do not have a greater element yet. We iterate through `nums2` and for each element, we pop all elements from the stack that are smaller than the current element and store the current element as the next greater element. We store the next greater elements in a map for efficient lookup.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    stack<int> st;
    unordered_map<int, int> mp;
    
    // iterate through nums2 to fill the map
    for (int num : nums2) {
        // pop elements from stack that are smaller than num
        while (!st.empty() && st.top() < num) {
            mp[st.top()] = num;
            st.pop();
        }
        st.push(num);
    }
    
    // create result vector
    vector<int> result;
    for (int num : nums1) {
        // if num is in the map, add its next greater element to result
        if (mp.find(num) != mp.end()) {
            result.push_back(mp[num]);
        } else {
            // if num is not in the map, it means there is no greater element
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
- Use a stack to keep track of elements that do not have a greater element yet.
- Use a map to store the next greater elements for efficient lookup.
- Iterate through the second array to fill the map and then create the result vector by looking up the next greater elements in the map.