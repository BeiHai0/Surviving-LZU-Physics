# include<stdio.h>

double f_1(double x){ // x = x^2 - 7 +x 简单迭代 
	return x*x-7+x;
}

double f_2(double x){ //x = 7/x 简单迭代 
	return 7.0/x;
}

double f_3(double x){ //x=0.5*(x+7/x) 牛顿迭代法 
	return 0.5*(x+7/x);
}


int main(){
	
	int i;
	
	double a[6];
	
	double init_1 = 1.0;
	double init_2 = 3.0;
	
	/* f_1 */
	
	a[0] = init_1; 
	
	for(i=1; i<=5; i++){
		a[i] = f_1(a[i-1]);
	}
	
	for(i=0;i<=5;i++){
		printf("iteration %d, x%d:%lf\n", i, i, a[i]);
	}
	
	printf("###################\n");
	
	a[0] = init_2; 
	
	for(i=1; i<=5; i++){
		a[i] = f_1(a[i-1]);
	}
	
	for(i=0; i<=5; i++){
		printf("iteration %d, x%d:%lf\n", i, i, a[i]);
	}
	
	printf("###################\n");
	
	/* f_2 */
	
	a[0] = init_1; 
	
	for(i=1; i<=5; i++){
		a[i] = f_2(a[i-1]);
	}
	
	for(i=0;i<=5;i++){
		printf("iteration %d, x%d:%lf\n", i, i, a[i]);
	}
	
	printf("###################\n");
	
	a[0] = init_2; 
	
	for(i=1; i<=5; i++){
		a[i] = f_2(a[i-1]);
	}
	
	for(i=0; i<=5; i++){
		printf("iteration %d, x%d:%lf\n", i, i, a[i]);
	}
	
	printf("###################\n");
	
	/* f_3 */
	
	a[0] = init_1; 
	
	for(i=1; i<=5; i++){
		a[i] = f_3(a[i-1]);
	}
	
	for(i=0;i<=5;i++){
		printf("iteration %d, x%d:%lf\n", i, i, a[i]);
	}
	
	printf("###################\n");
	
	a[0] = init_2; 
	
	for(i=1; i<=5; i++){
		a[i] = f_3(a[i-1]);
	}
	
	for(i=0; i<=5; i++){
		printf("iteration %d, x%d:%lf\n", i, i, a[i]);
	}
	
	
	return 0;
}
