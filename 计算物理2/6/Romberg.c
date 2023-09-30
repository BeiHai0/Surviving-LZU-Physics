#include<stdio.h>
#include<math.h>
#define a 0.0
#define b 1.0

double f(double x){
	return 4/(1+x*x);
}

double epsilon = 0.00000001;

double computeT(double aa, double bb, long int n){
	int i;
	double sum;
	double h = (bb-aa)/n;
	
	for(i=1; i<n; i++){
		sum += f(aa + i*h);
	}
	
	sum += (f(aa)+f(bb))/2;
	sum *= h;
	
	return sum;
}

int main(){
	
	int i;
	long int n = 20, m = 0;
	
	
	double T[11][2];
	
	T[0][1] = computeT(a, b, n);
	n *= 2;
	
	for(m=1; m<21; m++){
	
		for(m=1; i<m; i++){
		T[i][0] = T[i][1];
		}
	
		T[0][1] = computeT(a, b, n);
		n *= 2;
	
		for(i=1; i<m; i++){
		T[i][1] = T[i-1][1] + (T[i-1][1]-T[i-1][0])/(pow(2, 2*m)-1);
		}
	
		if( fabs(T[m][1] - M_PI) < epsilon ){
			printf("the integrate is %lf\n",T[m][1]);
			break;
		}
	}	
	return 0;
}

