# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. If there are multiple possible answers, any of them is correct. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]`. The constraints are: `1 <= nums.length <= 10^5` and `1 <= k <= num.length`.

## Approach
We can use a hashmap to count the frequency of each element in the array, then use a priority queue to find the top k frequent elements. The priority queue will store pairs of elements and their frequencies, and will be ordered by the frequency.

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
        // Count the frequency of each element
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        // Use a priority queue to find the top k frequent elements
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
- Use a hashmap to count the frequency of each element in the array.
- Use a priority queue to find the top k frequent elements, with the priority queue ordered by the frequency.
- The time complexity is O(n log k) due to the use of the priority queue, where n is the length of the input array.