#include<stdio.h>
#include<math.h>
#define pi 3.14159265

typedef struct tagPOINT{
	double x;
	double y;
} point;

int main(){
	
	int n = 5; // 5¸ö²åÖµµã
	int i, j;
	
	point points[5];
	double diff[5];
	point save[101];
	
	double x, tmp, newton; 
	
	points[0].x = 0.0;
	points[1].x = pi/2;
	points[2].x = pi;
	points[3].x = 3*pi/2;
	points[4].x = 2*pi;
	
	points[0].y = 0;
	points[1].y = 1;
	points[2].y = 0;
	points[3].y = -1;
	points[4].y = 0;
	
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
	
	fp_1 = fopen("a.txt", "w");
	
	for(i=0; i<=100; i++){
		fprintf(fp_1, "%lf\n",save[i].x);
	}
	
	fp_2 = fopen("b.txt", "w");
	
		for(i=0; i<=100; i++){
		fprintf(fp_2, "%lf\n",save[i].y);
	}
	
	return 0;
}

