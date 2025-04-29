#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>

double f(double x){
	
	return exp(-2*fabs(x-5));
	
}

double w(double x){
	
	return 3.0/125*x*x; // ��Ҫ��ȡ�� 
	
}

double x(double y){
	
	return 5.0*pow(y, 1.0/3); // ����� x 
	
}

int main(){
	
	printf("�򵥳���###################################\n");
	
	int rand_int;
	double rand_double;
	
	double sigma_1 = 0.0, sigma_2 = 0.0, sigma = 0.0;
	double integral = 0.0;
	
	int i;
	
	srand(time(0));
	
	for(i=1; i<=1000001; i++){
	
		rand_int = rand()%10000;
		rand_double = rand_int/ 1000.0; // 0-10
		
		//printf("%lf\n", rand_double);
		
		sigma_1 += pow(f(rand_double), 2.0);
		sigma_2 += f(rand_double);
		
		integral += f(rand_double);
	
		if( i == 100 || i == 1000 || i== 10000 || i == 100000 || i == 1000000 ){
			
			printf("N=%d:\n", i);
			printf("ƽ��ֵ:%lf\n", integral/i);
			printf("����:%lf\n", 1.0/i *( (sigma_1)/i - pow(sigma_2/i , 2.0) ));
			printf("������:%lf\n", sqrt(1.0/i * ((sigma_1)/i - pow(sigma_2/i , 2.0)) ));
			
		}
		
	}

////////////////////////////////////////

	printf("��Ҫ�Գ���###################################\n");

	sigma_1 = 0.0;
	sigma_2 = 0.0;
	integral = 0.0;
	
	for(i=1; i<=1000001; i++){
	
		rand_int = rand()%10000; // ��ȷ��С����� 3 λ 
		rand_double = rand_int/ 1000.0/2; // 0-5
		
		//printf("%lf\n", rand_double);
		
		if(f(x(rand_double))/w(x(rand_double))>1000){ // ����ĸ̫С�������� 
			i--;
			continue;
		}
		
		sigma_1 += pow(f(x(rand_double))/w(x(rand_double)), 2.0);
		sigma_2 += f(x(rand_double)) / w(x(rand_double));
		
		integral += f(x(rand_double))/w(x(rand_double));
		//printf("%lf", x(rand_double));
		//printf("%lf\n", integral);
	
		if( i == 100 || i == 1000 || i== 10000 || i == 100000 || i == 1000000 ){
			
			printf("N=%d:\n",i);
			printf("ƽ��ֵ:%lf\n", 2*integral/i);
			printf("����:%lf\n", 1.0/i *( (sigma_1)/i - pow(sigma_2/i , 2.0) ));
			printf("������:%lf\n", sqrt(1.0/i * ((sigma_1)/i - pow(sigma_2/i , 2.0)) ));
			
		}
		
	}
	
	

	
	return 0;
	
}
