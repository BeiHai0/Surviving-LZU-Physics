# include<stdio.h>
# include<math.h>

double f_1(double x){ 
	return x*x*x*x - 4*x*x + 4;
}

double f_1_prime(double x){
	return 4*x*x*x - 8*x;
}

int main(){
	
	double delta = 0.000000001;
	int i, j;
	
	double a[500] = {0,0};
	
	/* Newton µü´ú·¨ */
	
	double init = 3.0;
	
	a[0] = init;
	i = 1;
	
	while( fabs( a[i-1] - sqrt(2.0) ) >= delta ){
		a[i] = a[i-1] - f_1(a[i-1]) / f_1_prime(a[i-1]);
		
		i++;
	}
	
	for(j=0; j<=i; j++){
		printf("iteration %d, x%d:%.10lf\n", j, j, a[j]);
	}
	
	/* ÏÒ½Ø·¨ */
	
	double b[300] = {0,0,0};
	
	double init_1 = 3.0;
	double init_2 = 2.0;
	
	b[0] = init_1;
	b[1] = init_2;
	i = 2;

	do{
		b[i] = b[i-1] - (b[i-1] - b[i-2]) / ( f_1(b[i-1]) - f_1(b[i-2]) ) * f_1(b[i-1]);
		
		i++;
	}while(fabs( b[i-1] - sqrt(2.0) ) <= delta);
	
	for(j=0; j<=i; j++){
		printf("iteration %d, x%d:%.10lf\n", j, j, b[j]);
	}
	
	return 0;
}
