from typing import Any

from mcp_server.models.user_info import UserUpdate
from mcp_server.tools.users.base import BaseUserServiceTool


class UpdateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        #TODO: Provide tool name as `update_user`
        return "update_user"

    @property
    def description(self) -> str:
        #TODO: Provide description of this tool
        return "Tool for updating an existing user's information in the system by user ID. It accepts the user's ID and the new information as input and returns the updated user's details."

    @property
    def input_schema(self) -> dict[str, Any]:
        #TODO:
        # Provide tool params Schema:
        # - id: number, required, User ID that should be updated.
        # - new_info: UserUpdate.model_json_schema()
        return {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "new_info": UserUpdate.model_json_schema()
            },
            "required": ["id", "new_info"]  
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        #TODO:
        # 1. Get user `id` from `arguments`
        # 2. Get `new_info` from `arguments` and create `UserUpdate` via pydentic `UserUpdate.model_validate`
        # 3. Call user_client update_user and return its results (it is async, don't forget to await)
        user_id = arguments.get("id")
        if user_id is None: 
            raise ValueError("Missing required parameter: id")
        
        new_info_data = arguments.get("new_info")
        if new_info_data is None:
            raise ValueError("Missing required parameter: new_info")
        
        new_info = UserUpdate.model_validate(new_info_data)
        updated_user = await self._user_client.update_user(user_id, new_info)
        return updated_user

