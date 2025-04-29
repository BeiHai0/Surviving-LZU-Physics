N = 1000;
a = 0;
b = 1;
delta_x = (b-a)./N;

x = linspace(a, b, N+1);
x = x(2:N);
y = 1 ./ (1+0.3.*sin(pi.*(x-a)./(b-a)));

m_1 = diag(y, 0);
m_2 = diag( -2.*ones(N-1, 1), 0 ) + diag( ones(N-2, 1), -1 ) + diag( ones(N-2, 1), 1 );

M = -1./delta_x^2.*m_1*m_2;

[V, D] = eig(M);

[mu, index] = sort(sqrt(diag(D)));
V = V(:,index);

n = 200;

x_1 = 1:n;
y_1 = mu(1:n);

figure(1);
scatter(x_1, y_1);
xlabel('n');
ylabel('\mu_n');
title('有限差分法数值计算前200个本征值');

figure(2);
for i =1:12
    subplot(4, 3, i);
    plot(x, V(:,i));
    title(['本征值\mu_{', num2str(i), '}=', num2str(mu(i)), '的本征函数']);
end

