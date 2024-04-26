from copy import deepcopy

jurusan_ilkom = {"Ilmu Komputer", "Manajemen Informatika"}
jurusan_ilkom_salinan = deepcopy(jurusan_ilkom)

jurusan_ilkom_salinan.add("Sistem Informasi")

print(jurusan_ilkom)  
print(jurusan_ilkom_salinan)  