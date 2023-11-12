#include<stdio.h>
#include<math.h>

double square_sum(double a[5][5]){
	
	double sum = 0.0;
	int i, j;
	
	for(i=0; i<5; i++){
		
		for(j=0; j<5; j++){
			
			if(j==i){
				continue;
			}
			
			sum += a[i][j] * a[i][j];
			
		}
		
	}
	
	return sum;
}

int find_max(double a[5][5]){
	
	int i, j;
	int index = 1;
	double max = 0;
	
	for(i=0; i<5; i++){
		
		for(j=i+1; j<5; j++){
			
			if( fabs(a[i][j]) > max ){
				
				max = fabs(a[i][j]);
				index = 10*i + j;
				
			}
			
		}
		
	}
	
	return index;
	
}

int main(){
	
	double a[5][5] = { {-13, 6, 13, 2, -17}, {6, 19, 17, 14, -7}, {13, 17, 7, -10, -13}, {2, 14, -10, -6, -15}, {-17, -7, -13, -15, 4} };
	double a_copy[5][5] = { {-13, 6, 13, 2, -17}, {6, 19, 17, 14, -7}, {13, 17, 7, -10, -13}, {2, 14, -10, -6, -15}, {-17, -7, -13, -15, 4} };
	double P[5][5] = {0.0};
	double I[5][5] = {0.0};
	double tmp_m[5][5] = {0.0};
	double store[5][5];
	
	double eps = 1e-12;
	
	double t, t_1, t_2, s;
	double c, d;
	
	int index;
	int p, q;
	int i, j, k;
	double tmp_1, tmp_2, tmp_3 = 0;
	
	for(i=0; i<5; i++){
		P[i][i] = 1.0;
	}
	
	for(i=0; i<5; i++){
		I[i][i] = 1.0;
	}
	
	for(i=0; i<5; i++){
		tmp_m[i][i] = 1.0;
	}
	
	while( square_sum(a) > eps ){
		
		for(i=0; i<5; i++){
			
			for(j=0; j<5; j++){
				
				tmp_m[i][j] = I[i][j];
				
			}
			
		}
		
		index = find_max(a);
		p = index / 10;
		q = index % 10;
		
		s = (a[q][q]-a[p][p]) / 2.0 / a[p][q];
		
		if(s==0.0){
			t = 1.0;
		}else{
			t_1 = -s - sqrt(s*s+1);
			t_2 = -s + sqrt(s*s+1);
			
			if( fabs(t_1)>fabs(t_2) ){
				t = t_2;
			}else{
				t = t_1;
			}
		}
		
		
		c = 1 / sqrt(1+t*t);
		d = t / sqrt(1+t*t);
		
		for(i=0; i<5; i++){
			
			if(i!=p && i!=q){
			
			tmp_1 = a[p][i];
			tmp_2 = a[q][i];
			
			a[p][i] = c*tmp_1-d*tmp_2;
			a[i][p] = a[p][i];
			a[q][i] = c*tmp_2+d*tmp_1;
			a[i][q] = a[q][i]; 
			
			}
			
		}
			
			tmp_1 = a[p][q];
			
			a[p][p] = a[p][p] - t*tmp_1;
			a[q][q] = a[q][q] + t*tmp_1;
			
			a[p][q] = 0.0;
			a[q][p] = 0.0;
			
		tmp_m[q][q] = c;
		tmp_m[p][p] = c;
		tmp_m[p][q] = d;
		tmp_m[q][p] = -d;
		
		for(i=0; i<5; i++){
			
			for(j=0; j<5; j++){
				
				tmp_3 = 0;

				for(k=0; k<5; k++){
					
					tmp_3 += P[i][k]*tmp_m[k][j];
					
				}
				
				store[i][j] = tmp_3;
				
			}
			
		}
		
		for(i=0; i<5; i++){
			
			for(j=0; j<5; j++){
				
				P[i][j] = store[i][j];
				
			}
			
		}
		
		for(i=0; i<5; i++){
			
			for(j=0; j<5; j++){
				
				tmp_m[i][j] = I[i][j];
				
			}
			
		}
		
	}
	
	for(i=0; i<5; i++){
		printf("%.3lf\n", a[i][i]);	
	}
	
	for(i=0; i<5; i++){
		
		for(j=0; j<5; j++){
			
			printf("%.3lf  ",store[i][j]);
			
		}
		
		printf("\n");
		
	}
	
	return 0;
}
