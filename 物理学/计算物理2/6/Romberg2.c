#include<stdio.h>
#include<math.h>
#define a 0.0
#define b 1.0

double epsilon = 0.00000001;

double f(double x){
	return 4/(1+x*x);
}

int main(){
	
	int R[25][25];
	int i, j;
	int n = 1;
	double h = b-a;
	int k = 2;
	double tmp;
	
	R[1][1] = (f(a) + f(b))*h/2;
	
	while(1){
		
		tmp = 0.0;
		
		for(i=1; i<=pow(2.0, k-2); i++){
			tmp += f(a + (2*i-1)*h/pow(2.0, k-1));
		}
		
		tmp *= h/pow(2.0, k-2);
		
		R[k][1] = (R[k-1][1] + tmp)/2;
		
		for(j=2; j<=k; j++){
			R[k][j] = R[k][j-1] + (R[k][j-1]-R[k-1][j-1])/(pow(4.0, j-1) - 1);
		}
		
		if(fabs(R[k][k] - M_PI) < epsilon){
			break;
		}
		
		k++;
	}
	
	printf("integrate:%lf\n",R[k][k]);
	printf("step:%d",k);
	
	return 0;
}
