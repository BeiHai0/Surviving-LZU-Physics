#include<stdio.h>
#include<math.h>

typedef struct tag_point{
	double x;
	double y;
}point;

int main(){
	
	int m = 9;
	int i;
	point points[9];
	double u11 = 9.0, u12 = 0.0, u21 = 0.0, u22 = 0.0, c1 = 0.0, c2 = 0.0;
	double a, b;
	points[0].x = -4.0;
	points[0].y = -3.0;
	points[1].x = -3.0;
	points[1].y = -1.0;
	points[2].x = -2.0;
	points[2].y = -2.0;
	points[3].x = -1.5;
	points[3].y = -0.5;
	points[4].x = -0.5;
	points[4].y = 1.0;
	points[5].x = 1.0;
	points[5].y = 0.0;
	points[6].x = 2.0;
	points[6].y = 1.5;
	points[7].x = 3.5;
	points[7].y = 1.0;
	points[8].x = 4.0;
	points[8].y = 2.5;
	
	for(i=0; i<m; i++){
		u21 += points[i].x;
		u22 += points[i].x * points[i].x;
		c1 += points[i].y;
		c2 += points[i].x * points[i].y;
	}
	
	u12 = u21;
	u11 = m;
	
	a = (c1*u22 - c2*u12) / (u11*u22 - u12*u21);
	b = (u11*c2 - u21*c1) / (u11*u22 - u12*u21);
	
	printf("ÄâºÏÇúÏßÎª:p(x)=%lf+%lfx\n", a, b);
	
	FILE *fp_1, *fp_2;
	
	fp_1 = fopen("a.txt", "w");
	fp_2 = fopen("b.txt", "w");
	
	for(i=0; i<m; i++){
		fprintf(fp_1, "%lf\n", points[i].x);
		fprintf(fp_2, "%lf\n", points[i].y);
	}
	
	return 0;
}
