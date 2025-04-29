#include<stdio.h>
#include<math.h>

void Gauss_Seidel(double a[9][9], double b[9], double x[9]){
	
	int i, j;
	double delta = 0.000001;
	double max, tmp_1, tmp_2, tmp_3;
	
	do{
		
		max = 0.0;
		
		for(i=0; i<9; i++){
			
			tmp_1 = x[i];
			tmp_2 = 0.0;
			tmp_3 = 0.0;
			
			for(j=0; j<i; j++){
				
				tmp_2 += a[i][j] * x[j];
				
			}
			
			for(j=i; j<9; j++){
				
				tmp_3 += a[i][j] * x[j];
				
			}
			
			x[i] = x[i] + (b[i]-tmp_2-tmp_3) / a[i][i];
			
			if(fabs(x[i]-tmp_1)>max){
				
				max = fabs(x[i]-tmp_1);
				
			}
			
		}
	
	}while(max>delta);
	
}

int SOR(double a[9][9], double b[9], double x[9], double omega){
	
	int i, j;
	double delta = 0.000001;
	double max, tmp_1, tmp_2, tmp_3;
	int cnt = 0;
	
	do{
		
		cnt++;
		max = 0.0;
		
		for(i=0; i<9; i++){
			
			tmp_1 = x[i];
			tmp_2 = 0.0;
			tmp_3 = 0.0;
			
			for(j=0; j<i; j++){
				
				tmp_2 += a[i][j] * x[j];
				
			}
			
			for(j=i; j<9; j++){
				
				tmp_3 += a[i][j] * x[j];
				
			}
			
			x[i] = x[i] + omega/a[i][i]*( b[i]-tmp_2-tmp_3 );
			
			if(fabs(x[i]-tmp_1)>max){
				
				max = fabs(x[i]-tmp_1);
				
			}
			
		}
		
	}while(max>delta);
	
	return cnt;
			
}

int main(){
	
	int i, j;
	
	double b[9] = {-15, 27, -23, 0, -20, 12, -7, 7, 10};
	double a[9][9] = { 
	{31, -13, 0, 0, 0, -10, 0, 0, 0},
	{-13, 35, -9, 0, -11, 0, 0, 0, 0},
	{0, -9, 31, -10, 0, 0, 0, 0, 0},
	{0, 0, -10, 79, -30, 0, 0, 0, -9},
	{0, 0, 0, -30, 57, -7, 0, -5, 0},
	{0, 0, 0, 0, -7, 47, -30, 0, 0,},
	{0, 0, 0, 0, 0, -30, 41, 0, 0},
	{0, 0, 0, 0, -5, 0, 0, 27, -2},
	{0, 0, 0, -9, 0, 0, 0, -2, 29}
	};
	
	double x_1[9] = {0.0};
	double x_2[9] = {0.0};
	
	double omega;
	int step = 0;
	int min_step = 1e7;
	double chosen_omega;
	
	Gauss_Seidel(a, b, x_1);
	
	printf("Gauss-Seidel solution:\n");
	
	for(i=0; i<9; i++){
		
		printf("%lf\n",x_1[i]);
		
	}
	
	printf("#############################\nSOR solution:\n");
	
	for(i=1; i<=95; i++){
		
		omega = i/50.0;
		
		for(j=0; j<9; j++){
			x_2[j] = 0.0;
		}
		
		step = SOR(a, b, x_2, omega);
		
		if(step<min_step){
			min_step = step;
			chosen_omega = omega;
		}
		
		printf("omega=%lf:\n", omega);
		printf("step:%d\n", step);
		
		for(j=0; j<9;j++){
			
			printf("%lf\n",x_2[j]);
			
		}
		
	}
	
	printf("########################\nmin step:%d\n", min_step);
	printf("chosen omega:%lf\n", chosen_omega);
	
	double c[9] = {0.0};
	double d[9] = {0.0};
	double e[9][9];
	int bin;
	
	for(i=0; i<9; i++){
		
		c[i] = 1.0;
		
		for(j=0; j<9; j++){
			
			d[j] = 0;
		
		}
		
		bin = SOR(a, c, d, chosen_omega);
		
		for(j=0; j<9; j++){
			
			e[j][i] = d[j];
			
		}
		
		c[i] = 0.0;
		
	}
	
	printf("##########################\nA inverse:\n");
	
	for(i=0; i<9; i++){
		
		for(j=0; j<9; j++){
			
			printf("%lf ",e[i][j]);
			
		}
		
		printf("\n");
		
	}
	
	return 0;
	
}
