import glob
import sys
import os
import numpy as np
from astropy.io import fits


# I/O
flat_files = [f for f in glob.glob('Flats/*.fit')]
flat_f_name = os.getcwd() + "/MasterFlat.fit"

bias_f_name = os.getcwd() + "/MasterBias.fit"
dark_f_name = os.getcwd() + "/MasterDark.fit"


def inv_median(a):
    return 1 / np.median(a)

# Open the master dark frame
darkframe = bias_f_name
print('dark frame: ' + darkframe)
hdul_dark = fits.open(darkframe)
data_dark = hdul_dark[0].data
hdul_dark.close()

# Open the master bias frame
biasframe = bias_f_name
print('bias frame: ' + biasframe)
hdul_bias = fits.open(biasframe)
data_bias = hdul_bias[0].data
hdul_bias.close()


# Open each flat frame, subtract out the bias and
# dark noise and normalize before averaging
image_concat = []
for i in range(0, len(flat_files)):
    hdul_im = fits.open(flat_files[i])
    data_im = hdul_im[0].data
    data_im -= data_bias
    data_im -= data_dark
    data_im *= inv_median(data_im)
    image_concat.append(data_im)
    hdul_im.close()

print("Averaging flat images")
final_image = np.zeros(shape=image_concat[0].shape)
for image in image_concat:
    final_image += image

final_image = final_image / len(image_concat)

hdu = fits.PrimaryHDU(final_image)
print("Writing master flat: "+ flat_f_name)
hdu.writeto(flat_f_name, overwrite=True)
