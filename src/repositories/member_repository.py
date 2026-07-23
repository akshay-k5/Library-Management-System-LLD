from abc import ABC, abstractmethod
from typing import Optional, List
from ..models.member import Member

class MemberRepositoryInterface(ABC):
    @abstractmethod
    def add(self, member: Member) -> None:
        pass

    @abstractmethod
    def get_by_id(self, member_id: str) -> Optional[Member]:
        pass

    @abstractmethod
    def get_all(self) -> List[Member]:
        pass

class InMemoryMemberRepository(MemberRepositoryInterface):
    def __init__(self):
        self._members = {}

    def add(self, member: Member) -> None:
        if member.id in self._members:
            raise ValueError(f"Member with ID {member.id} already exists.")
        self._members[member.id] = member

    def get_by_id(self, member_id: str) -> Optional[Member]:
        return self._members.get(member_id)

    def get_all(self) -> List[Member]:
        return list(self._members.values())