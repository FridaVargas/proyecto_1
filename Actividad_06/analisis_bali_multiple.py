#%%
import numpy as np
import skimage as ski
import matplotlib.pyplot as plt

# Lo que sucede va a depender de: (a) plagas
#                                 (b) disponibilidad de agua

## Caso donde b > 20a aparecen muchas vecindades pequeñas 
"""
1. a = 0.06, b = 6
2. a = 0.3, b = 8
"""

## Caso donde b = 20a 
"""
1. a = 0.2, b = 4
"""

## Caso donde b < 20a aparecen cuatro  cuadrantes distintos
"""
1. a = 0.3, b = 5
2. a = 0.1, b = 0.1
"""

#%%
# imágenes a analizar
rutas_imgs = ["img_06_60.png", "img_3_80.png", "img_2_40.png", "img_3_50.png", "img_01_01.png"]

# etiquetas de los parámetros que se van a poner en la figura
a_params = [0.06, 0.3, 0.2, 0.3, 0.1]
b_params = [6, 8, 4, 5, 0.1]
# filas de la figura: imagen, dist tamaños, dist tamaños con bins logarítimcos
# dist acumulada complementaria tamaños, dist acumulada complementaria tamaños con bins log 
rows = 5
 
fig, axs = plt.subplots(rows,len(rutas_imgs),
                        squeeze=False,
                        figsize=(10,14),
                        layout="constrained")

for i in range(len(rutas_imgs)):
    # se importa la imagen
    img = ski.io.imread(rutas_imgs[i])
    
    # se procesa y etiqueta la imagen por regiones
    img_gris = ski.color.rgb2gray(ski.color.rgba2rgb(img))
    img_gris = (img_gris * 255).astype(int)
    img_etiquetada = ski.measure.label(img_gris,
                                       connectivity = 1)
    # se le calculan los tamaños de vecindad
    propiedades = ski.measure.regionprops(img_etiquetada)
    tamanios = np.array([region['area'] for region in propiedades])

    # se generan los histogramas
    t_min = tamanios.min()
    t_max = tamanios.max()
    
    bins =  range(int(t_min), int(t_max + 2))
    hist, bordes_bins = np.histogram(tamanios,
                                     bins = bins,
                                     density = True)

    log_bins = np.logspace(np.log10(t_min),np.log10(t_max + 2),7)
    hist_log, bordes_bins_log = np.histogram(tamanios,
                                             bins = log_bins,
                                             density = False)
    hist_log = hist_log / len(tamanios)

    ccdf = np.array([hist[i:].sum() for i in range(len(hist))])
    ccdf_log = np.array([hist_log[i:].sum() for i in range(len(hist_log))])

    # se grafica
    # límites máximos y mínimos de la gráfica
    xmin, xmax = 0, 10e2
    ymin, ymax = 10e-3, 1.5

    # en la primera fila se grafica la imágen y se indican los parámetros a y b
    k = 0
    axs[k,i].imshow(img)
    axs[k,i].axis('off')
    axs[k,i].set_title('$a = %.2f$; $b = %.1f$' %(a_params[i], b_params[i]),{'fontsize':10})

    # en la segunda fila se grafica la distribución de tamaños
    k = 1
    axs[k,i].plot(bordes_bins[:-1], hist, 's',markersize=3, color='b')
    axs[k,i].set_xscale('log')
    axs[k,i].set_yscale('log')
    axs[k,i].set_xlim([xmin, xmax])
    axs[k,i].set_ylim([ymin, ymax])
    if i == 0: axs[k,i].set_ylabel('$P(s)$') # si es la primera columna se deja el nombre del eje
    if i > 0: axs[k,i].set_yticks([]) # si no es la primera columna se quitan las etiquetas de los ejes
    axs[k,i].set_xticks([]) # se le quitan las etiquetas de los ejes

    # en la tercera fila se grafica la distribución de tamaños con bins logarítmicos
    k = 2
    axs[k,i].plot(bordes_bins_log[:-1], hist_log, 's',markersize=4, color='b')
    axs[k,i].set_xscale('log')
    axs[k,i].set_yscale('log')
    axs[k,i].set_xlim([xmin, xmax])
    axs[k,i].set_ylim([ymin, ymax])
    if i == 0: axs[k,i].set_ylabel('$P(s)$') # si es la primera columna se deja el nombre del eje
    if i > 0: axs[k,i].set_yticks([]) # si no es la primera columna se quitan las etiquetas de los ejes
    axs[k,i].set_xticks([]) # se le quitan las etiquetas de los ejes

    # en la cuarta se grafica la distribución acumulada complementaria
    k = 3
    axs[k,i].plot(bordes_bins[:-1], ccdf, 's',markersize=3, color='b')
    axs[k,i].set_xscale('log')
    axs[k,i].set_yscale('log')
    axs[k,i].set_xlim([xmin, xmax])
    axs[k,i].set_ylim([ymin, ymax])
    if i == 0: axs[k,i].set_ylabel('$P(>s)$')
    if i > 0: axs[k,i].set_yticks([])
    axs[k,i].set_xticks([]) # se le quitan las etiquetas de los ejes

    # en la quinta se grafica la distribución acumulada complementaria con bins logarítmicos
    k = 4
    axs[k,i].plot(bordes_bins_log[:-1], ccdf_log, 's',markersize=4, color='b')
    axs[k,i].set_xscale('log')
    axs[k,i].set_yscale('log')
    axs[k,i].set_xlim([xmin, xmax])
    axs[k,i].set_ylim([ymin, ymax])
    if i == 0: axs[k,i].set_ylabel('$P(>s)$')  # si es la primera columna se deja el nombre del eje
    if i > 0: axs[k,i].set_yticks([])  # si no es la primera columna se quitan las etiquetas de los ejes

# se agrega un título de eje x para todas las columnas
fig.supxlabel('Tamaño de parche $s$ (pixeles)')
fig.show()

# %%
fig.savefig("comparacion_regimenes.png")

