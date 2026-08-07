# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2-x1)^2 + (y2-y1)^2). If two points have the same distance to the origin, their order does not matter. Return the k closest points. You may return the answer in any order. The number of points is at least 1, and k is between 1 and the number of points.

## Approach
We will utilize a priority queue to efficiently select the k closest points. The priority queue will store points based on their distance from the origin. We will then extract the k smallest elements from the queue to obtain the k closest points.

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
        pq.push({point[0], point[1]});
    }
    
    vector<vector<int>> result;
    for (int i = 0; i < k; i++) {
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
```

## Key Takeaways
- Utilize a priority queue to efficiently select the k closest points.
- Define a custom comparator to order points based on their distance from the origin.
- Extract the k smallest elements from the priority queue to obtain the k closest points.