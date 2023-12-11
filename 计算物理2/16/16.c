#include<stdio.h>
#include<math.h>

double f(double t, double x, double y, double z){
	return -y-z;
}

double g(double t, double x, double y, double z){
	return x+0.2*y;
}

double p(double t, double x, double y, double z){
	return 0.2+(x-9.0)*z;
}

int main(){
	
	FILE *fp = fopen("result.txt", "w");
	
	int i;
	double h = 0.01;
	double R1, R2, R3, R4, L1, L2, L3, L4, K1, K2, K3, K4;
	double t, x = 1.0 ,y = 1.0, z = 1.0;
	
	for(i=0; i<=300000; i++){
		
		t = i*h;
		
		fprintf(fp, "%lf, %lf, %lf, %lf\n", t, x, y, z);
		
		R1 = f(t, x, y, z);
		L1 = g(t, x, y, z);
		K1 = p(t, x, y, z);
		R2 = f(t+h/2.0, x+h/2.0*R1, y+h/2.0*L1, z+h/2.0*K1);
		L2 = g(t+h/2.0, x+h/2.0*R1, y+h/2.0*L1, z+h/2.0*K1);
		K2 = p(t+h/2.0, x+h/2.0*R1, y+h/2.0*L1, z+h/2.0*K1);
		R3 = f(t+h/2.0, x+h/2.0*R2, y+h/2.0*L2, z+h/2.0*K2);
		L3 = g(t+h/2.0, x+h/2.0*R2, y+h/2.0*L2, z+h/2.0*K2);
		K3 = p(t+h/2.0, x+h/2.0*R2, y+h/2.0*L2, z+h/2.0*K2);
		R4 = f(t+h/2.0, x+h/2.0*R3, y+h/2.0*L3, z+h/2.0*K3);
		L4 = g(t+h/2.0, x+h/2.0*R3, y+h/2.0*L3, z+h/2.0*K3);
		K4 = p(t+h/2.0, x+h/2.0*R3, y+h/2.0*L3, z+h/2.0*K3);
		
		x += h/6.0*(R1+2*R2+2*R3+R4);
		y += h/6.0*(L1+2*L2+2*L3+L4);
		z += h/6.0*(K1+2*K2+2*K3+K4);
	}
	
	fclose(fp);
	
	return 0;
}