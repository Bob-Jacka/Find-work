import dataclasses

from core.data.enums import Work_status


@dataclasses.dataclass(init=True, frozen=True)
class MyProfile:
    position_name: str
    workstatus: Work_status
