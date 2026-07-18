# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be sorted in descending order of frequency, and if two elements have the same frequency, they should be sorted in ascending order. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]`. The constraints are `1 <= nums.length <= 10^5` and `1 <= k <= nums.length`.

## Approach
The algorithm uses an unordered_map to store the frequency of each element, then a priority_queue to store the top k frequent elements. The priority_queue is implemented as a max heap, where the top element is the one with the highest frequency. If two elements have the same frequency, the one with the smaller value is given higher priority.

## Complexity
- Time: O(n log k)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Create a hashmap to store the frequency of each element
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        // Create a priority queue to store the top k frequent elements
        priority_queue<pair<int, int>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }
        
        // Get the top k frequent elements from the priority queue
        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(pq.top().second);
            pq.pop();
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Input: nums = [1], k = 1
Output: [1]
```

## Key Takeaways
- Use an unordered_map to store the frequency of each element for efficient lookup and update.
- Use a priority_queue to store the top k frequent elements, with a custom comparator to handle ties in frequency.
- The time complexity is O(n log k) due to the use of the priority queue, where n is the length of the input array and k is the number of top frequent elements to return.