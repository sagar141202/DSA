# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max], where min and max are the minimum and maximum values in the range. The lists are non-empty and contain distinct integers. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20, 24].

## Approach
We use a priority queue to store the current smallest element from each list along with its list index and element index. We maintain the minimum and maximum values in the priority queue and update the smallest range if a smaller range is found. We then remove the smallest element from the priority queue and add the next element from the same list.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val, listIndex, elementIndex;
    Node(int val, int listIndex, int elementIndex) : val(val), listIndex(listIndex), elementIndex(elementIndex) {}
};

struct Compare {
    bool operator()(const Node& a, const Node& b) {
        return a.val > b.val;
    }
};

vector<int> smallestRange(vector<vector<int>>& nums) {
    priority_queue<Node, vector<Node>, Compare> pq;
    int maxVal = INT_MIN;
    for (int i = 0; i < nums.size(); i++) {
        maxVal = max(maxVal, nums[i][0]);
        pq.push(Node(nums[i][0], i, 0));
    }
    int minRange = INT_MAX, start = 0, end = 0;
    while (!pq.empty()) {
        Node node = pq.top();
        pq.pop();
        if (maxVal - node.val < minRange) {
            minRange = maxVal - node.val;
            start = node.val;
            end = maxVal;
        }
        if (node.elementIndex + 1 < nums[node.listIndex].size()) {
            maxVal = max(maxVal, nums[node.listIndex][node.elementIndex + 1]);
            pq.push(Node(nums[node.listIndex][node.elementIndex + 1], node.listIndex, node.elementIndex + 1));
        } else {
            break;
        }
    }
    return {start, end};
}
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20, 24]
```

## Key Takeaways
- Use a priority queue to store the current smallest element from each list.
- Maintain the minimum and maximum values in the priority queue to update the smallest range.
- Remove the smallest element from the priority queue and add the next element from the same list to ensure all elements are covered.