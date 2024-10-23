#%% 
import numpy as np
import skimage as ski
import matplotlib.pyplot as plt
from skimage import measure, color, io
#%%
print(ski.__version__)
#%%
ruta_img = "img_25_50.png"
img = ski.io.imread(ruta_img)

plt.imshow(img)
plt.show()


# %%
img_gris = ski.color.rgb2gray(ski.color.rgba2rgb(img))
img_gris = (img_gris * 255).astype(int)
img_gris[img_gris == 84] = 1 
# %%
plt.imshow(img_gris)
plt.show()
#%%

img_etiquetado = ski.measure.label(img_gris, connectivity=1) # conectivity 1 son 4 vecinos

plt.imshow(img_etiquetado, cmap = "prism")
plt.show()
# %%
propiedades = ski.measure.regionprops(img_etiquetado) 
# cada elemento corresponde a una regio distinta
# propiedades[0]['area']

tamanios =np.array([region['area'] for region in propiedades])
tamanios

# %%
t_min = tamanios.min()
t_max = tamanios.max()

bins = range(int(t_min), int(t_max) + 2)

hist, bordes_bins = np.histogram(tamanios, bins = bins, density=True)

plt.plot(bordes_bins[:-1], hist, 's', markersize=4, color='b' )
plt.xscale('log')
plt.yscale('log')
plt.xlabel( 'Tamaño de parche $s$ (pixeles)')
plt.ylabel('$P(s)$')
plt.title('Distribucion de tamaño de parche')
plt.show()

#%%
log_bins = np.logspace(np.log10(t_min), np.log10(t_max +2),7)
hist_log, bordes_bins_log = np.histogram(tamanios, bins = log_bins, density = False)
hist_log = hist_log / len(tamanios)

plt.plot(bordes_bins_log[:-1], hist_log, 's', markersize=4, color='b' )
plt.xscale('log')
plt.yscale('log')
plt.xlabel( 'Tamaño de parche $s$ (pixeles)')
plt.ylabel('$P(s)$')
plt.title('Distribucion de tamaño de parche (bin logaritmico)')
plt.show()

#%%
ccdf = np.array([hist[i:].sum() for i in range(len(hist))])
plt.plot(bordes_bins[:-1], ccdf, 's', markersize=4, color='b' )
plt.xscale('log')
plt.yscale('log')
plt.xlabel( 'Tamaño de parche $s$ (pixeles)')
plt.ylabel('$P(>s)$')
plt.title('Distribucion acumulada complementaria de tamaño de parche')
plt.show()
# %%
ccdf_log = np.array([hist_log[i:].sum() for i in range(len(hist_log))])
plt.plot(bordes_bins_log[:-1], ccdf_log, 's', markersize=4, color='b' )
plt.xscale('log')
plt.yscale('log')
plt.xlabel( 'Tamaño de parche $s$ (pixeles)')
plt.ylabel('$P(>s)$')
plt.title('Distribucion acumulada complementaria de tamaño de parche (bin logaritmico)')
plt.show()