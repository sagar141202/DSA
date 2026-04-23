# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin. The distance between two points on a 2D plane can be calculated using the Euclidean distance formula: √(x2 - x1)^2 + (y2 - y1)^2. The origin is at (0, 0). Return the k closest points ordered by their distance from the origin. If there are multiple points with the same distance, return them in any order. For example, given points = [[1, 3], [-2, 2]], k = 1, the output should be [[-2, 2]] because the distance from (-2, 2) to the origin is less than the distance from (1, 3) to the origin.

## Approach
We can use a priority queue to solve this problem, where each point is stored along with its distance from the origin. The priority queue will automatically order the points based on their distance. We can then pop the k closest points from the queue to get the result. Alternatively, we can use the nth_element function in C++ to find the kth smallest element in the array of distances.

## Complexity
- Time: O(n log k)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
    int distance;
    Point(int x, int y) : x(x), y(y) {
        distance = x * x + y * y;
    }
};

struct Compare {
    bool operator()(const Point& a, const Point& b) {
        return a.distance > b.distance;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Compare> pq;
    for (auto& point : points) {
        pq.push(Point(point[0], point[1]));
        if (pq.size() > k) {
            pq.pop();
        }
    }
    vector<vector<int>> result;
    while (!pq.empty()) {
        auto point = pq.top();
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
- We can use a priority queue to efficiently find the k closest points to the origin.
- The time complexity of the solution is O(n log k) due to the use of the priority queue.
- The space complexity is O(n) for storing the points in the priority queue.