import dataclasses

from core.data.Enums import Work_status


@dataclasses.dataclass(init=True, frozen=True)
class MyProfile:
    position_name: str  # i.e. title of the resume
    desired_payment: int
    workstatus: Work_status
