import numpy as np
from scipy import stats

###############################################################################
#   Datos
###############################################################################
V = np.array([5.007, 4.994, 5.005, 4.990, 4.999])
I = np.array([19.663e-3, 19.639e-3, 19.640e-3, 19.685e-3, 19.678e-3])
Theta = np.array([1.0456, 1.0438, 1.0468, 1.0428, 1.0433])


###############################################################################
#   Datos comunes
###############################################################################
# Incertidumbres
u_i_v = V.std(ddof=1)/np.sqrt(len(V))
u_i_i = I.std(ddof=1)/np.sqrt(len(I))
u_i_t = Theta.std(ddof=1)/np.sqrt(len(Theta))

# Covarianzas
cov_matrix = np.cov([V, I, Theta])
cov_v_i = cov_matrix[0][1]/len(V)
cov_v_t = cov_matrix[0][2]/len(V)
cov_i_t = cov_matrix[1][2]/len(V)

###############################################################################
#   Función de R = V/I*cos(theta)
###############################################################################
dr_dv = ( 1/I.mean() ) *np.cos(Theta.mean())
dr_di = -V.mean()*np.cos(Theta.mean()) / I.mean()**2
dr_dt = V.mean()*(-np.sin(Theta.mean())) / I.mean()

u_c_r = np.sqrt( (dr_dv*u_i_v)**2 + (dr_di*u_i_i)**2 + (dr_dt*u_i_t)**2 +
   2*dr_dv*dr_di*cov_v_i + 2*dr_dv*dr_dt*cov_v_t + 2*dr_di*dr_dt*cov_i_t)


###############################################################################
#   Funcion de X = V/I*sen(theta) 
###############################################################################
dx_dv = (1/I.mean())*np.sin(Theta.mean())
dx_di = -V.mean()*np.sin(Theta.mean()) / I.mean()**2
dx_dt = V.mean()*np.cos(Theta.mean()) / I.mean()

u_c_x = np.sqrt( (dx_dv*u_i_v)**2 + (dx_di*u_i_i)**2 + (dx_dt*u_i_t)**2 +
    2*dx_dv*dx_di*cov_v_i + 2*dx_dv*dx_dt*cov_v_t + 2*dx_di*dx_dt*cov_i_t)


###############################################################################
#   Función de Z = V/I * e^iTheta = R + iX
###############################################################################
# La incertidumbre de la parte real es la de R, la de la parte real es la X,
# la de la fase es la de Theta, y falta hallar la del módulo.
# Tomando de referencia |Z| = V/I
dz_dv = 1/I.mean()
dz_di = -V.mean()/I.mean()**2

u_c_z = np.sqrt( (dz_dv*u_i_v)**2 + (dz_di*u_i_i)**2 + 2*dz_dv*dz_di*cov_v_i)

print (f"""u_c_r: {u_c_r}
u_c_x: {u_c_x}
u_c_z: 
    Parte real: {u_c_r}
    Parte imaginaria: {u_c_x}
    Módulo: {u_c_z}
    Fase: {u_i_t}""")

