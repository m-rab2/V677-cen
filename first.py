from astropy.io import fits
import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt

fits_file_path = 'v677.fits'

# Read the FITS file
with fits.open(fits_file_path, mode="readonly") as hdulist:
    tess_data = hdulist[1].data

# Extract time and flux from the TESS data
time = tess_data['TIME']
flux = tess_data['SAP_FLUX']

# Create a LightCurve object from the time and flux data
lc = lk.LightCurve(time=time, flux=flux)

lc.scatter(marker=',', s=1, color='black')
plt.title('TESS Light Curve for V677 Cen')
plt.show()
