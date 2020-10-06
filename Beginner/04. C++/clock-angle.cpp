#include <iostream>

using namespace std;

float min(float x, float y)  
{  
    return (x < y)? x: y;  
} 

int main(){
	float hh, mm;

	scanf("%f:%f", &hh, &mm);
	float hasil;
	float jam, menit;
	
	if(hh > 12){
		hh -= 12;
	}

	if (mm == 60) mm = 0;


	jam = mm * 6;

	menit = 0.5 * (hh * 60 + mm);
	
	float sudut = abs(jam - menit);

	sudut = min(360 - sudut, sudut);

	printf("%.1f\n", sudut);

	return 0;
}
