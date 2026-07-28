# Next Greater Element I

## Problem Statement
The problem "Next Greater Element I" involves two arrays, `nums1` and `nums2`, where `nums1` is a subset of `nums2`. The goal is to find the next greater element for each element in `nums1` within the array `nums2`. If no greater element is found, the result should be `-1`. The constraint is that `nums1` is a subset of `nums2`, and the size of `nums1` is `m` while the size of `nums2` is `n`. For example, given `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the output should be `[-1,3,-1]` because for `4` in `nums1`, there's no greater element in `nums2`, for `1` the next greater element is `3`, and for `2` there's no greater element.

## Approach
We use a stack to keep track of elements from `nums2` that we've seen but haven't found a greater element for yet. We iterate through `nums2`, and for each element, we pop elements from the stack that are smaller than the current element and update our result map. This approach ensures we find the next greater element efficiently.

## Complexity
- Time: O(n + m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> map; // To store next greater element for each element in nums2
    stack<int> st; // Stack to keep track of elements we've seen but not found greater for
    
    // Populate map with next greater elements from nums2
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
            result.push_back(-1); // No greater element found
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
- Utilize a stack to efficiently track and update next greater elements.
- An unordered map facilitates quick lookup and storage of next greater elements for each number in `nums2`.
- The solution iterates through both arrays once, maintaining a linear time complexity.