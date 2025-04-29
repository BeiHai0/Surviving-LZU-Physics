import numpy as np
import matplotlib.pyplot as plt

a = 0.115
b = 7.53e-4
c = 3e8
B = 7.4e-2
x_0 = 9.5e-2
m_0 = 9.11e-31 # 电子静止质量
m_0_c_c_in_MeV = m_0 * c * c * 1e-6 / 1.602 * 1e19 # m_0 c^2 在 MeV 作为单位时的数值

x = 1e-2 * np.array([34.90, 32.40, 30.00, 27.50, 24.00, 22.00])

pc = c * B * (x - x_0) / 2 * 1e-6

CH = np.array([995, 809, 581, 435, 335, 237])

E_k = a + b * CH

pc1 = np.linspace(1, 3, 100)

E_k1 = pc1**2 / ( 2 * m_0_c_c_in_MeV )

E_k2 = np.sqrt( (pc1)**2 + (m_0_c_c_in_MeV)**2 ) - (m_0_c_c_in_MeV)**2

plt.xlabel('pc(MeV)')
plt.ylabel('Ek(meV)')

plt.scatter(pc, E_k, label='measured data')
plt.plot(pc1, E_k1, label='classical theory')
plt.plot(pc1, E_k2, label='relativistic theory', linestyle='--')

plt.legend()
plt.show()