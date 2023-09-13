#include<stdio.h>
#include<math.h>
#define pi 3.14159265

typedef struct tagPOINT{
	double x;
	double y;
} point;

int main(){
	
	int n = 9; // 9¸ö²åÖµµã
	int i, j;
	
	point points[9];
	double diff[9];
	point save[101];
	
	double x, tmp, newton; 
	
	points[0].x = 0.0;
	points[1].x = pi/6;
	points[2].x = pi/2;
	points[3].x = 5*pi/6;
	points[4].x = pi;
	points[5].x = 7*pi/2;
	points[6].x = 3*pi/2;
	points[7].x = 11*pi/2;
	points[8].x = 2*pi;
	
	points[0].y = 0;
	points[1].y = 0.5;
	points[2].y = 1;
	points[3].y = 0.5;
	points[4].y = 0;
	points[5].y = -0.5;
	points[6].y = -1;
	points[7].y = -0.5;
	points[8].y = 0;
	
	for(i=0; i<=n-1; i++){
		diff[i] = points[i].y;
	}
	
	for(i=0; i<n-1; i++){
		for(j=n-1; j>i; j--){
			diff[j] = (diff[j]-diff[j-1]) / (points[j].x-points[j-1-i].x);
		}
	}
	
	int cnt = 0;
	
	for(x=0; x<=2*pi; x+=2*pi/100){
		tmp = 1.0;
		newton = diff[0];
		for(i=0; i<n; i++){
			tmp *= (x-points[i].x);
			newton += tmp*diff[i+1];
		}
		save[cnt].y = newton;
		cnt++;
		printf("(%lf,%lf)\n",x,newton);
		
	}
	
	for(i=0; i<=100; i++){
		save[i].x = i*2*pi/100; 
	}
	
	FILE *fp_1, *fp_2;
	
	fp_1 = fopen("c.txt", "w");
	
	for(i=0; i<=100; i++){
		fprintf(fp_1, "%lf\n",save[i].x);
	}
	
	fp_2 = fopen("d.txt", "w");
	
		for(i=0; i<=100; i++){
		fprintf(fp_2, "%lf\n",save[i].y);
	}
	
	return 0;
}

