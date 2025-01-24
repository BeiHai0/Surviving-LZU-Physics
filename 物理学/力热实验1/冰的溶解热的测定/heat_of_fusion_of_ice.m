t1 = linspace(0, 80, 5);
T1p = [41.7, 41.6, 41.4, 41.4, 41.2];
t1
p1 = polyfit(t1, T1p, 1);
p1

x1 = linspace(0, 470); % 原来是 0,80
y1 = polyval(p1, x1);

% 经过python 过定点一次函数拟合得到直线1的参数p1
x1 = linspace(0, 470);
p1 = [-0.00633333, 41.70666667];
y1 = polyval(p1, x1);


t2 = linspace(85, 325, 49);
T2p1 = [38.1, 33.8, 32.4, 30.0, 28.5, 26.2, 24.8, 24.4, 23.9, 23.6, 22.3, 21.9, 21.5, 21.3, 21.3, 21.2, 21.0, 21.0, 21.0, 20.9];
T2p2 = ones(1,29) * 20.6;
T2p = [T2p1,T2p2];
t2
T2p
p2 = polyfit(t2, T2p, 12);
p2
x2 = linspace(81, 327); % 原来是 85, 325
y2 = polyval(p2, x2);


t3 = linspace(330, 470, 8);
T3p = [20.7, 20.8, 20.8, 20.8, 20.8, 20.8, 20.8, 21.0];
t3
p3 = polyfit(t3, T3p, 1);
p3

x3 = linspace(0, 470); % 原来是330,470
y3 = polyval(p3, x3);

% 经过python 过定点一次函数拟合得到直线3的参数3
x3 = linspace(0, 470);
p3 = [0.00150000, 20.20500000];
y3 = polyval(p3, x3);

p1 = padarray(p1, [0, 11], "pre"); %对p1进行填充，使其与p2大小一致
p1
p_1_minus_2 = p1 - p2;
q1_2 = polyint(p_1_minus_2);
x_0_12 = 81.75859; % 目测曲线1,2交点位置

p3 = padarray(p3, [0,11], "pre"); %对p3进行填充
p3
p_3_minus_2 = p3 -p2;
q3_2 = polyint(p_3_minus_2);
x_0_23 = 326.31661; % 目测曲线2,3交点位置

min = 10000000000;

for i = x_0_12:0.1:x_0_23
    I_1 = diff(polyval(q1_2,[x_0_12, i]));
    I_2 = diff(polyval(q3_2,[i, x_0_23]));
    S = I_1 + I_2;
    if abs(S) > min
        break
    end
    min = abs(S);
end

i

T_above = polyval(p1, i);
T_under = polyval(p3, i);

s1 = sprintf("(%f,%f)",i, T_above);
s2 = sprintf("(%f,%f)",i, T_under);


figure
plot(t1, T1p, '.')
hold on
plot(t2, T2p, '.')
plot(t3, T3p, '.')
title("冰的熔解热的测定拟合曲线")
xlabel("时间t/秒")
ylabel("温度T/摄氏度")
plot(x1, y1)
plot(x2, y2)
plot(x3, y3)
line([i, i],[0, 50])
plot(i,T_above,'o')
plot(i,T_under,'o')
text([i,i],[T_above+2,T_under-2,],{s1,s2})
hold off

