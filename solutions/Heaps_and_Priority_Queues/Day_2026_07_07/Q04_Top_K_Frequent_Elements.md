# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. The input array will contain at least `k` elements. The frequency of an element is the number of times it appears in the array. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]` because `1` appears three times and `2` appears two times.

## Approach
We can use a hash map to store the frequency of each element and then use a priority queue to find the top `k` frequent elements. The priority queue will store pairs of elements and their frequencies, and it will be ordered by the frequency in descending order.

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
        // Create a hash map to store the frequency of each element
        unordered_map<int, int> frequency;
        for (int num : nums) {
            frequency[num]++;
        }
        
        // Create a priority queue to store the top k frequent elements
        priority_queue<pair<int, int>> pq;
        for (auto& pair : frequency) {
            pq.push({pair.second, pair.first});
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
- Use a hash map to store the frequency of each element for efficient lookup and update.
- Use a priority queue to find the top `k` frequent elements, taking advantage of its ordering property.
- The time complexity is dominated by the priority queue operations, which are O(N log k) in the worst case.