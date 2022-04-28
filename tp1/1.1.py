import numpy as np
from tables import type_b_dom
from scipy import stats

###############################################################################
#   Datos
###############################################################################
mean = 100.145          # Media de las mediciones
s = 1.489               # Desvio muestral
n = 20                  # Cantidad de mediciones
ic = 0.95               # intervalo de confianza 95%

###############################################################################
#   Ejercicio
###############################################################################
u_i = s/np.sqrt(n)                                  # Incertidumbre tipo A, desvio de la media.

u_j = 0.005 * 100.1 + 3/1001                        # Incetidumbre tipo B. Se asume que las cuentas totales son 1001 y la medición promedio fue 100.1

u_c = np.sqrt(u_i**2 + u_j**2 )                     # Incertidumbre combinada

v_eff = u_c**4 / (u_i**4/(n-1))                     # Grados efectivos de libertad

if (v_eff < 100):
    print ("Usando t de student.")
    u_exp = u_c * np.abs(stats.t.ppf((1-ic)/2 , np.round(v_eff,0)))      #t de student con veff Dof al 95%

else:
    print ("Usando tipo B dominante.")
    u_exp = u_c * type_b_dom(u_i, u_j)


print (f"""Los datos obtenidos son:
    u_i     = {u_i}
    u_j     = {u_j}
    u_c     = {u_c}
    v_eff   = {np.round(v_eff,0)}
    u_exp   = {u_exp}
    """)

print (f"Intervalo de confianza al 95%: {mean} +- {u_exp}")