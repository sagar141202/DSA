# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, find the K closest points to the origin (0, 0). The distance between two points on the X-Y plane is calculated using the Euclidean distance formula: √(x2 - x1)^2 + (y2 - y1)^2. Here, we can ignore the square root and simply calculate the squared distance (x2 - x1)^2 + (y2 - y1)^2. The problem constraints are 1 <= K <= points.length <= 10^4 and -10^4 <= xi, yi <= 10^4.

## Approach
We can use a priority queue to store the points based on their squared distances from the origin. The priority queue will automatically order the points, and we can then extract the K closest points. Alternatively, we can use the nth_element function from the C++ Standard Library or a custom implementation of the quickselect algorithm to find the Kth smallest distance in linear time on average.

## Complexity
- Time: O(N log K) for the priority queue approach, where N is the number of points
- Space: O(K) for the priority queue approach

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

vector<Point> kClosest(vector<Point>& points, int K) {
    priority_queue<Point, vector<Point>, Compare> pq;
    for (const auto& point : points) {
        if (pq.size() < K) {
            pq.push(point);
        } else if (point.x * point.x + point.y * point.y < pq.top().x * pq.top().x + pq.top().y * pq.top().y) {
            pq.pop();
            pq.push(point);
        }
    }
    vector<Point> result;
    while (!pq.empty()) {
        result.push_back(pq.top());
        pq.pop();
    }
    return result;
}

// Alternatively, using nth_element
vector<Point> kClosestAlternative(vector<Point>& points, int K) {
    nth_element(points.begin(), points.begin() + K, points.end(),
                [](const Point& a, const Point& b) {
                    return a.x * a.x + a.y * a.y < b.x * b.x + b.y * b.y;
                });
    return vector<Point>(points.begin(), points.begin() + K);
}
```

## Test Cases
```
Input: points = [[1, 3], [-2, 2]], K = 1
Output: [[-2, 2]]
```

## Key Takeaways
- The priority queue approach is suitable when K is significantly smaller than the total number of points.
- The nth_element approach is more efficient when K is close to the total number of points, as it has a linear time complexity on average.
- The choice of approach depends on the specific problem constraints and the characteristics of the input data.