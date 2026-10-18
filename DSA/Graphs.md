BFS

https://www.codingninjas.com/studio/problems/bfs-in-graph_973002?leftPanelTab=0

```
vector<int> bfsTraversal(int n, vector<vector<int>> &adj){
    vector<int> bfs;
 
    vector<int> visited(n, 0);
    queue<int> q;

    q.push(0);
    visited[0] = 1;
    bfs.push_back(0);

    while (!q.empty()) {

        int node = q.front();
        q.pop();

        for (const auto& it: adj[node]) {
            if (!visited[it]) {
                q.push(it);
                visited[it] = 1;
                bfs.push_back(it);
            }
        }
    }

    return bfs;
}
```

---


DFS

https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

```
class Solution {
  public:
    vector<int> dfs_runner(int node, vector<int> adj[], vector<int>& dfs, vector<int>& visited) {
        visited[node] = 1;
        dfs.push_back(node);

        for (const auto& it: adj[node]) {
            if (!visited[it]) {
                dfs_runner(it, adj, dfs, visited);
            }
        }
        
        return dfs;
    }

    vector<int> dfsOfGraph(int V, vector<int> adj[]) {
        vector<int> dfs, visited(V, 0);
        return dfs_runner(0, adj, dfs, visited);
    }
};
```

---


Cycle detection in undirected graph:


- DFS: Use visited array, ensure you never reach another element in the visited array that isn't the current node's parent. For this, keep track of parent.
- BFS: Use visited array, same logic as DFS. Keep track of parent.


Cycle detection in directed graph:


- DFS: Use visited and visited_in_curr_path arrays. If element not in visited , keep traversing. Else, if element also in visited_in_curr_path, there exists a cycle.
- BFS with toposort: Kahn's Algo

---




Topological Sort

https://practice.geeksforgeeks.org/problems/topological-sort/1
- DFS: Using Stack
  https://www.youtube.com/watch?v=5lZ0iJMrUMk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=21&pp=iAQB
- BFS: Kahn's Algorithm
  https://www.youtube.com/watch?v=73sneFXuTEg&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=22
---

Shortest distance in DAG with weights (from source to all nodes):
- Use toposort and then traverse in that order
- set distance to source = 0
- Check distance to adj elements, and update their distance based on min(existing distance, distance though toposort's top node)
- pop toposort top node

https://www.youtube.com/watch?v=ZUFQfFaU-8U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=27&pp=iAQB
---

Shortest distance in undirected unit weighted graph:

Apply simple BFS but store the distance from source for each node in a distance array.

https://www.youtube.com/watch?v=C4gxoTaI71U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=28
---

Shortest Path Algo for Undirected Weighted Graph (w/o negative weights): Dijkstra's Algorithm

- with priority queue (min_heap)
```
	- public:
	- 	//Function to find the shortest distance of all the vertices
	-     //from the source vertex S.
	-     vector <int> dijkstra(int V, vector<vector<int>> adj[], int S) {
	-         priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
	-         vector<int> distances (V, 1e9);
	-         
	-         pq.push({0, S});
	-         distances[S] = 0;
	-         
	-         while (!pq.empty()) {
	-             int weight = pq.top().first;
	-             int node = pq.top().second;
	-             pq.pop();
	-             
	-             for (auto it: adj[node]) {
	-                 int adj_node = it[0];
	-                 int adj_weight = it[1];
	-                 
	-                 if (distances[adj_node] > weight + adj_weight) {
	-                     distances[adj_node] = weight + adj_weight;
	-                     pq.push({distances[adj_node], adj_node});
	-                 }
	-             }
	-         }
	-         
	-         return distances;
	-     }
```

- with set

