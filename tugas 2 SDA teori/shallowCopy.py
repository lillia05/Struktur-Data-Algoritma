biodata = ["Lia", 18, "Mahasiswa"] 
biodata_salinan = biodata[:]        # Shallow copy dari biodata

biodata_salinan[1] = 19             # Ubah umur di salinan

print("Biodata asli:", biodata)
print("Biodata salinan:", biodata_salinan)