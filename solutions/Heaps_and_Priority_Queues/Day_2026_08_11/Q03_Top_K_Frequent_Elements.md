# Top K Frequent Elements
## Problem Statement
Given a non-empty array of integers, return the k most frequent elements. You may return the answer in any order. The input array will have at least 1 element, and k will be between 1 and the number of unique elements in the array. For example, given the array [1,1,1,2,2,3] and k = 2, the output should be [1,2] because 1 appears 3 times and 2 appears 2 times.

## Approach
We can solve this problem by using a hash map to store the frequency of each element, and then using a priority queue to get the top k frequent elements. The priority queue will store pairs of elements and their frequencies, and it will be ordered by the frequency in descending order.

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
- We can use a hash map to store the frequency of each element in O(N) time.
- We can use a priority queue to get the top k frequent elements in O(N log k) time.
- The space complexity is O(N) because we need to store the frequency of each element and the top k frequent elements.