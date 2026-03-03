from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool
from mcp_server.models.user_info import UserSearchRequest

class SearchUsersTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        #TODO: Provide tool name as `search_users`
        return "search_users"

    @property
    def description(self) -> str:
        #TODO: Provide description of this tool
        return "Tool for searching users in the system based on various criteria. It accepts search parameters such as name, surname, email, and gender, and returns a list of users that match the provided criteria."

    @property
    def input_schema(self) -> dict[str, Any]:
        #TODO:
        # Provide tool params Schema:
        # - name: str
        # - surname: str
        # - email: str
        # - gender: str
        # None of them are required (see UserClient.search_users method)
        return UserSearchRequest.model_json_schema()

    async def execute(self, arguments: dict[str, Any]) -> str:
        #TODO:
        # Call user_client search_users (with `**arguments`) and return its results (it is async, don't forget to await)
        search_request = UserSearchRequest.model_validate(arguments)
        search_results = await self._user_client.search_users(**search_request.model_dump())
        return search_results