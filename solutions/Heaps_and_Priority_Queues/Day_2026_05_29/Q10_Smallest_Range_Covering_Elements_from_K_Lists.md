# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max] where min and max are the smallest and largest elements in the range, respectively. If there are multiple such ranges, return the one with the smallest length. For example, given lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20, 24].

## Approach
We use a priority queue to keep track of the smallest element from each list. We initialize the queue with the first element from each list along with its list index and element index. We then repeatedly pop the smallest element from the queue, update the range if necessary, and push the next element from the same list into the queue.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
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

int main() {
    vector<vector<int>> nums = {{4,10,15,24,26},{0,9,12,20},{5,18,22,30}};
    vector<int> result = smallestRange(nums);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20, 24]
```

## Key Takeaways
- Use a priority queue to keep track of the smallest element from each list.
- Update the range whenever a smaller range is found.
- Use a struct to store the value, list index, and element index of each node in the priority queue.