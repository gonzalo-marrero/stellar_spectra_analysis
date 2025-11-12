"""
Stellar Spectra Analysis
Authors: Gonzalo Marrero, Pablo Jiménez, Nöel Cortes.
"""

import warnings
import matplotlib.pyplot as plt
import numpy as np
from specutils.fitting import fit_generic_continuum
from specutils.spectra import Spectrum1D
from astropy import units as u
import os
import glob

# -------------------------------
# CONFIG
# -------------------------------
DATA_REF = "../data1"       # Carpeta con archivos de referencia
DATA_TARGET = "../data2"    # Carpeta con archivos target
PLOTS_DIR = "../docs/plots"
os.makedirs(PLOTS_DIR, exist_ok=True)

# -------------------------------
# FUNCIONES
# -------------------------------
def load_spectrum(file_path):
    """Carga un espectro desde un archivo .txt"""
    return np.loadtxt(file_path)

def plot_spectrum(wavelength, flux, label="", save_path=None):
    """Plotea un espectro con líneas guía"""
    plt.figure(figsize=(10,5))
    plt.plot(wavelength, flux, label=label)
    
    # Líneas guía importantes
    lines = [
        (4552,'r','Si III'), (4471,'b','He I'), (4481,'r','Mg II'),
        (4541,'c','He II'), (4340,'m','H_gamma'), (4100,'m','H_alpha'),
        (4860,'m','H_beta'), (3934,'k','Ca II'), (4226,'y','Ca I'),
        (4383,'y','Fe I'), (4300,'c','Sr II'), (3970,'m','H_epsilon')
    ]
    for line, color, lab in lines:
        plt.axvline(line, color=color, linestyle='--', label=lab)
    
    plt.title(label)
    plt.xlim(3800,5000)
    plt.ylim(0,1.2)
    if save_path:
        plt.savefig(save_path)
    plt.show()

# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    # Procesar todos los espectros de referencia
    ref_files = sorted(glob.glob(os.path.join(DATA_REF, "*.txt")))
    for ref_file in ref_files:
        data_ref = load_spectrum(ref_file)
        filename = os.path.basename(ref_file).split(".")[0]
        plot_spectrum(
            data_ref[:,0], data_ref[:,1],
            label=f"Reference {filename}",
            save_path=os.path.join(PLOTS_DIR, f"{filename}.png")
        )

    # Procesar todos los espectros target
    target_files = sorted(glob.glob(os.path.join(DATA_TARGET, "*.txt")))
    for target_file in target_files:
        data_target = load_spectrum(target_file)
        filename = os.path.basename(target_file).split(".")[0]
        
        # No
