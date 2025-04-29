#include<stdio.h>
#include<math.h>
# define a 0.0
# define b 1.0
# define pi 3.14159265359

double epsilon = 0.00000001;

double f(double x){
	return 4/(1+x*x);
}

int main(){
	
	int n = 1;
	int i;
	int cnt = 0;
	double  T_n, H_n, T1, T2;
	double h =(b-a)/n;
	T_n = (f(a)+f(b))/2;
	
	for(i=1; i<n; i++){
		T_n += f(a+h*i);
	}
	
	T_n *= h;
	
	T2 = T_n;
	T1 = T2 + 100;
	
	do{
		cnt ++;
		
		T1 = T2;
		
		for(i=0, H_n=0; i<n; i++){
			H_n += f(a + h*i + h/2);
		}
		
		H_n *= h;
		T2 = (T1 + H_n)/2;
		h /= 2;
		n *= 2;
		
	}while(fabs(T2-M_PI) > epsilon);
	
	printf("T=%lf\n",T2);
	printf("step:%d",cnt);
	
	
	return 0;
}
