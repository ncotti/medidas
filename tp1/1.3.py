import numpy as np
from scipy import stats
from tables import type_b_dom

###############################################################################
#   Datos
###############################################################################
I = np.array([10.01, 10.00, 10.02, 10.01, 10.00])
ic_disp = 0.99  # Intervalo de confianza del dispositivo
ic  = 0.95      # Intervalo de confianza buscado
u_exp_disp = (0.05/100)*10 + 2e-3   # Incertidumbre expandida del dispositivo

###############################################################################
#   Ejercicio
###############################################################################
error = I.mean() - 10       # Función de estimación del error

u_i = I.std(ddof=1)/np.sqrt(len(I))

u_j = u_exp_disp/np.abs(np.abs(stats.norm.ppf((1-ic_disp)/2))) 

u_c = np.sqrt(u_i**2 + u_j**2)

v_eff = u_c**4 * (len(I) - 1) / u_i**4

if (v_eff < 100):
    print ("Estimación por t de student")
    u_exp = u_c*np.abs(stats.t.ppf((1-ic)/2, np.round(v_eff,0))) # t(0.025, 9)

else:
    print ("Estimación por tipo B dominante")
    u_exp = u_c*type_b_dom(u_i, u_j)


print (f"""Los datos obtenidos son:
    u_i     = {u_i}
    u_j     = {u_j}
    u_c     = {u_c}
    v_eff   = {np.round(v_eff,0)}
    u_exp   = {u_exp}
    """)
print (f"Intervalo de confianza al 95%: {error} +- {u_exp}")




