import numpy as np
from scipy import stats

###############################################################################
#   Datos
###############################################################################
ic_fuente = 0.95 # Intervalo de confianza de la fuente de corriente
i_fuente = 10

v1 = 123.38
u_i_v1 = 50e-3
u_j_voltimetro_1 = (0.04/100 + 1/12338)*v1 # Escala en 400V, 1 dígito = 000.01

v2 = 346.42e-3
u_i_v2= 0.50e-3
u_j_voltimetro_2 = (0.04/100 + 1/34642)*v2 #Escala en 400mv, 1 digito = 000.01e-3


###############################################################################
#   Primera medición = R = V1/I1
###############################################################################
r = v1/i_fuente

dr_dv = 1 / i_fuente
dr_di = -v1 / i_fuente**2 

u_j_exp_fuente = (0.1/100)*i_fuente
u_j_fuente = u_j_exp_fuente / np.abs(stats.norm.ppf((1-ic_fuente)/2))

# Primero obtengo la incertidumbre combianda de los potenciales
u_c_v1 = np.sqrt(u_i_v1**2 + u_j_voltimetro_1**2)

# Y ahora obtengo la incertidumbre de la resistencia, usando la combinada de
# los potenciales
u_c_r = np.sqrt((dr_dv*u_c_v1)**2 + (dr_di*u_j_fuente)**2)

###############################################################################
#   Segunda medición I = V2/R
###############################################################################
i_medida = v2/r

di_dv = 1/r
di_dr = -v2/r**2

u_c_v2 = np.sqrt(u_i_v2**2 + u_j_voltimetro_2**2)

u_c_i = np.sqrt((di_dv*u_c_v2)**2 + (di_dr*u_c_r)**2)

###############################################################################
#   Potencia primera medición P1 = V1 * I_fuente
###############################################################################
p1 = v1*i_fuente

dp_dv = i_fuente
dp_di = v1

u_c_p = np.sqrt((dp_dv*u_c_v1)**2 + (dp_di*u_j_fuente)**2)

###############################################################################
#   Potencia segunda medición P2 = V2^2/R
###############################################################################
p2 = v2**2/r

dp2_dv = 2*v2/r
dp2_dr = -v2**2/r**2

u_c_p2= np.sqrt((dp2_dv*u_c_v2)**2 + (dp2_dr*u_c_r)**2)

###############################################################################
#   Output
###############################################################################
print (f"""Todos los resultados de incertidumbre se expresan con un\
intervalo de confianza de confianza de 1 sigma = 68.27%:
    Resistencia R = {r} +- {u_c_r}
    Corriente medida = {i_medida} +- {u_c_i}
    Potencia de la primera medición (P = V*I) = {p1} +- {u_c_p}
    Potencia de la segunda medición (P = V^2/R) = {p2} +- {u_c_p2}""")


