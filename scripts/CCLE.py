import argparse
import pandas as pd

class CCLE_Info(object):
    def __init__(self, ccle_meta_file):
        self.fp = ccle_meta_file
        self.df = pd.read_csv(ccle_meta_file, header=0)
        self.broad_ids = list(self.df['DepMap_ID'])
        self.ccle_names = list(self.df['CCLE_Name'])
        self._broad2ccle = dict(zip(self.broad_ids, self.ccle_names))
        self._ccle2broad = dict(zip(self.ccle_names, self.broad_ids))

    def broad_id_2_ccle_name(self, broad_id):
        '''
        Convert Broad ID to CCLE name
        '''
        return self._broad2ccle[broad_id]

    def ccle_name_2_broad_id(self, ccle_name):
        '''
        Convert CCLE name to  Broad ID
        '''
        return self._ccle2broad[ccle_name]
    
    def get_ccle_name_info(self, ccle_name):
        '''
        Return dictionary of info given ccle_name
        '''
        raise NotImplementedError
    
    def get_broad_id_name_info(self, broad_id):
        '''
        Return dictionary of info given ccle_name
        '''
        raise NotImplementedError
        