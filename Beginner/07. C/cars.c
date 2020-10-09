#include<stdio.h>
#include<stdlib.h>

//Car object
struct car{
    int type;
    float effeciency;
    float batterySize;  //Battery size will br 0 for disel cars
    float fuel;
    float distance;
};


int main(){
    int numberOfCars;
    scanf("%d",&numberOfCars);
    struct car fleet[numberOfCars];  //Car Array
    for(int i=0;i<numberOfCars;i++){
        scanf("%d",&fleet[i].type);
        scanf("%f",&fleet[i].effeciency);
        scanf("%f",&fleet[i].fuel);
    }

    //Loop to calculate range of cars
    for(int i=0;i<numberOfCars;i++){
        //For diesel car
        if(fleet[i].type==1){
            fleet[i].batterySize=0; //No battery in disel cars
            fleet[i].distance = fleet[i].effeciency*fleet[i].fuel;
        }
        
        //For electric car
        else if(fleet[i].type==2){
            fleet[i].batterySize=100;  //100 kW-h
            fleet[i].distance = (((fleet[i].fuel/fleet[i].batterySize)*100)/fleet[i].effeciency)*1000;
        }
    }

    //Printing the result
    for(int i=numberOfCars-1;i>=0;i--){
        printf("The car %d can go upto %.2f\n",i+1,fleet[i].distance);
    }
    //We can sort the fleet array based on the distances calculated 
    //to print the cars in decreasing order of their ranges
}