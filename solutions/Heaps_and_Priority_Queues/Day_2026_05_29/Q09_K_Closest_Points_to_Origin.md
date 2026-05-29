# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2 - x1)^2 + (y2 - y1)^2). If two points have the same distance to the origin, their order in the result does not matter. Return the k closest points.

## Approach
We will use a priority queue to store the points along with their distances from the origin. The priority queue will be ordered based on the distance from the origin. We will then pop the k closest points from the priority queue and return them.

## Complexity
- Time: O(N log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
    int distance;
    Point(int x, int y) : x(x), y(y), distance(x * x + y * y) {}
};

struct compare {
    bool operator()(const Point& p1, const Point& p2) {
        return p1.distance > p2.distance;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, compare> pq;
    for (auto& point : points) {
        pq.push(Point(point[0], point[1]));
        if (pq.size() > k) {
            pq.pop();
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
- We use a priority queue to efficiently find the k closest points.
- The distance from a point to the origin is calculated as the square of the Euclidean distance to avoid unnecessary square root calculations.
- The time complexity is O(N log k) due to the use of the priority queue.