from astropy.io import fits
import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle

fits_file_path = 'v677.fits'

# Read the FITS file
with fits.open(fits_file_path, mode="readonly") as hdulist:
    tess_data = hdulist[1].data

# Extract time and flux from the TESS data
time = tess_data['TIME']
flux = tess_data['SAP_FLUX']

# Create a LightCurve object from the time and flux data
lc = lk.LightCurve(time=time, flux=flux)

# Plot the light curve with smaller points
lc.scatter(marker=',', s=1, color='black')
plt.title('TESS Light Curve for V677 Cen')
plt.show()

# Compute the Lomb-Scargle periodogram to find potential binary star periods
frequency, power = LombScargle(lc.time, lc.flux).autopower(method='fast')
periods = 1 / frequency
print(periods)

# Find the main peak in the periodogram as the binary star period
best_period = periods[np.argmax(power)]
print(f"Best period for binary star: {best_period:.2f} days")