#!/usr/bin/env python

def area(lon_data,lat_data,model):

    # building grid
    nlon = np.shape(lon_data)[0]
    nlat = np.shape(lat_data)[0]
    xo = np.repeat(lon_data,nlat,axis=0).reshape((nlon,nlat))
    yo = np.transpose(np.repeat(lat_data,nlon,axis=0).reshape((nlat,nlon)))

    # building res grid
    resx = np.repeat((lon_data[1]-lon_data[0]),nlon,axis=0); #print(xres)
    if model=='foamatm':
        resy = np.array([4.407066, 4.420082, 4.436035, 4.440086, 4.441738, 4.442583, 4.443069, 4.443373, 4.443577, 4.443718, 4.443823, 4.443901, 4.443957, 4.444, 4.444035, 4.44406, 4.444079, 4.444092, 4.4441, 4.444105, 4.444105, 4.4441, 4.444092, 4.444079, 4.44406, 4.444035, 4.444, 4.443957, 4.443901, 4.443823, 4.443718, 4.443577, 4.443373, 4.443069, 4.442583, 4.441738, 4.440086, 4.436035, 4.420082, 4.407066])
    else:
        resy=np.repeat((lat_data[1]-lat_data[0]),nlat,axis=0); #print(yres)
    xres = np.repeat(resx,nlat,axis=0).reshape((nlon,nlat))
    yres = np.transpose(np.repeat(resy,nlon,axis=0).reshape((nlat,nlon)))
    # checked: yres, xres, xo and yo have the same dimension
    # ... and yo and yres have the same orientation
    # building area
    r=6370*1000
    pi = np.pi
    deg2rad=pi/180.
    deg2met=2*pi*r/360.
    ycenterbox=yo
    area=xres*yres*np.cos(ycenterbox*deg2rad)*deg2met*deg2met # area.shape => (128, 128) ; np.sum(area)/1E6/1E6 => 509.9 Mkm2
    return np.transpose(area)#, yo
