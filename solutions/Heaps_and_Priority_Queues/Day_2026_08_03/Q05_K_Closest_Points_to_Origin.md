# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2 - x1)^2 + (y2 - y1)^2). Return the k closest points. You may return the answer in any order. The answer is guaranteed to be unique (no two points have the same distance to the origin). 1 <= k <= points.length <= 10^4, -10^4 < xi, yi < 10^4.

## Approach
We can use a priority queue to store the points based on their distance from the origin. The priority queue will automatically keep track of the k closest points. We can then extract the k closest points from the priority queue and return them. This approach ensures that we efficiently find the k closest points without having to calculate the distance of every point.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
};

struct compare {
    bool operator()(const Point& a, const Point& b) {
        int distA = a.x * a.x + a.y * a.y;
        int distB = b.x * b.x + b.y * b.y;
        return distA > distB;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, compare> pq;
    for (auto& point : points) {
        Point p;
        p.x = point[0];
        p.y = point[1];
        if (pq.size() < k) {
            pq.push(p);
        } else if (p.x * p.x + p.y * p.y < pq.top().x * pq.top().x + pq.top().y * pq.top().y) {
            pq.pop();
            pq.push(p);
        }
    }
    vector<vector<int>> result;
    while (!pq.empty()) {
        Point p = pq.top();
        pq.pop();
        result.push_back({p.x, p.y});
    }
    return result;
}
```

## Test Cases
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
```

## Key Takeaways
- We use a priority queue to store points based on their distance from the origin.
- The priority queue automatically keeps track of the k closest points.
- We can use a custom comparator to define the order of elements in the priority queue.