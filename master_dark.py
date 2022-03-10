import glob
import sys
import os
import numpy as np
from astropy.io import fits

# I/O
dark_files = [f for f in glob.glob('Darks/*.fit')]
dark_f_name = os.getcwd() + "/MasterDark.fit"
bias_f_name = os.getcwd() + "/MasterBias.fit"


# open the master bias frame
hdul_bias = fits.open(bias_f_name)
data_bias = hdul_bias[0].data
hdul_bias.close()

#open all the frames that will comprise the
#master dark frame, subtracting the bias noise from each one
image_concat = []
for i in range(0, len(dark_files)):
    hdul_im = fits.open(dark_files[i])
    data_im = hdul_im[0].data
    data_im -= data_bias
    image_concat.append(data_im)
    hdul_im.close()

print("Averaging dark frames")
final_image = np.zeros(shape=image_concat[0].shape)
for image in image_concat:
    final_image += image

final_image = final_image / len(image_concat)

hdu = fits.PrimaryHDU(final_image)
print("Writing master dark: "+dark_files)
hdu.writeto(dark_f_name, overwrite=True)
