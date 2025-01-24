#include<stdio.h>
#include<math.h>

double f_1(double x, double y, double z){
	return x-5*y*y+7*z*z+12;
}

double f_2(double x, double y, double z){
	return 3*x*y+x*z-11*x;
}

double f_3(double x, double y, double z){
	return y*z+20*x;
}

double F(double x, double y, double z){ 
	return f_1(x, y, z)*f_1(x, y, z) + f_2(x, y, z)*f_2(x, y, z) + f_3(x, y, z)*f_3(x, y, z);
}

int main(){
	
	double delta = 1e-8;
	double eps = 1e-8;
	double F_k;
	int cnt = 0;
	
	double F_x, F_y, F_z;
	double x_0 = -1.5, y_0 = 6.5, z_0 = -5.0;
	double x_1, y_1, z_1;
 	double lambda;
	
	while(1){
		
		F_k = F(x_0, y_0, z_0);
		
		if(fabs(F_k)<eps){
			break;
		}
		
		F_x = ( F(x_0+delta, y_0, z_0) - F(x_0, y_0, z_0) ) / (delta);
		F_y = ( F(x_0, y_0+delta, z_0) - F(x_0, y_0, z_0) ) / (delta);
		F_z = ( F(x_0, y_0, z_0+delta) - F(x_0, y_0, z_0) ) / (delta);
		
		lambda = F_k / (F_x*F_x + F_y*F_y + F_z*F_z);
		
		x_1 = x_0 - lambda*F_x;
		y_1 = y_0 - lambda*F_y;
		z_1 = z_0 - lambda*F_z;
		
		x_0 = x_1;
		y_0 = y_1;
		z_0 = z_1;
		
		cnt ++;
		
	}
	
	printf("(%lf, %lf, %lf)\n",x_0, y_0, z_0);
	printf("iteration number:%d", cnt);
	
	return 0;
}
