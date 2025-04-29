#include<stdio.h>
#include<math.h>
#define PI 3.14159265

int main(){
	
	FILE *fp = fopen("result4.txt", "w");
	
	int i, j;
	
	double dt = 0.001, dx = 0.001;
	double phi[1001];
	double alpha[1000];
	double beta[1000];
	double gamma[1000];
	double b[1001];
	
	phi[0] = 0.0;
	phi[1001] = 0.0;
	
	for(i=1; i<1000 ;i++){
		
		phi[i] = sin(PI*i*dt);
		
	}
	
	double A_0, A_plus, A_minus;
	
	double w = 0.75;
	
	A_plus = -dt/dx/dx*(1-w);
	A_minus = A_plus;
	A_0 = 1+2*dt/dx/dx*(1-w);
	
	alpha[999] = 0;
	beta[999] = 0;	
	
	for(i=999; i>0; i--){
		
		gamma[i] = -1.0/(A_0+A_plus*alpha[i]);
		alpha[i-1] = gamma[i]*A_minus;
		
	}
	
	for(i=1 ;i<501; i++){
		
		for(j=999; j>0; j--){
			
			b[j] = w*dt/dx/dx*(phi[j+1]+phi[j-1]-2*phi[j])+phi[j];
			beta[j-1] = gamma[j]*(A_plus*beta[j]-b[j]);
			
		}
		
		for(j=1; j<1001; j++){
			
			phi[j] = alpha[j-1]*phi[j-1]+beta[j-1]; 
			
		}
		
	}
	
	for(i=0; i<1001; i++){
		
		fprintf(fp, "%lf, %lf\n", i*dt, phi[i]);
		
	}
	
	fclose(fp);
	
	return 0;
}