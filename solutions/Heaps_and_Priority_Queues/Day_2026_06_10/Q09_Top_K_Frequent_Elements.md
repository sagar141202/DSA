# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. If there are multiple possible answers, any of them is fine. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output could be `[1,2]`. The constraints are that `1 <= nums.length <= 10^5` and `1 <= k <= nums.length`.

## Approach
We can use a hashmap to store the frequency of each element, then use a priority queue to get the top k frequent elements. The priority queue will store pairs of elements and their frequencies, and will be ordered by the frequency in descending order.

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
Input: nums = [1], k = 1
Output: [1]
```

## Key Takeaways
- Use a hashmap to store the frequency of each element for efficient lookup and counting.
- Use a priority queue to get the top k frequent elements, ordered by their frequencies in descending order.
- The time complexity is O(n log k) due to the priority queue operations, where n is the number of unique elements.