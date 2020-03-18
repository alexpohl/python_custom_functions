#!/usr/bin/env python

def stepped_coastline(lon_data, lat_data, topo_bathy_file, lwidth):
    # land outline... the hard part
    # for each point of the cropped area, determine if it is a coastal point and plot (or not) accordingly
    land_outline_linewidth = lwidth
    reslon = lon_data[1]-lon_data[0]
    reslat = lat_data[1]-lat_data[0]
    landseamask = np.ma.masked_where(topo_bathy_file < 0,topo_bathy_file)
    lonrange = np.arange(0,topo_bathy_file.shape[1]-1)
    for ilon in lonrange:
        for ilat in np.arange(0,topo_bathy_file.shape[0]-1):
            # is there an ocean to the East or to the West?
            if (landseamask.mask[ilat,ilon] != landseamask.mask[ilat,ilon+1]):
                    lat1 = lat_data[ilat]
                    lat2 = lat_data[ilat+1]
                    lon1 = lon_data[ilon]+reslon
                    lon2 = lon_data[ilon]+reslon
                    latpts = [lat1, lat2]; #print latpts
                    lonpts = [lon1, lon2]; #print lonpts
                    plt.plot(lonpts,latpts,'-',linewidth=land_outline_linewidth, color='k',zorder=40,transform=ccrs.PlateCarree())
            # is there an ocean to the North or to the South?
            if (landseamask.mask[ilat,ilon] != landseamask.mask[ilat+1,ilon]):
                    lat1 = lat_data[ilat]+reslat
                    lat2 = lat_data[ilat]+reslat
                    lon1 = lon_data[ilon]
                    lon2 = lon_data[ilon+1]
                    latpts = [lat1, lat2]; #print latpts
                    lonpts = [lon1, lon2]; #print lonpts
                    plt.plot(lonpts,latpts,'-',linewidth=land_outline_linewidth, color='k',zorder=40,transform=ccrs.PlateCarree())
    # deadling with the modulo
    for ilat in np.arange(0,topo_bathy_file.shape[0]-1):
        # is there an ocean to the East or to the West?
        if ((landseamask.mask[ilat,0] == True) != (landseamask.mask[ilat,-1])):
                lat1 = lat_data[ilat]
                lat2 = lat_data[ilat+1]
                lon1 = lon_data[0]
                lon2 = lon_data[0]
                latpts = [lat1, lat2]; #print latpts
                lonpts = [lon1, lon2]; #print lonpts
                plt.plot(lonpts,latpts,'-',linewidth=land_outline_linewidth, color='k',zorder=40,transform=ccrs.PlateCarree())
        # is there an ocean to the North or to the South?
        if (landseamask.mask[ilat,-1] != landseamask.mask[ilat+1,-1]):
                lat1 = lat_data[ilat]+reslat
                lat2 = lat_data[ilat]+reslat
                lon1 = (lon_data[-2]+lon_data[-1])/2.
                lon2 = lon_data[-1]
                latpts = [lat1, lat2]; #print latpts
                lonpts = [lon1, lon2]; #print lonpts
                plt.plot(lonpts,latpts,'-',linewidth=land_outline_linewidth, color='k',zorder=40,transform=ccrs.PlateCarree())
