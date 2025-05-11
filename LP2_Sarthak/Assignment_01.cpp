#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

class Graph {
public:
    int n;
    vector< vector<int> > adj;

    Graph(int n)
    {
        this->n = n;
        adj.resize(n);
    }

    void addEdge(int u, int v)
    {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    void DFS(int start)
    {
        stack<int> stk;
        vector<bool> visited(n, false);
        stk.push(start);
        visited[start] = true;

        while (!stk.empty()) {
            int u = stk.top();
            cout << u << " ";
            stk.pop();

            for (int v = 0; v < adj[u].size(); v++) {
                int node = adj[u][v];
                if (!visited[node]) {
                    visited[node] = true;
                    stk.push(node);
                }
            }
        }
    }

    void DFS_recursive(int u, vector<bool>& visited)
    {
        visited[u] = true;
        cout << u << " ";
        for (int v = 0; v < adj[u].size(); v++) {
            int node = adj[u][v];
            if (!visited[node]) {
                DFS_recursive(node, visited);
            }
        }
    }

    void BFS(int s)
    {
        queue<int> q;
        vector<bool> visited(n, false);
        visited[s] = true;
        q.push(s);

        while (!q.empty()) {
            int u = q.front();
            cout << u << " ";
            q.pop();

            for (int v = 0; v < adj[u].size(); v++) {
                int node = adj[u][v];
                if (!visited[node]) {
                    visited[node] = true;
                    q.push(node);
                }
            }
        }
    }

    void BFS_recursive_util(queue<int>& q, vector<bool>& visited)
    {
        if (q.empty()) return;

        int u = q.front();
        q.pop();
        cout << u << " ";

        for (int v = 0; v < adj[u].size(); v++) {
            int node = adj[u][v];
            if (!visited[node]) {
                visited[node] = true;
                q.push(node);
            }
        }

        BFS_recursive_util(q, visited);
    }

    void BFS_recursive(int start)
    {
        queue<int> q;
        vector<bool> visited(n, false);
        visited[start] = true;
        q.push(start);
        BFS_recursive_util(q, visited);
    }
};

int main()
{
    Graph g(4);

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(0, 3);
    g.addEdge(1, 0);
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 0);
    g.addEdge(2, 1);
    g.addEdge(3, 0);
    g.addEdge(3, 1);

    cout << "DFS : " << endl;
    g.DFS(3);
    cout << endl;

    cout << "DFS recursive : " << endl;
    vector<bool> visited(4, false);
    g.DFS_recursive(3, visited);
    cout << endl;

    cout << "BFS : " << endl;
    g.BFS(1);
    cout << endl;

    cout << "BFS recursive : " << endl;
    g.BFS_recursive(1);
}
