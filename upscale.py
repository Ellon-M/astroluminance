# image upscaling w/ different deep learning architectures
up_res = cv2.dnn_superres.DnnSuperResImpl_create()

# ESPCN 4x scaling factor
# Training: Extraction of feature maps from LR images -> apply complex upscaling filters
ESPCNpth = "SR/ESPCN_x4.pb"


# EDSR 4x scaling factor
# Training: ResNet style, w/out batch norm layers. Upscaling using bicubic filters
EDSRpth = "SR/EDSR_x4.pb"

# LapSRN 8x scaling factor
# Training: Pyramid like architecture w/ deep feature extraction and 
#image reconstruction w/ skip connections. No batch norm layers.
LapSRNpth = "SR/LapSRN_x8.pb"


# Upscaling
# ESPCN
up_res.readModel(ESPCNpth)
up_res.setModel("espcn",4)
ESPCNresult = up_res.upsample(img)
ESPCN_out = "SR_ESPCN.png"
cv2.imwrite(ESPCN_out, ESPCNresult)

# # ESDR
up_res.readModel(EDSRpth)
up_res.setModel("edsr",4)
EDSRresult = up_res.upsample(img)
EDSR_out = "SR_ESDR.png"
cv2.imwrite(EDSR_out, EDSRresult)

#LapSRN
up_res.readModel(LapSRNpth)
up_res.setModel("lapsrn",8)
LapSRNresult = up_res.upsample(img)
LapSRN_out = "SR_LapSRN.png"
cv2.imwrite(LapSRN_out, LapSRNresult)

# Display
plt.figure(figsize=(20,12))
plt.subplot(1,3,1)
plt.imshow(ESPCNresult[:,:,::-1])
plt.subplot(1,3,2)
plt.imshow(EDSRresult[:,:,::-1])
plt.subplot(1,3,3)
plt.imshow(LapSRNresult[:,:,::-1])
plt.show()
