x = linspace(0, 2*pi, 100);
y = zeros(size(x));

x_prime = pi;
l = 2*pi;

for k = 1000:2000
    y = y + sin(k*pi/l*x_prime)*sin(k*pi/l*x);
end

y = y*2/l;

plot(x,y);