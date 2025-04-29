a = 0;
b = 1;
f = @(x) 1./(1+0.3.*sin(pi.*(x-a)./(b-a)));
phi = @(n, x) sin(n.*pi./(b-a).*(x-a));
n = 200;
    
M = zeros(n, n);
    
for i = 1:n
    for j = 1:n
        int_func = @(x) f(x).*phi(i, x).*phi(j, x);
        tmp_1 = integral(int_func, a, b);
        tmp_2 = integral(@(x) phi(i, x).^2, a, b);
        M(i, j) = (j.*pi./(b-a)).^2 * tmp_1 ./ tmp_2;
    end
end   

[V, D] = eig(M);

[mu, index] = sort(sqrt(diag(D)));
V = V(:,index);

x = 1:n;
y = zeros(1, n);

for i = 1:n
    y(i) = mu(i);
end

figure(1);
scatter(x, y);
xlabel('n');
ylabel('\mu_n');
title('谱方法数值计算前200个本征值');

func_arr = cell(n, 1);

for i = 1:n
    func_arr{i} = @(x) phi(i, x);
end

figure(2);

for i = 1:12
    subplot(4, 3, i);
    u = @(x) 0;
    for j =1:n
        u = @(x) u(x) + func_arr{j}(x) * V(j, i);
    end
    x = a:0.01:b;
    y = u(x);
    plot(x, y);
    title(['本征值\mu_{',num2str(i), '}=',num2str(mu(i)), '的本征函数']);
    hold on;
end