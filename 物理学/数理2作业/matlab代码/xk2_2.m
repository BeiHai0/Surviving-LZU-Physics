N = 101; 
h = 2 ./ (N-1); 
cnt = 0;
cnt_to_n = zeros(1, N*N);
n_to_cnt = zeros(1, N*N);

X = [0];
Y = [0]; 

for n = 1:N*N
    i = mod(n-1, N)+1;
    j = floor((n-1)/N)+1;
    if ( (i-1)*h - 1 )^2 + ( (j-1)*h - 1 )^2 < 1
        cnt = cnt + 1;
        cnt_to_n(cnt) = n;
        n_to_cnt(n) = cnt;
        X(cnt) = -1+(i-1)*h;
        Y(cnt) = -1+(j-1)*h;
    end
end

bessel_zero_1_1 = 3.8317;
M = zeros(cnt, cnt);
integral_1 = sqrt(integral(@(r) r.*besselj(1, bessel_zero_1_1.* r).^2, 0, 1 ));
f = @(x, y) 1./(1 + 0.2.*(cos(atan2(y, x)).*besselj(1, bessel_zero_1_1.*sqrt(x.^2+y.^2))./sqrt(pi)./integral_1));

for k = 1:cnt
    n = cnt_to_n(k);
    i = mod(n-1, N) + 1;
    j = floor((n-1)./N) + 1;
    x = -1 + (i-1).*h;
    y = -1 + (j-1).*h;
    F = f(x, y);
    M(k, k) = F.*(-4);
    if i > 1 && n_to_cnt(n-1) > 0
        M(k, n_to_cnt(n-1) ) = 1.*F;
    end

    if  i<N && n_to_cnt(n+1) > 0
        M(k, n_to_cnt(n+1) ) = 1.*F;
    end

    if j>1 && n_to_cnt(n-N) > 0
        M(k, n_to_cnt(n-N) ) = 1.*F;
    end    

    if j < N && n_to_cnt(n+N) > 0
        M(k, n_to_cnt(n+N) ) = 1.*F;
    end    

end

M = -M./(h.^2);

[V, D] = eig(M);
[mu, index] = sort(sqrt(diag(D)));
V = V(:, index);

x = 1000:1015;
y = zeros(1, 16);

for i = 1000:1015
    y(i-999) = mu(i);
end

figure(1);
scatter(x, y);
xlabel("i");
ylabel("k_i");

for i =1000:1015
    text(i,y(i-999), num2str(y(i-999)));
end

[xq, yq] = meshgrid(-1:0.02:1, -1:0.02:1);

figure(2);

for k = 1000:1015
    subplot(4,4,k-999);
    Z = V(:, k);
    zq = griddata(X,Y,Z,xq,yq);
    mesh(xq,yq,zq);
    title(['本征值\mu_{', num2str(k), '}=', num2str(mu(k)), '的本征函数']);
    xlabel('x');
    ylabel('y');
    zlabel('u');
end