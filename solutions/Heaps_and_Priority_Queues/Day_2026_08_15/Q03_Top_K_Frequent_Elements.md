# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order, and the elements should be unique. If there are multiple possible answers, any of them will be accepted. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output could be `[1,2]` or `[2,1]`. The array `nums` will have at least 1 element, and `k` will be between 1 and the number of unique elements in `nums`.

## Approach
We will use a hash map to count the frequency of each element, then use a priority queue to find the top k frequent elements. The priority queue will store pairs of elements and their frequencies, with the frequency as the priority.

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
        // Count frequency of each element
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        // Use priority queue to find top k frequent elements
        priority_queue<pair<int, int>> pq;
        for (auto& pair : count) {
            pq.push({pair.second, pair.first});
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
- Use a hash map to count the frequency of each element in O(N) time.
- Use a priority queue to find the top k frequent elements in O(N log k) time.
- The space complexity is O(N) due to the hash map and priority queue.