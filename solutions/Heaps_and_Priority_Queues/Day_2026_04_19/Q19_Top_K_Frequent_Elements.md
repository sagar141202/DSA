# Top K Frequent Elements

## Problem Statement
Given a non-empty array of integers, return the k most frequent elements. The input array will have at least 1 element and at most 10^5 elements, and k will be between 1 and the number of unique elements in the array. For example, given the array [1,1,1,2,2,3] and k = 2, the output should be [1,2] because 1 appears 3 times and 2 appears 2 times, making them the two most frequent elements.

## Approach
We can solve this problem using a priority queue or a heap to store the frequency of each element. The algorithm involves counting the frequency of each element, then using a priority queue to get the top k frequent elements. We use a hash map to count the frequency of each element, then push the elements into a priority queue based on their frequency.

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

        // Use a priority queue to get the top k frequent elements
        priority_queue<pair<int, int>> maxHeap;
        for (auto& it : count) {
            maxHeap.push({it.second, it.first});
        }

        // Get the top k frequent elements
        vector<int> result;
        while (k-- > 0) {
            result.push_back(maxHeap.top().second);
            maxHeap.pop();
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
- Use a hash map to count the frequency of each element efficiently.
- Use a priority queue to get the top k frequent elements, where the priority is based on the frequency of each element.
- The time complexity is O(N log k) because we push N elements into the priority queue, and each push operation takes O(log k) time.