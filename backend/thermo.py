from if97.iapws97 import IAPWS97

def water_props(T_C, P_MPa):
    T_K = T_C + 273.15
    w = IAPWS97(T=T_K, P=P_MPa)

    return {
        "state": state(T_K, P_MPa),
        "density": 1 / w.v,
        "specific_volume": w.v,
        "Cp": w.cp,
        "Cv": w.cv,
        "enthalpy": w.h,
        "entropy": w.s,
        "viscosity": w.mu,
        "thermal_conductivity": w.k
    }

def state(T_K, P_MPa):
    sat = IAPWS97(T=T_K, x=0)
    if abs(P_MPa - sat.P) < 1e-4:
        return "Saturated"
    elif P_MPa > sat.P:
        return "Subcooled liquid"
    else:
        return "Superheated vapor"
