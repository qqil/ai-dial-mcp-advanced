from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class GetUserByIdTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        #TODO: Provide tool name as `get_user_by_id`
        return "get_user_by_id"

    @property
    def description(self) -> str:
        #TODO: Provide description of this tool
        return "Tool for retrieving user information by their ID. It accepts the user's ID as input and returns the corresponding user's details."

    @property
    def input_schema(self) -> dict[str, Any]:
        #TODO:
        # Provide tool params Schema. This tool applies user `id` (number) as a parameter and it is required
        return {
            "type": "object",
            "properties": {
                "id": {"type": "number"}
            },
            "required": ["id"]
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        #TODO:
        # 1. Get int `id` from arguments
        # 2. Call user_client get_user and return its results (it is async, don't forget to await)
        user_id = arguments.get("id")
        if user_id is None:
            raise ValueError("Missing required parameter: id")
        user_info = await self._user_client.get_user(user_id)
        return user_info