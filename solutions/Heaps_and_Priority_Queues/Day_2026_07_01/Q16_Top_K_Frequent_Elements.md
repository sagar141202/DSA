# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. You can assume that `k` is always valid, i.e., `1 ≤ k ≤` the number of unique elements in the array. For example, if `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]` because `1` appears three times and `2` appears two times.

## Approach
We can use a hash map to count the frequency of each element and then use a priority queue to find the top `k` frequent elements. The priority queue will store pairs of elements and their frequencies, and we will use the frequency as the priority.

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
        // Count the frequency of each element
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        // Use a priority queue to find the top k frequent elements
        priority_queue<pair<int, int>> pq;
        for (auto& it : count) {
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
- We can use a hash map to count the frequency of each element in O(N) time.
- We can use a priority queue to find the top `k` frequent elements in O(N log k) time.
- The space complexity is O(N) because we need to store the frequency of each element in the hash map.