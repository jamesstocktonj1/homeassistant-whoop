from __future__ import annotations

from typing import Any
import aiohttp

from homeassistant import core, config_entries
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.typing import DiscoveryInfoType

from .const import DOMAIN

async def async_setup_entry(hass: core.HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities) -> None:
    config = hass.data[DOMAIN][config_entry.entry_id]
    if config_entry.options:
        config.update(config_entry.options)
    session = async_get_clientsession(hass)
    sensors = WhoopSensor(session, config)
    async_add_entities([sensors], update_before_add=True)

async def async_setup_platform(hass: core.HomeAssistant, config: dict, async_add_entities, discovery_info: DiscoveryInfoType | None=None) -> None:
    session = async_get_clientsession(hass)
    sensors = WhoopSensor(session, config)
    async_add_entities([sensors], update_before_add=True)


class WhoopSensor(Entity):

    def __init__(self, session: aiohttp.ClientSession, config: dict[str, str]):
        super().__init__()
        self.session = session
        self.attrs: dict[str, Any] = {"state": 0}
        self._name = "Whoop"
        self._state = None
        self._available = True

    @property
    def name(self) -> str:
        """Return the name of the entity."""
        return self._name
    
    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return "whoop_sensor"
    
    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._available

    @property
    def state(self) -> str | None:
        return self._state
    
    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        return self.attrs
    
    async def async_update(self) -> None:
        self.attrs["state"] += 1
            