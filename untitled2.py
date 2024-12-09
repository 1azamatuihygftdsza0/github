# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Grafik parametrlari
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')  # O'qlarni o'chirish

# Shtrixlarni yaratish
x = np.linspace(-8, 8, 20)  # 20 ta chiziq joylashuvi uchun x koordinatalari
y1 = np.sin(x) * 5          # Asosiy shtrixlar uchun sinus funksiya
y2 = y1 - 0.3               # Soya uchun o'zgartirilgan sinus funksiya

# Rangli soyani chizish
for i in range(5):
    ax.plot(x, y2 - i * 0.1, color=(0.2, 0.2, 0.2, 0.1 + 0.1 * i), linewidth=2.5)

# Asosiy shtrixlarni chizish
ax.plot(x, y1, color='m', linewidth=2.5, label='Asosiy shtrix')

# Grafikni ko'rsatish
plt.legend()
plt.show()

