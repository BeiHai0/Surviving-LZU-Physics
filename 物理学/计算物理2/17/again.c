#include<stdio.h>
#include<math.h>
#include<stdlib.h>

double f(double x, double y){
	return -x*x*y;
}

int main(){
	
	FILE *fp = fopen("result.txt", "w");

	int i, j;
	
	double h = 0.06;
	double w = 1.5;
	double err, u_pre, u_after, tmp, x, y;
	double eps = 0.0001;
	
	double u[101][101], s[101][101];
	
	 for(i=0; i<101; i++){
	 	
	 	for(j=0; j<101; j++){
	 		
	 		if(i == 0 || i == 100 || j == 0 || j== 100 ){
	 			
	 			u[i][j] = 0.0;
	 			
			}else{
	 		
	 		u[i][j] = 1.0;
	 		
	 		}
	 		
	 		//printf("%lf\n", u[i][j]);
	 		
	 		x = i*h;
	 		y = -3.0+j*h;
	 		
	 		s[i][j] = f(x, y);
	 		
	 		//printf("%lf\n", s[i][j]);
	 		
		 }
	 	
	 }
	 
	 do{
	 	
	 	err = 0.0;
	 	
	 	for(i=1; i<100; i++){
	 		
	 		for(j=1; j<100; j++){
	 			
	 			u_pre = u[i][j];
	 			tmp = (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1]-h*h*s[i][j])/4.0;
	 			u_after = w*tmp + (1-w)*u_pre;
	 			u[i][j] = u_after;
	 			
	 			//printf("%lf", u[i][j]);
	 			
	 			if(err<fabs(u_after-u_pre)){
	 				
	 				err = fabs(u_after - u_pre);
	 				
				 }
	 				
			 }
	 		
		 }
	 	
	 }while(err>eps);
	 
	 for(i=0; i<101; i++){
	 	
	 	for(j=0; j<101; j++){
	 		
	 		fprintf(fp, "%d, %d, %lf\n", i, j, u[i][j]);
	 		
		 }
	 	
	 }
	 
	 fclose(fp);
	
	return 0;
	 
}