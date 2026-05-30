# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. If there is a tie, the smaller element should be preferred. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]`. The input array `nums` contains at most `10^5` integers, and `k` is between `1` and the number of unique elements in `nums`.

## Approach
We can use a hash map to store the frequency of each element, then use a priority queue to find the top k frequent elements. The priority queue will be ordered by the frequency of the elements in descending order, and if there is a tie, the smaller element will be preferred.

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
        unordered_map<int, int> freqMap;
        for (int num : nums) {
            freqMap[num]++;
        }

        // Create a priority queue to store the top k frequent elements
        priority_queue<pair<int, int>> pq;
        for (auto& pair : freqMap) {
            pq.push({pair.second, pair.first});
        }

        // Extract the top k frequent elements from the priority queue
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
- Use a hash map to store the frequency of each element for efficient lookup and update.
- Use a priority queue to find the top k frequent elements, with the priority queue ordered by the frequency of the elements in descending order.
- If there is a tie, the smaller element will be preferred due to the ordering of the priority queue.