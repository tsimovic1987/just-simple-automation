from dataclasses import dataclass, field
from typing import List, ClassVar

# first py.file with everything on english

@dataclass
class ScaleModels:

    # pool for instances from the class..!

    all_scales: ClassVar[List["Scale"]] = []

    serialid: str
    model: str
    # ...
    # ..
    # .

    meta_data: dict = field(default_factory=dict)

    def __post_init__(self):
        # every scale initialize himself to the ClassVar List (tryout, not final solution)
        ScaleModels.all_scales.append(self)