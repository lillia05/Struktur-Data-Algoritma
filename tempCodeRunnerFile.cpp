#include <iostream>
using namespace std;

int main(){
    int m, n;
    cin >> m >> n;
    int M[m][n];
    int T[m][n];

    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            cin>>M[i][j];
        }
    }
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
                T[j][i] = M[i][j];
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cout<<T[i][j];
        }
        return 0;
    }
}