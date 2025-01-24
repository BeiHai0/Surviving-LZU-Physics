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
	
	double I[5][5] = {0.0};
	
	for(i=0; i<5; i++){
		
		I[i][i] = 1.0;
		
	}
	
	double H[5][5];
	
	zero_m(H);

	double v[5];
	
	zero_vec(v);
	
	double beta;
	double v_v_T[5][5];
	double mo;
	double tmp_1, tmp_2;
	
	double tmp_m[5][5];
	
	for(i=0; i<5; i++){
	
		zero_vec(v);
		
		tmp_1 = 0.0;
		
		for(j=i; j<5; j++){
			
			tmp_1 += a[j][i]*a[j][i];
			
		}
		
		v[i] = -(tmp_1 - a[i][i]*a[i][i]) / (a[i][i]+sqrt(tmp_1)) ;
		
		for(j=i+1; j<5; j++){
			
			v[j] = a[j][i] ;
			
		}
	
		beta = 0;
		
		for(j=i; j<5; j++){
			
			beta = v[j]*v[j];
			
		}
		
		beta = 2.0/beta;
		
		zero_m(v_v_T);
		
		for(j=i; j<5; j++){
			
			for(k=i; k<5; k++){
				
				v_v_T[j][k] = v[j] * v[k];
				
			}
			
		}
		
		for(j=0; j<5; j++){
			
			for(k=0; k<5; k++){
				
				H[j][k] = I[j][k] - beta*v_v_T[j][k];
				
			}
			
		}
		
		zero_m(tmp_m);
		
		for(j=0; j<5; j++){
			
			for(k=0; k<5; k++){
				
				for(l=0; l<5; l++){
					
					tmp_m[j][k] += H[j][l]*a[l][k];
					
				}
				
			}
			
		}
		
		for(j=0; j<5; j++){
			
			for(k=0; k<5; k++){
				
				a[j][k] = tmp_m[j][k];
				
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
