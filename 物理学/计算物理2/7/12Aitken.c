# include<stdio.h>

double f_1(double x){ // x = x^2 - 7 +x 简单迭代 
	return x*x-7+x;
}

double f_2(double x){ // x = 7/x 简单迭代 
	return 7.0/x;
}


int main(){
	
	double init_1 = 1.0;
	double init_2 = 3.0;
	
	double a[11];
	
	int i;
	
	/* 方法1 Aitken 加速 */
	
		/* f_1, init = 1.0 */
	
	a[0] = init_1;
	
	for(i=1; i<=10; i++){
		a[i] = a[i-1] - ( f_1(a[i-1])-a[i-1] )*( f_1(a[i-1])-a[i-1] ) / ( f_1( f_1(a[i-1]) ) - 2*f_1(a[i-1]) + a[i-1] );
	}
	
	for(i=0; i<=10; i++){
		printf("iteration %d, x%d:%lf\n", i, i, a[i]);
	}
	
	/* 方法1 Aitken 加速 */
	
		/* f_1, init = 3.0 */
		
	a[0] = init_2;
	
	for(i=1; i<=10; i++){
		a[i] = a[i-1] - ( f_1(a[i-1])-a[i-1] )*( f_1(a[i-1])-a[i-1] ) / ( f_1( f_1(a[i-1]) ) - 2*f_1(a[i-1]) + a[i-1] );
	}
	
	for(i=0; i<=10; i++){
		printf("iteration %d, x%d:%lf\n", i, i, a[i]);
	}
	
	/* 方法2 Aitken 加速 */
	
		/* f_2, init = 1.0 */
		
		a[0] = init_1;
	
	for(i=1; i<=10; i++){
		a[i] = a[i-1] - ( f_2(a[i-1])-a[i-1] )*( f_2(a[i-1])-a[i-1] ) / ( f_2( f_2(a[i-1]) ) - 2*f_2(a[i-1]) + a[i-1] );
	}
	
	for(i=0; i<=10; i++){
		printf("iteration %d, x%d:%lf\n", i, i, a[i]);
	}
	
	/* 方法2 Aitken 加速 */
	
		/* f_2, init = 3.0 */
		
		a[0] = init_2;
	
	for(i=1; i<=10; i++){
		a[i] = a[i-1] - ( f_2(a[i-1])-a[i-1] )*( f_2(a[i-1])-a[i-1] ) / ( f_2( f_2(a[i-1]) ) - 2*f_2(a[i-1]) + a[i-1] );
	}
	
	for(i=0; i<=10; i++){
		printf("iteration %d, x%d:%lf\n", i, i, a[i]);
	}
	
	return 0;
}
