
#%%
#Importing the necessary packages

import osmnet

# Transit graph = pedestrian + transit
# Biking graph  = Walking graph = predestrian
# Driving graph = driving

import matplotlib
matplotlib.use('agg')  # allows notebook to be tested in Travis

import pandas as pd

import matplotlib.pyplot as plt
import time

import urbanaccess as ua
from urbanaccess.config import settings
from urbanaccess.gtfsfeeds import feeds
from urbanaccess import gtfsfeeds
from urbanaccess.gtfs.gtfsfeeds_dataframe import gtfsfeeds_dfs
from urbanaccess.network import ua_network, load_network

# %%
# Create a driving network
def store_driving_network(bbox):
    # Download network
    nodes, edges = osmnet.load.network_from_bbox(bbox=bbox, network_type='drive')
    # Create a network object
    ua.osm.network.create_osm_net(osm_edges=edges,
                                osm_nodes=nodes,
                                travel_speed_mph=3)

    # The UrbanAccess network object
    urbanaccess_net = ua.network.ua_network

    urbanaccess_net.net_nodes = urbanaccess_net.osm_nodes
    urbanaccess_net.net_edges = urbanaccess_net.osm_edges

    # Save the network to disk
    filename = 'driving_net.h5'

    ua.network.save_network(urbanaccess_network=urbanaccess_net,
                            filename=filename,
                            overwrite_key = True)

# bbox for Blockgroups selected in sample - recalculate for new sample!
# make sure to change in transit network too
bbox = (-71.13, 42.345, -71.04, 42.394)

# Order is important here - the driving osm data overrides the walking data used in the transit network
store_driving_network(bbox)
# %%
