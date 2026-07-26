# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max] where min and max are the minimum and maximum values in the range. For example, if we have three lists: [4,10,15,24,26], [0,9,12,20], [5,18,22,30], the smallest range covering elements from all three lists is [20,24]. If there are multiple such ranges, return the one with the smallest length. If there are still multiple ranges with the same length, return the one with the smallest start value.

## Approach
We can use a priority queue to keep track of the smallest element from each list. We start by pushing the first element from each list into the priority queue along with its list index and element index. Then, we keep popping the smallest element from the queue and push the next element from the same list until we find a range that covers at least one element from each list.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Node {
    int val, listIndex, elementIndex;
    Node(int v, int li, int ei) : val(v), listIndex(li), elementIndex(ei) {}
};

struct Compare {
    bool operator()(const Node& a, const Node& b) {
        return a.val > b.val;
    }
};

pair<int, int> smallestRange(vector<vector<int>>& nums) {
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

int main() {
    vector<vector<int>> nums = {{4,10,15,24,26},{0,9,12,20},{5,18,22,30}};
    pair<int, int> range = smallestRange(nums);
    cout << "[" << range.first << "," << range.second << "]" << endl;
    return 0;
}
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- Use a priority queue to keep track of the smallest element from each list.
- Keep popping the smallest element from the queue and push the next element from the same list until we find a range that covers at least one element from each list.
- Update the maximum value and the range if a smaller range is found.