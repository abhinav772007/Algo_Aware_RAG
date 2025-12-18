int find(int x, vector<int>& parent) {
    if (parent[x] != x)
        parent[x] = find(parent[x], parent);
    return parent[x];
}

void unite(int a, int b, vector<int>& parent, vector<int>& rank) {
    a = find(a, parent);
    b = find(b, parent);
    if (a != b) {
        if (rank[a] < rank[b]) swap(a, b);
        parent[b] = a;
        if (rank[a] == rank[b]) rank[a]++;
    }
}
