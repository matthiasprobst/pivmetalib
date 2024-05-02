import datetime
import unittest

import h5rdmtoolbox as h5tbx
from h5rdmtoolbox import Attribute


class TestTimeDate(unittest.TestCase):

    def test_time_date(self):
        abs_time = [datetime.datetime.now() + datetime.timedelta(minutes=i) for i in range(10)]
        print(abs_time)

        print(abs_time[0].strftime('YYYY-MM-DDTHH:MM:SS.ffffff'))

        with h5tbx.File() as h5:
            ds = h5.create_time_dataset('time', data=abs_time)
            ds.rdf.subject = 'https://schema.org/DateTime'
            ds.attrs['timeformat'] = Attribute(value='YYYY-MM-DDTHH:MM:SS.ffffff',
                                               rdf_predicate='https://matthiasprobst.github.io/pivmeta#timeFormat')
            print(h5['time'][()])
