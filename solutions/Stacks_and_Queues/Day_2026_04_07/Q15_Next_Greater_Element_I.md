# Next Greater Element I

## Problem Statement
The problem "Next Greater Element I" involves finding the next greater element for each element in the first array, considering the elements in the second array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no greater element is found, return `-1`. The arrays contain distinct integers, and `nums1` is a subset of `nums2`. For example, given `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the output should be `[-1,3,-1]`.

## Approach
We can use a stack to keep track of the elements in `nums2` and their next greater elements. We iterate over `nums2` and for each element, we pop elements from the stack that are smaller than the current element and update their next greater element.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> map;
    stack<int> s;
    
    // iterate over nums2 to find next greater element for each element
    for (int num : nums2) {
        // pop elements from stack that are smaller than current element
        while (!s.empty() && s.top() < num) {
            map[s.top()] = num;
            s.pop();
        }
        // push current element to stack
        s.push(num);
    }
    
    // create result array
    vector<int> result;
    for (int num : nums1) {
        // if next greater element is found, add it to result
        if (map.find(num) != map.end()) {
            result.push_back(map[num]);
        } else {
            // if no greater element is found, add -1 to result
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
- Use a stack to keep track of elements and their next greater elements.
- Iterate over the second array to find next greater elements for each element in the first array.
- Use an unordered map to store the next greater elements for each element in the first array.