#include<stdio.h>
#include<math.h>

double L(int n, double * x, double * y, double input){
	
	int k, i;
	float output = 0.0;
	float w_n_plus_1 = 1.0;
	float w_n_plus_1_prime;
	
	for(i=0; i<=n; i++){
		w_n_plus_1 *= input - x[i];
	}
	
	for(k=0; k<=n; k++){	
		w_n_plus_1_prime = 1.0;
		i=0;
		
		for(i=0; i<=n; i++){
			if(i!=k){
				w_n_plus_1_prime *= x[k] - x[i];
			}
		}
		
		output += y[k] / (input - x[k]) / w_n_plus_1_prime;
	}
	
	output *= w_n_plus_1;
	
	return output;
}

int main(){
	
	double x_1[3] = {1.0, 4.0, 9.0};
	double y_1[3] = {1.0, 2.0, 3.0};
	
	int n_1 = 2;
	int n_2 = 3;	
	
	double err_1, err_2;
	
	double result_1, result_2;
	
	result_1 = L(n_1, x_1, y_1, 7.0);
	
	double x_2[4] = {1.0, 4.0, 9.0, 16.0};
	double y_2[4] = {1.0, 2.0, 3.0, 4.0};
	
	result_2 = L(n_2, x_2, y_2, 7.0);
	
	err_1 = fabs(result_1-sqrt(7));
	err_2 = fabs(result_2-sqrt(7));
	
	printf("二次插值的误差:%lf\n",err_1);
	printf("三次插值的误差:%lf",err_2);
	
	return 0;
}
