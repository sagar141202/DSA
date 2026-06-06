# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the first array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no such element exists, return -1. The next greater element of an element x is the first element to the right of x that is greater than x. The input arrays will have a length of at most 1000, and the elements will be in the range [-2^31, 2^31 - 1]. For example, given `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the output should be `[3,-1,3]`.

## Approach
The approach to solve this problem involves using a stack to keep track of the indices of the elements in `nums2` that do not have a greater element to their right yet. We then iterate over `nums2` and for each element, we pop all the elements from the stack that are smaller than the current element and update the result array with the current element as the next greater element.

## Complexity
- Time: O(n + m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> map;
    stack<int> st;
    
    // Create a map of next greater elements for nums2
    for (int num : nums2) {
        while (!st.empty() && st.top() < num) {
            map[st.top()] = num;
            st.pop();
        }
        st.push(num);
    }
    
    vector<int> result;
    for (int num : nums1) {
        if (map.find(num) != map.end()) {
            result.push_back(map[num]);
        } else {
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
- Use a stack to keep track of elements that do not have a greater element to their right yet.
- Create a map to store the next greater element for each element in `nums2`.
- Iterate over `nums1` and use the map to find the next greater element for each element.