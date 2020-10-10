 //the questions asked are answered below
#include<stdio.h>
struct deisel_car{     //categories for diesel car
    float efficiency;
    float fuel_left;                                                               
};
struct electric_car{    //categories for electric car
    float efficiency;
    float battery_left;                                                               
};
int main()
{
    int n;
    scanf("%d",&n);
    int p = n;
    int choice[p];
    struct deisel_car c1[n];           //array of structs
    struct electric_car c2[n]; 
    int index_choice = 0,index_deisel = 0,index_electric = 0;
    while(p--)
    {
        int c;
        float eff,rem;
        scanf("%d %f %f",&c,&eff,&rem);
        choice[index_choice++] = c;
        if(c==1)                    //adding to the aray
        {
            c1[index_deisel].efficiency = eff;
            c1[index_deisel].fuel_left = rem;
            index_deisel++; 
        }
        else
        {
            c2[index_electric].efficiency = eff;
            c2[index_electric].battery_left = rem;
            index_electric++;
        }
    }
    index_deisel--;
    index_electric--;
    for(int i = n-1 ; i>=0 ; i--)
    {
        if(choice[i] == 1)
        {
            float ans = c1[index_deisel].efficiency*c1[index_deisel].fuel_left;
            printf("Car %d --> %.2f\n",i+1,ans);
            index_deisel--;
        }
        if(choice[i]==2)
        {
            float ans = (1000*c2[index_electric].battery_left)/c2[index_electric].efficiency;
            printf("Car %d --> %.2f\n",i+1,ans);
            index_electric--;
        }
    }
    return 0;
}
/* 1) since we have created two different structures once for deisel and other for electric we can
easily add and replace attributes of our choice and we can solve the questions accrodingly. */
/* 2) the first method is to directly store the asnwers in the array and then sort the array using quicksort
we can sort and then print the elements 
        or 
we can create a avl tree and then do inorder traversal on it and strore the sorted elements in the form of a array 
for this we have to create a new data structure for tree and store the left and right pointers and the value and the height.
*/    
