###############################################################################
#   Tablas con valores de factor de cobertura K
###############################################################################
import numpy as np

def type_b_dom(u_i:float, u_j:float) -> float:
    entry  = u_i/u_j

    k = [1.65, 1.66, 1.68, 1.70, 1.72, 1.75, 1.77, 1.79, 1.82, 
        1.84, 1.85, 1.87, 1.89, 1.90, 1.91, 1.92, 1.93, 1.94, 
        1.95, 1.95, 1.96, 1.97, 1.98, 1.99, 1.99, 2.00]

    cutoff = [0.00, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 
        0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 
        0.90, 0.95, 1.00, 1.10, 1.20, 1.40, 1.80, 2.00, 2.50]

    out = 0


    for i in range(0, len(cutoff) -1 ):
        if ( entry >= cutoff[i] and entry < cutoff[i + 1] ):
            if (np.abs(entry - cutoff[i]) < np.abs(entry - cutoff[i+1]) ):
                out = k[i]

            else:
                out = k[i+1]

            break

        if (i == len(cutoff) - 2):
            out = k[-1]

    return out