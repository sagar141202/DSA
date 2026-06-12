# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated using the Euclidean distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2). Return the k closest points to the origin. If there are multiple points with the same distance, the points with smaller x-coordinates are considered closer. If there are still multiple points with the same distance and x-coordinate, the points with smaller y-coordinates are considered closer. 

## Approach
We can use a priority queue to store the points based on their distances from the origin. The priority queue will automatically sort the points based on their distances. We will then pop the k closest points from the priority queue and return them. The priority queue will be implemented using a max heap, where the point with the maximum distance will be at the top.

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
        Point point = pq.top();
        pq.pop();
        result.push_back({point.x, point.y});
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
- Use a priority queue to efficiently find the k closest points to the origin.
- Implement a custom comparator to compare points based on their distances and coordinates.
- Use a max heap to store the points, so the point with the maximum distance is at the top.