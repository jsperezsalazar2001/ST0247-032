import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from bokeh.plotting import *
from bokeh.models import *
from bokeh.tile_providers import *
import pandas as pd
import bokeh
from sklearn.preprocessing import MinMaxScaler


class DrawerTEST:
    """
    This class is a helper to visualize the nodes and their paths in a map
    :author Juan Sebastian Perez Salazar
    :author Yhoan Alejandro Guzman Garcia
    """
    
    def latlng_to_meters(self, lat, lng):
        """
        This method converts from coordinates between an origin to a point to meters
        :param lat: latitudinal position
        :param lng: longitudinal position
        :return: meters in each axis
        """
        origin_shift = 2 * np.pi * 6378137 / 2.0
        mx = lng * origin_shift
        mx = mx / 180.0
        my = np.log(np.tan((90. + lat) * np.pi / 360.0)) / (np.pi / 180.0)
        my = my * origin_shift / 180.0
        return mx, my
    
    def plot_map(self, lat, lon, ids, mode, center, color=None, size=10):
        """
        This method draws a map with points in the given coordinates
        :param lat: Pandas Series of latitudes
        :param lon: Pandas Series of longitudes
        :param center: origin coordinates
        :param color: Numpy Array of distances between an origin an each given latitude and longitude reshaped from -1 to 1
        :param size: size of the point in the map
        :return: None
        """
        cmap = cm.rainbow 
        wlat0, wlong0 = self.latlng_to_meters(center[0], center[1])
        w2lat = pd.Series([])
        w2long = pd.Series([])
        startLatPoints = []
        startLonPoints = []
        endLatPoints = []
        endLonPoints = []
        tools="pan,wheel_zoom,reset"
        p = figure(tools=tools, plot_width=1200,plot_height=850, x_axis_type="mercator", y_axis_type="mercator")
        for i in range(len(lat)):
            if lat[i] == 0.0 and lon[i] == 0.0:
                continue
            else:
                wlat, wlong = self.latlng_to_meters(lat[i], lon[i])
                x = [wlat]
                y = [wlong]
                w2lat = w2lat.append(pd.Series(x))
                w2long = w2long.append(pd.Series(y))
                startLatPoints.append(wlat)
                startLonPoints.append(wlong)
                if  i+1 == len(lat) :
                    endLatPoints.append(wlat0)
                    endLonPoints.append(wlong0)
                elif lat[i+1] == 0.0 and lon[i+1] == 0.0:
                    endLatPoints.append(wlat0)
                    endLonPoints.append(wlong0)
                else:
                    wlatEnd, wlongEnd = self.latlng_to_meters(lat[i+1], lon[i+1])
                    endLatPoints.append(wlatEnd)
                    endLonPoints.append(wlongEnd)              
        if color is not None:
            colors = MinMaxScaler(feature_range=(0,255)).fit_transform(color)
            colors = ["#%02x%02x%02x"%tuple([int(j*255) for j in cmap(int(i))[:3]]) for i in colors]
        

        w2lat = np.append(w2lat, wlat0)
        w2long = np.append(w2long, wlong0)
        openmap_url = 'http://c.tile.openstreetmap.org/{Z}/{X}/{Y}.png'
        otile_url = 'http://otile1.mqcdn.com/tiles/1.0.0/sat/{Z}/{X}/{Y}.jpg'
        TILES = WMTSTileSource(url=openmap_url)
        p.circle(np.array(w2lat), np.array(w2long), color=colors, size=size, alpha = 0.5)

        if mode == 2 or mode == 3:
            p.segment(np.array(startLatPoints), np.array(startLonPoints), np.array(endLatPoints), np.array(endLonPoints), color="#902cdd", line_width=3, alpha = 0.8)

        startLatPoints.append(wlat0)
        startLonPoints.append(wlong0)
        if mode == 3:
            p.text(np.array(startLatPoints), np.array(startLonPoints),text = ids, angle = 0,x_offset= 0,y_offset=0, text_font_size = '12pt', text_font_style = 'bold')
        p.add_tile(TILES)
        p.axis.visible = False
        cb = figure(plot_width=130, plot_height=600,  tools=tools)
        yc = np.linspace(np.min(color),np.max(color),20)
        c = np.linspace(0,255,20).astype(int)
        dy = yc[1]-yc[0]    
        cb.rect(x=0.5, y=yc, color=["#%02x%02x%02x"%tuple([int(j*255) for j in cmap(int(i))[:3]]) for i in c], width=1, height = dy)
        cb.xaxis.visible = False
        pb = gridplot([[p, cb]])
        show(pb)

