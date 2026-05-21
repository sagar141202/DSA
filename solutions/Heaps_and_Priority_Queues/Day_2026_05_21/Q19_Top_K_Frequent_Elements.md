# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. The input array will have at least one element, and `k` will be between 1 and the number of unique elements in the array. For example, if `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]`. If there are multiple possible answers, any of them will be accepted.

## Approach
We can use a hash map to store the frequency of each element, then use a priority queue to get the top k frequent elements. The priority queue will store pairs of elements and their frequencies, and will be ordered based on the frequencies. We can then pop the top k elements from the priority queue to get the result.

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
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        // Create a priority queue to store the top k frequent elements
        priority_queue<pair<int, int>> queue;
        for (auto& pair : count) {
            queue.push({pair.second, pair.first});
        }
        
        // Get the top k frequent elements
        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(queue.top().second);
            queue.pop();
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
- Use a hash map to store the frequency of each element for efficient lookup.
- Use a priority queue to get the top k frequent elements, ordered by their frequencies.
- The time complexity is O(N log k) due to the use of a priority queue, and the space complexity is O(N) for storing the frequency of each element.