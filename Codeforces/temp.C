#include <bits/stdc++.h>
#define FastIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define mod 1000000007
#define prva(x) cout << #x << " : " << x << "\n";

using namespace std;
typedef long long ll;

int gcd(int a, int b)
{
    if(b == 0)
        return a;
    return gcd(b, a % b);
}

void solve()
{
}

int main()
{
	FastIO;
	ll t;
	cin >> t;
	while(t--)
	{
		solve();
	}
	return 0;
}