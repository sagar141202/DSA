# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. If there is a tie, the smaller elements are preferred. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]`. If `nums = [1,1,2,2,3,3,3]` and `k = 1`, the output should be `[3]`.

## Approach
We can use a hash map to store the frequency of each element, then use a priority queue to get the top k frequent elements. The priority queue will store pairs of elements and their frequencies, and will be ordered by frequency and then by the element itself.

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
        
        // Create a priority queue to get the top k frequent elements
        priority_queue<pair<int, int>> pq;
        for (auto& pair : frequency) {
            pq.push({pair.second, pair.first});
        }
        
        // Get the top k frequent elements
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
Input: nums = [1,1,2,2,3,3,3], k = 1
Output: [3]
```

## Key Takeaways
- We can use a hash map to efficiently store and retrieve the frequency of each element.
- A priority queue can be used to efficiently get the top k frequent elements.
- The `unordered_map` and `priority_queue` data structures in C++ provide an efficient way to solve this problem.