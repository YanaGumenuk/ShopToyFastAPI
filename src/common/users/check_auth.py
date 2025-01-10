from typing import Annotated
from fastapi import Depends, HTTPException, status

from src.common.users.authentication import get_current_active_user
from src.services.database.models.users.user import UserRole, User


class RoleChecker:
    def __init__(self, target_role: UserRole):
        self.target_role = target_role

    def __call__(self, current_user: Annotated[User, Depends(get_current_active_user)]):
        if current_user.role < self.target_role:
            raise HTTPException(
                status_code=403,
                detail="No access")
        return User