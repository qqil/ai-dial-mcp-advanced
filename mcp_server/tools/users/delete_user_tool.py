from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class DeleteUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        #TODO: Provide tool name as `delete_users`
        return "delete_user"

    @property
    def description(self) -> str:
        #TODO: Provide description of this tool
        return "Tool for deleting a user from the system. It accepts the user's ID as input and returns a confirmation of deletion."

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
        # 2. Call user_client delete_user and return its results (it is async, don't forget to await)
        user_id = arguments.get("id")
        if user_id is None:
            raise ValueError("Missing required parameter: id")
        deletion_result = await self._user_client.delete_user(user_id)
        return deletion_result