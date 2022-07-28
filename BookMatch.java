

#include<bits/stdc++.h> 

using namespace std; 

int main(){ 

    string a, b; 

    cin >> a >> b; 

    map<char, int> m1, m2; 

    if(a == b){ 

        cout << a << endl; 

        cout << 100 << endl; 

        cout << "The book can be added in section" << endl; 

        return 0; 

    } 

    int n = a.length(); 

    string common; 

    for(auto ch: a) 

        m1[ch] += 1; 

    for(auto ch: b) 

        m2[ch] += 1; 

    for(auto it: m1){ 

        int low = min(it.second, m2[it.first]); 

        while(low--) 

            common += it.first; 

    } 

    int len = common.length(); 

    int percentage = (len * 100) / n; 

    if(percentage > 0){ 

        cout << common << endl; 

        cout << percentage << endl; 

        if(percentage > 70) 

            cout << "The book can be added in section" << endl; 

        else 

            cout << "NO Match!!The book can not be added in section" << endl; 

    } 

    else{ 

        cout << percentage << endl; 

        cout << "NO Match!!The book can not be added in section" << endl; 

    } 

    return 0; 

}
