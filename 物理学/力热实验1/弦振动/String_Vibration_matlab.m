x = ([10, 15, 20, 25, 30, 35, 40, 45]);
y = ([5.749, 6.990, 8.103, 9.048, 9.902, 10.689, 11.437, 12.129]).^2;
p = polyfit(x, y, 1);
p
x1 = linspace(0, 50);
y1 = polyval(p, x1);
figure
plot(x, y, 'o')
hold on
title("牛顿环")
xlabel("X")
ylabel("Y")
plot(x1, y1)
legend({"measured data","fitting line"})
hold off




