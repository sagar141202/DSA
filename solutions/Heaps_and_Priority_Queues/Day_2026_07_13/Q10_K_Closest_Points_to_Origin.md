# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2-x1)^2 + (y2-y1)^2). The answer should be sorted in ascending order by their distance to the origin. If there are multiple answers, output them in any order. Constraints: 1 <= k <= points.length <= 10^4, -10^4 <= xi, yi <= 10^4.

## Approach
We can use a priority queue to solve this problem, where the priority is the distance of each point to the origin. We will push all points into the priority queue and then pop the k smallest points. Alternatively, we can use a partial sort or nth_element approach to find the k smallest points.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
    Point(int x = 0, int y = 0) : x(x), y(y) {}
};

struct Compare {
    bool operator()(const Point& p1, const Point& p2) {
        int dist1 = p1.x * p1.x + p1.y * p1.y;
        int dist2 = p2.x * p2.x + p2.y * p2.y;
        return dist1 > dist2;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Compare> pq;
    for (auto& point : points) {
        pq.push(Point(point[0], point[1]));
    }
    vector<vector<int>> result;
    while (k-- > 0) {
        Point p = pq.top();
        pq.pop();
        result.push_back({p.x, p.y});
    }
    return result;
}

// alternative solution using nth_element
vector<vector<int>> kClosest_nsth_element(vector<vector<int>>& points, int k) {
    nth_element(points.begin(), points.begin() + k, points.end(),
                [](const vector<int>& p1, const vector<int>& p2) {
                    return p1[0] * p1[0] + p1[1] * p1[1] < p2[0] * p2[0] + p2[1] * p2[1];
                });
    return vector<vector<int>>(points.begin(), points.begin() + k);
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
- Use a priority queue to efficiently find the k smallest points.
- Alternatively, use nth_element or partial sort to find the k smallest points.
- The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2-x1)^2 + (y2-y1)^2), but for comparison purposes, we can use the squared distance to avoid the sqrt operation.