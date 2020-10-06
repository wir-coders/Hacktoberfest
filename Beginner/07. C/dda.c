#include<stdio.h> 
#include<conio.h> 
#include<graphics.h> 
#include<math.h> 
void main() 
{ 
  float x,y,x1,y1,x2,y2,dx,dy,step; 
  int i,gd=DETECT,gm; 
  initgraph(&gd,&gm,"c:\\turboc3\\bgi"); 
  printf("Enter the starting coordinates (x1 and y1): "); 
  scanf("%f%f",&x1,&y1); 
  printf("Enter the ending coordinates (x2 and y2): "); 
  scanf("%f%f",&x2,&y2); 
  dx=abs(x2-x1); 
  dy=abs(y2-y1); 
  step=(dx>=dy?dx:dy); 
  dx=dx/step; 
  dy=dy/step; 
  x=x1; 
  y=y1; 
  for(i=0;i<step;i++) 
  { 
    if(i%5>0) 
      putpixel(x,y,3); 
    x+=dx; 
    y+=dy; 
  } 
  getch(); 
}
