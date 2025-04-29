求解单位圆内的二维亥姆霍兹方程：

$$
(\nabla^2+k^2)u
=0
$$

# 解析解

极坐标系下，二维亥姆霍兹方程化为：

$$
\frac{1}{\rho}\frac{\partial }{\partial \rho}(\rho\frac{\partial u}{\partial \rho})+\frac{1}{\rho^2}\frac{\partial^2 u}{\partial \varphi^2}+k^2 u
=0
$$

设 $u(\rho,\varphi)=R(\rho)\Phi(\varphi) $，分离变量得：

$$
\frac{\mathrm{d}^2\Phi}{\mathrm{d}\varphi^2}+m^2\Phi
=0
$$

$$
\frac{1}{\rho}\frac{\mathrm{d}}{\mathrm{d}\rho}(\rho\frac{\mathrm{d}R}{\mathrm{d}\rho})+(k^2-\frac{m^2}{\rho^2})R
=0
$$

形式解为：

$$
\Phi^{(m)}(\varphi)
=A_m\cos(m\theta)+B_m\sin(m\theta)
$$

$$
R^{(m)}(\rho)
=C_m\mathrm{J}_m(k\rho)+D_m\mathrm{N}_m(k\rho)
$$

$R(0) $ 是有限的，于是：

$$
R^{(m)}(\rho)
=C_m\mathrm{J}_m(k\rho)
$$

## 第一类齐次边界条件

$$
u\bigg|_{\rho=1}
=0
$$

由此可得本征值：

$$
k_n^{(m)}
=x_n^{(m)}
$$

其中，$x_n^{(m)} $ 是 $m $ 阶贝塞尔函数 $\mathrm{J}_m $ 的第 $n $ 个零点

本征振动模式为：

$$
R_n^{(m)}(\rho)
=\mathrm{J}_m(x_n^{(m)}\rho)
$$

## 第二类齐次边界条件

$$
\frac{\partial u}{\partial n}\bigg|_{\rho=1}
=0
$$

由此可得本征值：

$$
k_n^{(m)}
=y_n^{(m)}
$$

其中，$y_n^{(m)} $ 是 $m $ 阶贝塞尔函数的导数 $\mathrm{J}_m' $ 的第 $n $ 个零点

本征振动模式为：

$$
R_n^{(m)}(\rho)
=\mathrm{J}_m(y_n^{(m)}\rho)
$$

# 数值解

## 第一类齐次边界条件

绘图如下：

![](img/9.png)

![](img/10.png)

matlab 代码如下：

```
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
```

## 第二类齐次边界条件

绘图如下：

![](img/11.png)

![](img/12.png)

matlab 代码如下：

```
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
    else
        M(k, k) = M(k, k) + 1;
    end

    if  i<N && n_to_cnt(n+1) > 0
        M(k, n_to_cnt(n+1) ) = 1;
    else
        M(k, k) = M(k, k) + 1;
    end

    if j>1 && n_to_cnt(n-N) > 0
        M(k, n_to_cnt(n-N) ) = 1;
    else
        M(k, k) = M(k, k) + 1;
    end    

    if j < N && n_to_cnt(n+N) > 0
        M(k, n_to_cnt(n+N) ) = 1;
    else
        M(k, k) = M(k, k) + 1;
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
```
