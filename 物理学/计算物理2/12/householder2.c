#include<stdio.h>
#include<math.h>

void zero_m(double a[5][5]){
	
	int i, j;
	
	for(i=0; i<5; i++){
		
		for(j=0; j<5; j++){
			
			a[i][j] = 0.0;
			
		}
		
	}
	
}

void zero_vec(double a[5]){
	
	int i;
	
	for(i=0; i<5; i++){
		
		a[i] = 0;
		
	}
	
}

int main(){
	
	int i, j, k, l;
	
	double a[5][5] = { {9, 7, 5, 3, 1}, {7, 2, 4, 6, 8}, {5, 4, 10, 12, 14}, {3, 6, 12, 11, 13}, {1, 8, 14, 13, 15} };
	double b[5][5];
	double omega[5];
	double tmp_m[5][5];
	double max=0;
	
	double I[5][5] = {0.0};
	double v[5];
	
	double alpha, beta, sigma, yita;
	
	double tmp_1;
	double tmp_v[5];
	
	for(i=0; i<5; i++){
		
		I[i][i] = 1.0;
		
	}
	
	for(i=0; i<5; i++){
		
		tmp_1 = 0;
		max = 0; 
		
		for(j=i; j<5; j++){
			
			if( fabs(a[j][i])>max ){
				
				max = fabs(a[j][i]);
				
			}
			
		}
		
		yita = max;
		
		zero_vec(tmp_v);
		zero_vec(v);
		
		sigma = 0;
		
		for(j=i; j<5; j++){
	
			tmp_v[j] = a[j][i] / yita;
			
		}
		
		for(j=i+1; j<5; j++){
			
			sigma += tmp_v[j]*tmp_v[j];
			
		}
		
		for(j=i+1; j<5; j++){
			
			v[j] = tmp_v[j];
			
		}
		
		if(sigma == 0){
			
			beta = 0;
			
		}else{
			
			alpha = sqrt( tmp_v[i]*tmp_v[i] + sigma );
			
			if(tmp_v[i] <= 0 ){
				
				v[i] = tmp_v[i] - alpha;
				
			}else{
				
				v[i] = -sigma/(tmp_v[i]+alpha);
				
			}
			
			beta = 2*v[i]*v[i]/( sigma+v[i]*v[i] );
			
			for(j=i; j<5; j++){
				
				v[j] = v[j] / v[i];
				
			}
			
		}
		
		zero_vec(omega);
		
		for(j=i; j<5; j++){
			
			for(k=i; k<5; k++){
				
				omega[j] += beta*a[k][j]*v[k];
				
			}
			
		}
		
		zero_m(tmp_m);
		zero_m(b);
		
		for(j=i; j<5; j++){
			
			for(k=i; k<5; k++){
				
				b[j][k] = a[j][k] - v[j]*omega[k];
				
			}
			
			
		}
		
		for(j=i; j<5; j++){
			
			for(k=i; k<5; k++){
				
				a[j][k] = b[j][k];
				
			}
			
		}
		
	}
	
		for(i=0; i<5; i++){
		
			for(j=0; j<5; j++){
			
			printf("%lf ",a[i][j]);
			
		}
		
		printf("\n");
		
	}
	

	return 0;
	
	
}
