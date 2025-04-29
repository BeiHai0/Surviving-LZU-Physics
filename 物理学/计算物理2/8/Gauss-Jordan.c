# include<stdio.h>
# include<math.h>

int main(){	
	
	double a[6][7] = { {1, -1, 1, 0, 0, 0, 0}, {1, -1, 0, 1, 0, 0, 0}, {0, 0, 1, 0, -1, 1, 0}, {2, 4, 0, 0, 0, 0, 10}, {0, 4, 1, 2, 2, 0, 17}, {0, 0, 0, 0, 2, 4, 14} }; 
	int i, j, k, index;
	double max, tmp;
	int m = 6, n = 7;
	
	for(i=0; i<m-1; i++){
		
		for( j=i+1, index=i, max = fabs(a[i][i]); j<m; j++ ){
			
			if( fabs(a[j][i])>max ){
				index = j;
				max = fabs(a[j][i]);
			}
			
		}
		
		if(i<index){
			
			for(k=0; k<n; k++){
				tmp = a[i][k];
				a[i][k] = a[index][k];
				a[index][k] = tmp;
			}
			
		}
		
		for(j=i+1; j<m; j++){
			
			tmp = -a[j][i] / a[i][i];
			
			for(k=0;k<n; k++){
				a[j][k] += tmp * a[i][k];
			}
			
		}
		
		
	
	}
	
	for(i=5; i>0; i--){
		
		for(j=i-1; j>=0; j--){
			
			tmp = -a[j][i] / a[i][i];
			a[j][i] = 0.0;
			a[j][6] += tmp * a[i][6];
						
		}
		
	}
	
	for(i=0 ;i<6; i++){
		a[i][6] /= a[i][i];
		a[i][i] =1.0;
	}
	
	for(i=0;i<6;i++){
		for(j=0;j<7;j++){
			printf("%lf ",a[i][j]);
		}
		
		printf("\n");
		
	}
	
	for(i=0;i<6;i++){
		printf("I%d = %lf\n",i+1, a[i][6]);
	}
	
	return 0;
}


















