#include <iostream>
#include <string.h>
using namespace std;
int main()
{   
    int t;
    cin>>t;
    while(t--){
        char str[1000];
        cin>>str;
        int len = strlen(str);

        int count1[26] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}, count2[26] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        
        if(len%2==0){
            for(int i = 0; i < len/2; i++){
                int pos = ((int) str[i]) - ((int) 'a');
                count1[pos]++;
                pos = ((int) str[i+len/2]) - ((int) 'a');
                count2[pos]++;
            }

        }else{
            
            for(int i = 0; i < len/2; i++){
                int pos = ((int) str[i]) - ((int) 'a');
                
                count1[pos]++;
                pos = ((int) str[i+len/2+1]) - ((int) 'a');
                count2[pos]++;
            }
        }
        bool valid = true;
        for(int i =0; i < 26; i++){
            if(count1[i] != count2[i]){
                valid = false;
                break;
            }
        }
        if(valid)
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
}