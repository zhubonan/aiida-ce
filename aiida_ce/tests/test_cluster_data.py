from aiida.manage.tests.unittest_classes import PluginTestCase

from aiida.plugins import DataFactory

from ase.build import bulk

ClusterSpaceData = DataFactory('ce.cluster')

class TestClusterSpaceData(PluginTestCase):

    def setUp(self):
        prim = bulk('Au')
        cs_dict = {
            'cell': prim.cell.tolist(),
            'positions': prim.positions.tolist(),
            'pbc':prim.pbc.tolist(),
            'cutoffs': [6.0, 4.0],
            'chemical_symbols': [['Au', 'Pd']]
        }
        self.cs = ClusterSpaceData(cs_dict)

    def test_properties(self):
        pass
