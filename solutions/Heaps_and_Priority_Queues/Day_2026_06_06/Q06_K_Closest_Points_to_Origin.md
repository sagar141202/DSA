# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2-x1)^2 + (y2-y1)^2). If there are multiple points with the same distance to the origin, the points with smaller x-coordinates will be considered closer. If there are still multiple points with the same distance and x-coordinate, the points with smaller y-coordinates will be considered closer. Return the k closest points.

## Approach
We will use a priority queue to store points based on their distance from the origin. The priority queue will be ordered by the distance and then by the x and y coordinates. We will then pop the k closest points from the priority queue.

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
        if (distA == distB) {
            if (a.x == b.x) {
                return a.y > b.y;
            }
            return a.x > b.x;
        }
        return distA > distB;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Compare> pq;
    for (auto& point : points) {
        pq.push({point[0], point[1]});
        if (pq.size() > k) {
            pq.pop();
        }
    }
    vector<vector<int>> result;
    while (!pq.empty()) {
        result.push_back({pq.top().x, pq.top().y});
        pq.pop();
    }
    return result;
}
```

## Test Cases
```
Input: points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]
```

## Key Takeaways
- Use a priority queue to efficiently find the k closest points.
- Define a custom comparator to order points based on their distance and coordinates.
- Use a struct to represent points for clarity and readability.