# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is `-1`. The function should return an array of next greater elements in the same order as the input array. For example, given the arrays `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the function should return `[3,-1]` because the next greater element of `4` is `3` (which is present in `nums2`) and there is no next greater element for `1` and `2`.

## Approach
The algorithm uses a stack to keep track of the elements from `nums2` that do not have a next greater element yet. It iterates over `nums2` and for each element, it pops all the elements from the stack that are smaller than the current element and updates the next greater element for these popped elements. The algorithm then pushes the current element to the stack.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a hashmap to store the next greater element for each element in nums2
    unordered_map<int, int> nextGreater;
    stack<int> s;
    
    // Iterate over nums2 to find the next greater element for each element
    for (int num : nums2) {
        // Pop all elements from the stack that are smaller than the current element
        while (!s.empty() && s.top() < num) {
            nextGreater[s.top()] = num;
            s.pop();
        }
        // Push the current element to the stack
        s.push(num);
    }
    
    // Create the result array
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
Output: [3,-1]
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

## Key Takeaways
- Use a stack to keep track of the elements that do not have a next greater element yet.
- Iterate over the second array to find the next greater element for each element.
- Use a hashmap to store the next greater element for each element in the second array.