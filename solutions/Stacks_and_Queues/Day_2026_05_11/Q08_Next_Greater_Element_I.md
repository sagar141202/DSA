# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the result is `-1`. The function should return an array of the same length as the input array, where each element at index `i` is the next greater element to the element at index `i` in the input array. For example, given the input array `[2, 1, 5]`, the output should be `[5, 5, -1]` because the next greater element for `2` is `5`, for `1` is `5`, and for `5` is `-1` since there is no element to its right that is greater.

## Approach
The solution uses a stack to keep track of the elements that do not have a next greater element yet. We iterate through the array from left to right, popping elements from the stack that are smaller than the current element and updating the result array accordingly. This approach ensures that we find the next greater element for each element in a single pass.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> map;
    stack<int> st;
    for (int num : nums2) {
        while (!st.empty() && st.top() < num) {
            map[st.top()] = num;
            st.pop();
        }
        st.push(num);
    }
    vector<int> result(nums1.size(), -1);
    for (int i = 0; i < nums1.size(); i++) {
        if (map.find(nums1[i]) != map.end()) {
            result[i] = map[nums1[i]];
        }
    }
    return result;
}
```

## Test Cases
```
Input: nums1 = [2, 4], nums2 = [1, 2, 3, 4]
Output: [2, -1]
Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]
```

## Key Takeaways
- Use a stack to keep track of elements without a next greater element.
- Iterate through the array to find the next greater element for each element.
- Utilize an unordered map to store the next greater element for each element in `nums2` for efficient lookup when processing `nums1`.