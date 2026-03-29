# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in `nums`. The output should be sorted in descending order of frequency. If two elements have the same frequency, they should be sorted in ascending order. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]`. The constraints are `1 <= nums.length <= 10^5` and `1 <= k <= num.length`.

## Approach
The approach is to use an unordered_map to store the frequency of each element, then use a priority_queue to get the top k frequent elements. The priority_queue will store pairs of frequency and element, and will be sorted based on frequency and then element value.

## Complexity
- Time: O(N log k)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // store frequency of each element
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        // use priority_queue to get top k frequent elements
        priority_queue<pair<int, int>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }
        
        vector<int> result;
        while (k-- > 0) {
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
- Use unordered_map to store frequency of each element for efficient lookup.
- Use priority_queue to get top k frequent elements, sorted by frequency and then element value.
- The time complexity is O(N log k) due to the use of priority_queue.