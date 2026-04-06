# Smallest Range Covering Elements from K Lists

## Problem Statement
Given k sorted lists of integers, find the smallest range that covers at least one element from each of the k lists. The range [a, b] covers an element from a list if there is an element x in the list such that a <= x <= b. The range is defined as the difference between the maximum and minimum elements in the range, i.e., b - a. If there are multiple such ranges with the same difference, return the one with the smallest start value. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20,24].

## Approach
We can use a priority queue to keep track of the smallest element from each list. The algorithm iterates over the lists, adding the smallest element from each list to the priority queue. The range is updated whenever a smaller range is found. The time complexity is optimized by using a min-heap to store the current smallest elements from each list.

## Complexity
- Time: O(N log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val, row, col;
    Node(int v, int r, int c) : val(v), row(r), col(c) {}
};

struct compare {
    bool operator()(const Node& a, const Node& b) {
        return a.val > b.val;
    }
};

vector<int> smallestRange(vector<vector<int>>& nums) {
    priority_queue<Node, vector<Node>, compare> pq;
    int mx = INT_MIN;
    for (int i = 0; i < nums.size(); i++) {
        pq.push(Node(nums[i][0], i, 0));
        mx = max(mx, nums[i][0]);
    }
    int ans = INT_MAX, start = 0, end = 0;
    while (!pq.empty()) {
        Node node = pq.top();
        pq.pop();
        if (mx - node.val < ans) {
            ans = mx - node.val;
            start = node.val;
            end = mx;
        }
        if (node.col + 1 < nums[node.row].size()) {
            pq.push(Node(nums[node.row][node.col + 1], node.row, node.col + 1));
            mx = max(mx, nums[node.row][node.col + 1]);
        } else {
            break;
        }
    }
    return {start, end};
}

int main() {
    vector<vector<int>> nums = {{4,10,15,24,26},{0,9,12,20},{5,18,22,30}};
    vector<int> result = smallestRange(nums);
    cout << "[" << result[0] << "," << result[1] << "]" << endl;
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
- Update the range whenever a smaller range is found.
- The algorithm has a time complexity of O(N log k), where N is the total number of elements across all lists and k is the number of lists.