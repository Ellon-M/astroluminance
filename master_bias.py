import glob
import sys
import os
import numpy as np
from astropy.io import fits

# I/O
bias_f_name = os.getcwd() + "/MasterBias.fit"
bias_files = [f for f in glob.glob('Bias/*.fit')]


# load the FITS files
image_concat = []
for i in range(0, len(bias_files)):
    hdul_im = fits.open(bias_files[i])
    data_im = hdul_im[0].data
    image_concat.append(data_im)
    hdul_im.close()

print("Averaging bias frames")
final_image = np.zeros(shape=image_concat[0].shape)
for image in image_concat:
    final_image += image

final_image = final_image / len(image_concat)

hdu = fits.PrimaryHDU(final_image)
hdu.writeto(bias_f_name, overwrite=True)
print(bias_f_name)
