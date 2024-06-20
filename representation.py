import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('obj_database.csv')

etoiles = df[df['type'] == 6]
galaxies = df[df['type'] == 3]

plt.figure(figsize=(10, 6))
plt.scatter(etoiles['ra'], etoiles['dec'], color='red', label='Étoiles', s=3)
plt.scatter(galaxies['ra'], galaxies['dec'], color='blue', label='Galaxies', s=3)
plt.xlabel('RA')
plt.ylabel('Dec')
plt.title('Distribution des objets astronomiques')
plt.legend()
plt.show()