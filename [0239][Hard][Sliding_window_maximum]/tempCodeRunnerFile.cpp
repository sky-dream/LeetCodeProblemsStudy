        result.push_back(q.front().first ) ;
            for(int i=k;i<=n-1;++i) {
                while(q.size() >= k) q.pop_front() ;
                while(1) {
                    if(q.size() == 0 ) break ;
                    int ind = q.front().second ;
                    int ele = i - ind + 1 ;
                    if(ele > k){
                        q.pop_front() ;
                        continue;
                    }
                    else {
                        break ;
                    }
            }
            while(q.size() > 0 and q.back().first <= nums[i]){
                q.pop_back() ;
            }
            q.push_back({nums[i] , i}) ;
            result.push_back(q.front().first) ;
        }