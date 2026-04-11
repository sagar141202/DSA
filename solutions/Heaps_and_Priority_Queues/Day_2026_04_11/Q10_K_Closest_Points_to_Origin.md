# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2-x1)^2 + (y2-y1)^2). Return the k closest points. You may return the answer in any order. The answer is guaranteed to be unique (no two points have the same distance to the origin).

## Approach
We can use a priority queue to solve this problem. The priority queue will store pairs of points and their distances from the origin. We will pop the point with the smallest distance from the queue k times to get the k closest points.

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
        } else {
            Point top = pq.top();
            int distTop = top.x * top.x + top.y * top.y;
            int distP = p.x * p.x + p.y * p.y;
            if (distP < distTop) {
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
- We can use a priority queue to efficiently find the k closest points to the origin.
- The priority queue stores pairs of points and their distances from the origin, allowing us to easily compare and retrieve the closest points.
- The time complexity of this solution is O(N log k), where N is the number of points, because we are using a priority queue to store and retrieve the closest points.