# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be sorted in descending order of frequency, and if two elements have the same frequency, they should be sorted in ascending order. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]`.

## Approach
We can use a hash map to store the frequency of each element, then use a priority queue to get the top k frequent elements. The priority queue will be sorted based on the frequency of the elements.

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
        // Create a hash map to store the frequency of each element
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }

        // Create a priority queue to get the top k frequent elements
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
- Use a hash map to store the frequency of each element for efficient lookup and counting.
- Use a priority queue to get the top k frequent elements, sorted by frequency and then by value.
- The time complexity is O(n log k) due to the priority queue operations, and the space complexity is O(n) for the hash map and priority queue.