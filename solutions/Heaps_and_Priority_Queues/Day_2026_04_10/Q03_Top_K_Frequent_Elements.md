# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. The input array `nums` will have a length of at least 1 and at most 10^5, and `k` will be in the range [1, min(100, length of `nums`)].

## Approach
We can use an unordered map to store the frequency of each element, then use a priority queue to get the top k frequent elements. The priority queue will store pairs of elements and their frequencies, and will be ordered by the frequency.

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
        // Create an unordered map to store the frequency of each element
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
- Use an unordered map to store the frequency of each element for efficient lookup and update.
- Use a priority queue to get the top k frequent elements, with the priority queue ordered by the frequency of the elements.
- The time complexity is O(N log k) due to the use of the priority queue, where N is the length of the input array.