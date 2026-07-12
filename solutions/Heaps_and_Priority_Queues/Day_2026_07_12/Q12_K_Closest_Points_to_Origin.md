# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, find the k closest points to the origin (0, 0). The distance between two points on the X-Y plane is calculated as the Euclidean distance. If there are multiple answers, return them in any order. The number of points, n, will be in the range [1, 10^4]. The value of k will be in the range [1, n]. The range of the coordinates of the points is [-10^4, 10^4].

## Approach
We can solve this problem using a priority queue to store the points along with their Euclidean distance from the origin. The priority queue will automatically sort the points based on their distance. We can then pop the k smallest elements from the queue to get the k closest points.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x;
    int y;
};

struct compare {
    bool operator()(const pair<int, Point>& a, const pair<int, Point>& b) {
        return a.first > b.first;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<pair<int, Point>, vector<pair<int, Point>>, compare> pq;
    
    for (auto& point : points) {
        int dist = point[0] * point[0] + point[1] * point[1];
        pq.push({dist, {point[0], point[1]}});
        
        if (pq.size() > k) {
            pq.pop();
        }
    }
    
    vector<vector<int>> result;
    while (!pq.empty()) {
        result.push_back({pq.top().second.x, pq.top().second.y});
        pq.pop();
    }
    
    return result;
}
```

## Test Cases
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
```

## Key Takeaways
- Use a priority queue to efficiently find the k smallest elements.
- The priority queue can be used to store custom objects, such as points, along with their distance from the origin.
- The time complexity of the solution is O(n log k) due to the use of the priority queue.