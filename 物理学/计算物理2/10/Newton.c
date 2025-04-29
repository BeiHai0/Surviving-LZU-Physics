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

/* calculate partial derivative by hand */ 

double f_1_x(double x, double y, double z){
	return 1.0;
}

double f_1_y(double x, double y, double z){
	return -10*y;
}

double f_1_z(double x, double y, double z){
	return 14*z;
}

double f_2_x(double x, double y, double z){
	return 3*y+z-11.0;
}

double f_2_y(double x, double y, double z){
	return 3*x;
}

double f_2_z(double x, double y, double z){
	return x;
}

double f_3_x(double x, double y, double z){
	return 20.0;
}

double f_3_y(double x, double y, double z){
	return z;
}

double f_3_z(double x, double y, double z){
	return y;
}

int main(){
	
	double x_0 = -1.5, y_0 = 6.5, z_0 = -5.0;
	double x_1, y_1, z_1;
	double delta_x, delta_y, delta_z;
	
	double D, D_1, D_2, D_3;
	
	int cnt = 0;
	double eps = 1e-8;
	
	while(1){
		
		D = f_1_x(x_0, y_0, z_0) * ( f_2_y(x_0, y_0, z_0)*f_3_z(x_0, y_0, z_0)-f_2_z(x_0, y_0, z_0)*f_3_y(x_0, y_0, z_0) ) \
		- f_1_y(x_0, y_0, z_0) * ( f_2_x(x_0, y_0, z_0)*f_3_z(x_0, y_0, z_0)-f_2_z(x_0, y_0, z_0)*f_3_x(x_0, y_0, z_0) ) \
		+ f_1_z(x_0, y_0, z_0) * ( f_2_x(x_0, y_0, z_0)*f_3_y(x_0, y_0, z_0) - f_2_y(x_0, y_0, z_0)*f_3_x(x_0, y_0, z_0) );
		
		D_1 = f_1(x_0, y_0, z_0) * ( f_2_y(x_0, y_0, z_0)*f_3_z(x_0, y_0, z_0)-f_2_z(x_0, y_0, z_0)*f_3_y(x_0, y_0, z_0) ) \
		- f_2(x_0, y_0, z_0) * ( f_1_y(x_0, y_0, z_0)*f_3_z(x_0, y_0, z_0)-f_1_z(x_0, y_0, z_0)*f_3_y(x_0, y_0, z_0) ) \
		+ f_3(x_0, y_0, z_0) * ( f_1_y(x_0, y_0, z_0)*f_2_z(x_0, y_0, z_0)-f_1_z(x_0, y_0, z_0)*f_2_y(x_0, y_0, z_0) );
		
		D_2 = -f_1(x_0, y_0, z_0) * ( f_2_x(x_0, y_0, z_0)*f_3_z(x_0, y_0, z_0)-f_2_z(x_0, y_0, z_0)*f_3_x(x_0, y_0, z_0) ) \
		+ f_2(x_0, y_0, z_0) * ( f_1_x(x_0, y_0, z_0)*f_3_z(x_0, y_0, z_0)-f_1_z(x_0, y_0, z_0)*f_3_x(x_0, y_0, z_0) ) \
		- f_3(x_0, y_0, z_0) * ( f_1_x(x_0, y_0, z_0)*f_2_z(x_0, y_0, z_0)-f_1_z(x_0, y_0, z_0)*f_2_x(x_0, y_0, z_0) );
		
		D_3 = f_1(x_0, y_0, z_0) * ( f_2_x(x_0, y_0, z_0)*f_3_y(x_0, y_0, z_0)-f_2_y(x_0, y_0, z_0)*f_3_x(x_0, y_0, z_0) ) \
		- f_2(x_0, y_0, z_0) * ( f_1_x(x_0, y_0, z_0)*f_3_y(x_0, y_0, z_0)-f_1_y(x_0, y_0, z_0)*f_3_x(x_0, y_0, z_0) ) \
		+ f_3(x_0, y_0, z_0) * ( f_1_x(x_0, y_0, z_0)*f_2_y(x_0, y_0, z_0)-f_1_y(x_0, y_0, z_0)*f_2_x(x_0, y_0, z_0) );
		
		/* using Cramer's rule */
		
		delta_x = D_1/D;
		delta_y = D_2/D;
		delta_z = D_3/D;
		
		x_1 = x_0 - delta_x;
		y_1 = y_0 - delta_y;
		z_1 = z_0 - delta_z;
		

		if(fabs(delta_x)<eps && fabs(delta_y)<eps && fabs(delta_z)<eps){
			break;
		}
		
		x_0 = x_1;
		y_0 = y_1;
		z_0 = z_1;
		
		cnt ++;
		
	}
	
	printf("(%lf, %lf, %lf)\n",x_1, y_1, z_1);
	printf("iteration number:%d", cnt);
	
	return 0;
}
