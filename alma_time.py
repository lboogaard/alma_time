import os
import numpy as np
from astropy.table import Table

datapath = os.path.dirname(os.path.abspath(__file__))
datadir = os.path.join(datapath, './time_config-C13/')

def time_available(lst_start=0, lst_end=24,
                   configs=['ACA', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10'],
                   bands=['Total','LP','Band 8','Band 9/10'],
                   datadir = datadir):
    """
    Prints total time available for an LST range and configuration in ACA and ALMA bands

    Total time from LST = 0 to 6 in configurations C1 through C4:

        time_available(0, 6, ['C1', 'C2', 'C3', 'C4'])
    
    Parameters
    ----------
    lst_start, lst_end: int
        start and end of LST range in hours
    config: list
        list of configurations to consider (if ACA in list will NOT be summed to total)
    bands: list
        bands to print (default: all)
    datadir: str

    
    Author: Leindert Boogaard
    Version: 12/04/2024
        
    """
    grand_total = 0
    grand_total_aca = 0
    for band in bands:
        total = 0
        for config in configs:
            data = Table.read(os.path.join(datadir, config+'.txt'), format="ascii", delimiter=',', names=['LST','Total','LP','Band 8','Band 9/10'])
            # print(data[lst_range[0]:lst_range[1]+1])  # check lst ranges selected
            inconfig = np.round(np.sum(data[band][lst_start:lst_end+1]),1)
            print(band, config, inconfig, 'h')
            if config == 'ACA':
                grand_total_aca += inconfig
            else:
                total += inconfig
        grand_total += total
        
        print(band, 'total (excl. ACA)', np.round(total,1), 'h\n')
    print('All bands total (excl. ACA)', np.round(grand_total,1), 'h')
    print('All bands total ACA', np.round(grand_total_aca, 1), 'h\n')    


