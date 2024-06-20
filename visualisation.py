from sdss import Region

#17.0229695944904,2.82331103195887
ra = 17.0229695944904
dec = 2.82331103195887

reg = Region(ra, dec, fov=0.033)
reg.show()