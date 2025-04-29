z = 0:0.1:20;
J = zeros(10, 201);

for i = 0:9
    J(i+1,:) = besselj(i, z);
end

plot(z,J);
grid on;
legend('J_0','J_1','J_2','J_3','J_4','J_5','J_6','J_7','J_8','J_9', 'Location','Best');
title('Bessel Functions of the First Kind for $\nu \in [0, 9]$','interpreter','latex');
xlabel('z','interpreter','latex');
ylabel('$J_\nu(z)$','interpreter','latex');