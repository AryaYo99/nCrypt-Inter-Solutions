#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

int n, m, k;

int mat[55][55], vis[55][55];

int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};

bool valid(int x, int y) {
    return x >= 0 && y >= 0 && x < n && y < m && !mat[x][y] && !vis[x][y];
}

int dfs(int x, int y) {
    if (x == 0 || y == 0 || x == n - 1 || y == m - 1)   return -1e10;
    vis[x][y] = 1;
    int c = 1;
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i], ny = y + dy[i];
        if (valid(nx, ny))
            c += dfs(nx, ny);
    }
    return c;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char c; cin >> c;
            if (c == '*')   mat[i][j] = vis[i][j] = 1;
        }
    }
    vector<array<int, 3>> a;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (valid(i, j)) {
                int t = dfs(i, j);
                if (t < 0)  continue;
                a.push_back({t, i, j});
            }
        }
    }
    sort(a.begin(), a.end(), [&] (auto x, auto y) {return x[0] < y[0];});
    int ans = 0;
    memset(vis, 0, sizeof vis);
    k = (int) a.size() - k;
    for (auto &i: a) {
        if (k == 0) break;
        k--;
        ans += i[0];
    }
    cout << ans;
}
