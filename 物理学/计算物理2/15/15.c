#include<stdio.h>

double f(double t, double x){
	double r = 2.5, K = 1000;
	return r*x*(1-x/K);
}

int main(){
	
	FILE *fp = fopen("result.txt", "w");
	
	double m = 2000.0;
	double h = 30.0/m;
	double x_0 = 150.0;
	double t, x = x_0;
	double k1, k2, k3, k4;
	
	int i;
	
	for(i=0 ; i<=m; i++){
		
		t = i*h;
		
		fprintf(fp, "%lf, %lf\n", t, x);
		
		k1 = f(t, x);
		k2 = f(t+h/2.0, x+h*k1/2.0);
		k3 = f(t+h/2.0, x+h*k2/2.0);
		k4 = f(t+h, x+h*k4);
		
		x += h/6.0*(k1 + 2.0*k2 + 2*k3 + k4);
		
	}
	
	fclose(fp);

	return 0;
}