import pandas as pd
# from qso_toolbox import catalog_tools as ct
import catalog_tools as ct # temp means special requirements in notes 1/2
import argparse

parser = argparse.ArgumentParser()
                                 
# Add an argument for the 'ra' variant
parser.add_argument('-ra_name', type=str, help='name of the RA column in the file')
parser.add_argument('-dec_name', type=str, help='name of the dec column in the file')
parser.add_argument('-source_name', type=str, help='name of the Source Name column in the file')
parser.add_argument('-img_path', type=str, help='img saving path')
parser.add_argument('-csv_path', type=str, help='csv file path')

# Parse the command-line arguments
args = parser.parse_args()

# Access the value of the 'ra' variant
ra_name = args.ra_name
dec_name = args.dec_name
source_name = args.source_name
img_path = args.img_path
csv_path = args.csv_path
    
# Input File (only csv here)
# Input File (only csv here)
catalog_filename = csv_path

# Image path to save
image_path = img_path
# Coordinate column names, either string or list of strings with length N
ra_column_name = ra_name
dec_column_name = dec_name
object_column_name=source_name # if no obj name provided, set it to None
# object_column_name = 'name_short' # user provided names
# List of surveys, list with length N
# surveys = ['ps1', 'ps1', 'ps1', 'ps1', 'ps1', \
#     'skymapper', 'skymapper', 'skymapper','skymapper',
#            'unwise-neo6', 'unwise-neo6', 'vhsdr6', 'vhsdr6', 'vhsdr6', 'vhsdr6', 'vhsdr6', \
#                'vikingdr5', 'vikingdr5', 'vikingdr5', 'vikingdr5', 'vikingdr5', 'vlass', 'decals']

# surveys = ['ps1', 'ps1', 'ps1', 'ps1', 'ps1', \
#     'skymapper', 'skymapper', 'skymapper','skymapper',
#             'unwise-neo6', 'unwise-neo6', 'vhsdr6', 'vhsdr6', 'vhsdr6', 'vhsdr6', 'vhsdr6', \
#                 'vikingdr5', 'vikingdr5', 'vikingdr5', 'vikingdr5', 'vikingdr5']

# bands = ['g','r','i','z','y','g','r','i','z','w1','w2', 'Z', 'Y', 'J', 'H', 'Ks', 'Z', 'Y', 'J', 'H', 'Ks']

surveys=['vlass']

bands=['3GHz']
            # Possible survey names include: desdr1, ps1, decals, vhsdr6, vikingdr5,unwise-allwise, unwise-neo1, unwise-neo2, unwise-neo3, unwise-neo4, unwise-neo5, unwise-neo6
# List of survey bands, list with length N

# List of field of views for downloading the images
fovs = [120]*len(bands)

#------------------------------------------------------------------------------
# INPUT Keyword Arguments
#------------------------------------------------------------------------------

# List of psf sizes, either None, float or list with length N
psf_size = None
# List of aperture sizes, either None (automatic) or list with length N
apertures = None


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# table = pd.read_hdf(catalog_filename)
table = pd.read_csv(catalog_filename)

# # table.query('340 < mq_ra < 350 and -1.26 < mq_dec < 0', inplace=True)

# Currently only the normal get_photometry function works for VLASS and
# skymapper. The multiprocessing function needs to be updated before it can
# be used.
ct.get_photometry(table[:], ra_column_name, dec_column_name, object_column_name, surveys,
                     bands, image_path, fovs, verbosity=2) # object names is user provided names


# table[:n].to_hdf('temp.hdf5', 'data')

# catalog_filename = 'temp.hdf5'

# # Run a simple example
# imview.run(catalog_filename, image_path, ra_column_name,
#                  dec_column_name, surveys, bands, verbosity=2)