# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` if all elements are distinct. The function should be able to handle arrays of size up to 10^5 and integers in the range [-10^9, 10^9]. For example, given the array `[1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice, and given the array `[1, 2, 3, 4]`, the function should return `false` because all elements are distinct.

## Approach
We can solve this problem using an unordered set to store unique elements. We iterate through the array and for each element, we check if it exists in the set. If it does, we return true. If we finish iterating through the array without finding any duplicates, we return false. This approach ensures we only need to traverse the array once.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // Create an unordered set to store unique elements
        unordered_set<int> unique_nums;
        
        // Iterate through the array
        for (int num : nums) {
            // Check if the current element exists in the set
            if (unique_nums.find(num) != unique_nums.end()) {
                // If it does, return true
                return true;
            }
            // Otherwise, add the element to the set
            unique_nums.insert(num);
        }
        // If we finish iterating without finding duplicates, return false
        return false;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 1]
Output: true
Input: [1, 2, 3, 4]
Output: false
Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
```

## Key Takeaways
- Using an unordered set allows us to check for duplicates in constant time.
- This approach has a linear time complexity because we only need to traverse the array once.
- The space complexity is also linear because in the worst case, we might need to store all elements in the set.