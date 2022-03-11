# Image Processing: *M13 Globular Cluster* & the *NGC7333 Star*

Astronomical images are usually ‘refined’ or ‘processed’ as compared to the raw data that the astronomers work on with their computers. 
These images, taken by telescopes with electronic detectors, such as CCD chips, are always nearly grayscale and contain different levels of noise from various sources.


'*Pretty pictures*' such as these:

<img width="400px" height="auto" src="https://res.cloudinary.com/denphvygd/image/upload/v1646961810/astroluminance/2c0f2506279664c8c252cc8a30ce72d9_cwimry.jpg"/> , <img width="400px" height="275px" src="https://res.cloudinary.com/denphvygd/image/upload/v1646957423/astroluminance/NGC-5307_vidtkg.jpg"/> 


are routinely taken through a series of steps, involving filters, calibration, alignment, noise reduction and sometimes upscaled to appear as seen.


The workflow here is for monochrome images. 
The desire is to achieve considerable luminance in them such that star fields can be discerned visually- thus making plate solving possible.

<hr/>

**Processing Walkthrough**


- Calibration frames are captured along with the image frames to estimate noise which is then subtracted out. (*Thermal noise*: from the heat emitted by the CCD chips, 
 *Read/bias noise*: from the uncertainty of reading out a single CCD cell's value and *Optical noise*: caused by uneven illumination of the chip).

- Computation of a master bias frame from dark frames taken with extremely short exposure times (< 1/1000 second) to estimate the **read** 'noise' and subtract it.
- Computation of a master dark frame to estimate the **thermal** 'noise' generated in the CCD chip at a given temperature.
- Computation of a master flat frame to estimate the **optical** 'noise' caused by dust particles and uneven illumination of the CCD chip. 
- Aligning and stacking image frames correctly to remove some of the misalignment errors that occur due to mechanical and atmospheric 'noise' captured during each subframe's exposure and not having the mount's polar axis precisely aligned with the earth's axis.
- Applying flat fields (uniformly illuminated fields) to adjust image brightness.
- Curving and stretching the image to enhance the fainter parts. ( Photoshop curves tool works here too )
- Mild deconvolution to sharpen stars.
- Darkening the background to make the fainter stars more prominent.


**Super Resolution**

The image processing alone is enough to have a decent looking astronomical image. 

Upscaling the image afterwards, or before the process, is a preferential step that
is entirely situational depending on the final resolution of the image(s) at hand.  

<hr/>

**M13**

Imaging sequence:

Alignment & Stacking -> Brgihtness Equalize -> Stretching -> Deconvolution -> Darkened Background

<img width="250px" height="250px" src="https://res.cloudinary.com/denphvygd/image/upload/v1646957983/astroluminance/M13_firstproc_w77ews.png" /><img width="250px" height="250px" src="https://res.cloudinary.com/denphvygd/image/upload/v1646957983/astroluminance/M13_secondproc_yhordi.png" /><img width="250px" height="250px" src="https://res.cloudinary.com/denphvygd/image/upload/v1646957984/astroluminance/M13_thirdproc_pwsavj.png" />


<img width="250px" height="250px" src="https://res.cloudinary.com/denphvygd/image/upload/v1646957984/astroluminance/M13_fourthproc_weovqk.png" /><img width="250px" height="250px" src="https://res.cloudinary.com/denphvygd/image/upload/v1646957983/astroluminance/m13_final_cauoel.png" />



**NGC7333**


<img width="250px" height="250px" src="https://res.cloudinary.com/denphvygd/image/upload/v1646957984/astroluminance/NGC7333_firstproc_o8kw2c.png"/> <img width="250px" height="250px" src="https://res.cloudinary.com/denphvygd/image/upload/v1646957984/astroluminance/NGC7333_secondproc_dyhbov.png"/> <img width="250px" height="250px" src="https://res.cloudinary.com/denphvygd/image/upload/v1646957985/astroluminance/NGC7333_finalproc_s3jscd.png"/>


**Both Upscaled**

*3000 x 2300 Dims*

Files are too large for display.

M13 - [here](https://res.cloudinary.com/denphvygd/image/upload/v1646966469/astroluminance/SR_ESDR_dqahhe.png)


NGC7333 - [here](https://res.cloudinary.com/denphvygd/image/upload/v1646966469/astroluminance/SR_ESDR_2_obrynh.png)
