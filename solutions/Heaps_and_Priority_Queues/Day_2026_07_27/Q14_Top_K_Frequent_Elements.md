# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be sorted in descending order of frequency. If two elements have the same frequency, they should be sorted in ascending order. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]`. The array `nums` has a length of at most `10^5` and `k` is at most `10^4`.

## Approach
We can use a priority queue to store the frequency of each element. The priority queue will be sorted based on the frequency of elements. We will then pop the top `k` elements from the priority queue to get the top `k` frequent elements. We will use an unordered map to store the frequency of each element.

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
        
        // Get the top k frequent elements
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
- Use a priority queue to store the frequency of each element.
- Use an unordered map to store the frequency of each element.
- The priority queue will be sorted based on the frequency of elements.