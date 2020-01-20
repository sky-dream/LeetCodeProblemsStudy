#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
typedef int ll;
typedef long double ld;
using namespace __gnu_pbds;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
ll exp(ll x,ll y){if(y==0) return 1;if(y%2 == 1) return x*exp(x,y/2)*exp(x,y/2);return exp(x,y/2) * exp(x,y/2);}
ll exp(ll x,ll y,ll modd) {if(y==0) return 1;ll t=exp(x,y/2,modd);t = t%modd;t=t*t;t=t%modd;if(y % 2 == 1) return (x*t)%modd ;return t%modd;}
#pragma GCC target ("avx2")
#pragma GCC optimization ("O3")
#pragma GCC optimization ("unroll-loops")
#pragma GCC target ("sse4")
#define ios ios_base::sync_with_stdio(0) ; cin.tie(0) ; cout.tie(0)
#define so sizeof
#define pb push_back
#define cl clear() ;
#define vl vector<ll>
#define sz size()
#define len length()
#define emp empty()
#define el endl;cout.flush()
#define be begin()
#define fi first
#define se second
#define br break
#define en end()
#define ro return 0
#define eb emplace_back
#define con continue
#define ms(x) memset(x , 0ll, so x)
#define all(x) (x).be , (x).en
#define acc(x) accumulate((x).be , (x).en , 0ll)
#define forn(i,a,b) for(ll i=a;i<=b;++i)
#define revn(i,a,b) for(ll i=a;i>=b;--i)
#define rng_58 mt19937 rng(chrono::steady_clock::now().time_since_epoch().count())
#define vs vector<string>
#define vsi vector<pair<string,int>>
#define vll vector<pair<ll,ll> >
#define vlll vector<ll,pair<ll,ll>>
#define vlvl vector<pair<ll,ll>,ll>>
#define pll pair<ll,ll>
#define plll pair<ll,pair<ll,ll>>
#define plvl pair<pair<ll,ll> ,ll>
#define mp make_pair
#define trace3(a,b,c) cerr <<"a is " << a << " b is " << b << " c is " << c << el;
#define trace4(a,b,c,d) cerr <<"a is " << a << " b is " << b << " c is " << c <<" d is " << d << el ;
#define trace5(a,b,c,d,e) cerr <<"a is " << a << " b is " << b << " c is " << c <<" d is " << d << " e is " << e << el;
#define trace6(a,b,c,d,e,f) cerr <<"a is " << a << " b is " << b << " c is " << c <<" d is " << d << " e is " << e << " f is " << f << el ;
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
       vl v = nums ; 
        ll n = v.sz ;
        if(n == 0) {
            vl res;
            res.cl ;
            return res ; 
        }
       deque<pll> q ;
    forn(i , 0 , k - 1){
       if(i == 0) q.push_front({v[i] , i});
       else if(i > 0 ){
        ll curr = v[i] ;
        while(q.size() >0 and q.front().fi <= curr){
            q.pop_front() ;
        }
        while(q.sz > 0 and q.back().fi <= curr){
            q.pop_back();
        }
        q.push_back({curr , i}) ;
       }
    }
    vl ans ;
    ans.pb(q.front().fi ) ;
    forn(i , k , n - 1 ) {
       while(q.sz >= k) q.pop_front() ;
       while(1) {
        if(q.sz == 0 ) br ;
         ll ind = q.front().se ;
         ll ele = i - ind + 1 ;
         if(ele > k){
            q.pop_front() ;
            con ;
         }
         else {
            br ;
         }
       }
       ll curr = v[i] ;
       while(q.size() > 0 and q.front().fi <= curr){
        q.pop_back();
       }
       while(q.sz > 0 and q.back().fi <= curr){
        q.pop_back() ;
       }
       q.push_back({curr , i}) ;
       ans.pb(q.front().fi) ;
    }
        return ans ; 
    }
};