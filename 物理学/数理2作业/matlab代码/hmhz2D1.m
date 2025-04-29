N = 101; 
h = 2 / (N-1); 
cnt = 0;
cnt_to_n = zeros(N*N);
n_to_cnt = zeros(N*N);

X = [0];
Y = [0]; 

for n = 1:N*N
    i = mod(n-1, N)+1;
    j = floor(n/N)+1;
    if ( (i-1)*h - 1 )^2 + ( (j-1)*h - 1 )^2 < 1
        cnt = cnt + 1;
        cnt_to_n(cnt) = n;
        n_to_cnt(n) = cnt;
        X(cnt) = (i-1)*h;
        Y(cnt) = (j-1)*h;
    end
end

M = zeros(cnt, cnt);

for k = 1:cnt
    M(k, k) = -4;
    n = cnt_to_n(k);
    i = mod(n-1, N) + 1;
    j = floor(n/N) + 1;

    if i > 1 && n_to_cnt(n-1) > 0
        M(k, n_to_cnt(n-1) ) = 1;
    end

    if  i<N && n_to_cnt(n+1) > 0
        M(k, n_to_cnt(n+1) ) = 1;
    end

    if j>1 && n_to_cnt(n-N) > 0
        M(k, n_to_cnt(n-N) ) = 1;
    end    

    if j < N && n_to_cnt(n+N) > 0
        M(k, n_to_cnt(n+N) ) = 1;
    end    

end

M = -M./(h^2);

[V, D] = eig(M);

x = 1:12;
y = zeros(12);

for i = 1:12
    y(i) = sqrt(D(i, i));
end

figure(1);
scatter(x, y);
xlabel("i");
ylabel("k_i");

for i =1:12
    text(i,y(i), num2str(y(i)));
end

[xq, yq] = meshgrid(0:0.02:2, 0:0.02:2);

figure(2);

for k = 1:12
    subplot(3,4,k);
    Z = V(:, k);
    zq = griddata(X,Y,Z,xq,yq);
    mesh(xq,yq,zq);
    title([num2str(k), 'th eig mode']);
    xlabel('x');
    ylabel('y');
    zlabel('u');
end




