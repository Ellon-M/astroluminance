import glob
import sys
import os
import numpy as np
from astropy.io import fits
import astroalign as aa


# I/O

target_name = "M13"
light_files = [f for f in glob.glob('{}/*.fit'.format(target_name))]
output_file = os.getcwd() + '/{}.fit'.format(target_name)

bias_f_name = os.getcwd() + "/MasterBias.fit"
dark_f_name = os.getcwd() + "/MasterDark.fit"



# Load the master dark frame
darkframe = dark_f_name
print('dark frame: ' + darkframe)
hdul_dark = fits.open(darkframe)
data_dark = hdul_dark[0].data
hdul_dark.close()

# Load the master bias frame
biasframe = bias_f_name
print('bias frame: ' + biasframe)
hdul_bias = fits.open(biasframe)
data_bias = hdul_bias[0].data
hdul_bias.close()


# Take the target for alignment to be the first of the light frames
targetframe = light_files[0]
print('target frame: ' + targetframe)
hdul_target = fits.open(targetframe)
data_target = hdul_target[0].data
hdul_target.close()

# Calibrate the target frame
data_target -= data_dark # subtract out the dark noise
data_target -= data_bias # subtract out the read noise
newdata_target = data_target.byteswap().newbyteorder()

image_concat = [] # empty list of aligned frames

print("Aligning " + str(len(light_files)) + " images")
for i in range(0, len(light_files)):
    hdul_im = fits.open(light_files[i])
    data_im = hdul_im[0].data # light frame data
    hdul_im.close()
    data_im -= data_dark # subtract out the dark noise
    data_im -= data_bias # subtract out the read noise

	# swap byte order from FITS big-endian to little-endian
	# so that little-endian based astroalign will work
    newdata_im = data_im.byteswap().newbyteorder() 

    # call the registration routine to align the frame
    try:
        data_aligned, footprint = aa.register(newdata_im, newdata_target)
        image_concat.append(data_aligned) # add the aligned frame
    except aa.MaxIterError:
        print("Failed to align "+light_files[i]+" skipping...")

print("Stacking " + str(len(light_files)) + " images")
final_image = np.zeros(shape=image_concat[0].shape)

# Average the aligned images
for image in image_concat:
        final_image += image

final_image = final_image / len(image_concat)
hdu = fits.PrimaryHDU(final_image)
print("Writing out stacked image: "+output_file)
hdu.writeto(output_file, overwrite=True)
