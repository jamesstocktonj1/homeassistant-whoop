
from typing import Any, Dict, Optional
import voluptuous as vol

from homeassistant import core, config_entries

from .const import (
    CONF_ACCESS_TOKEN, 
    DOMAIN
)


AUTH_SCHEMA = vol.Schema(
    {vol.Required(CONF_ACCESS_TOKEN): str}
)

class WhoopCustomConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    data: Optional[Dict[str, Any]]

    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None):
        errors: Dict[str, str] = {}
        self.data = user_input


        return self.async_show_form(step_id="user", data_schema=AUTH_SCHEMA, errors=errors)