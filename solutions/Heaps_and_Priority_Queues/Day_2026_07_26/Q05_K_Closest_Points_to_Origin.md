# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated using the Euclidean distance formula: sqrt((x2-x1)^2 + (y2-y1)^2). If two points have the same distance to the origin, their order does not matter. The points are distinct and k is always valid.

## Approach
We use a priority queue to store points based on their distance from the origin. The priority queue is a max heap where the point with the maximum distance is at the top. We iterate over all points, calculate their distance, and push them into the priority queue. If the size of the queue exceeds k, we remove the point with the maximum distance.

## Complexity
- Time: O(N log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
};

struct Compare {
    bool operator()(const Point& a, const Point& b) {
        int distA = a.x * a.x + a.y * a.y;
        int distB = b.x * b.x + b.y * b.y;
        return distA > distB;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Compare> pq;
    for (auto& point : points) {
        Point p;
        p.x = point[0];
        p.y = point[1];
        if (pq.size() < k) {
            pq.push(p);
        } else {
            if (p.x * p.x + p.y * p.y < pq.top().x * pq.top().x + pq.top().y * pq.top().y) {
                pq.pop();
                pq.push(p);
            }
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
- Use a priority queue to efficiently select the k closest points.
- Calculate the Euclidean distance for each point and use it as the priority in the queue.
- If the size of the queue exceeds k, remove the point with the maximum distance.