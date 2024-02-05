REGISTRY = {}

from .coordinate import Coordinate
REGISTRY["coordinate"] = Coordinate

from .onehot import Onehot
REGISTRY["onehot"] = Onehot

from .onehot_fov import OnehotFov
REGISTRY["onehot_fov"] = OnehotFov

from .heu_onehot import HeuOnehot
REGISTRY["heu_onehot"] = HeuOnehot

from .heu_onehot_fov import HeuOnehotFov
REGISTRY["heu_onehot_fov"] = HeuOnehotFov