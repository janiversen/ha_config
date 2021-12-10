"""Base implementation for all virtual platforms/entities."""
from __future__ import annotations

from abc import abstractmethod
import logging

import voluptuous as vol

from homeassistant.components.sensor import CONF_STATE_CLASS
from homeassistant.const import (
    ATTR_ENTITY_ID,
    CONF_DEVICE_CLASS,
    CONF_NAME,
    CONF_UNIT_OF_MEASUREMENT,
)
from homeassistant.core import HomeAssistant, ServiceCall
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "virtual"
CONF_AVAILABLE = "available"
CONF_VALUE = "value"
SERVICE_SET = "set"


BASE_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_NAME): cv.string,
        vol.Optional(CONF_VALUE): cv.string,
        vol.Optional(CONF_AVAILABLE, default=True): cv.boolean,
    }
)

SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required(ATTR_ENTITY_ID): cv.comp_entity_ids,
        vol.Required(CONF_VALUE): cv.string,
        vol.Optional(CONF_AVAILABLE, default=True): cv.boolean,
    }
)


async def async_base_setup(hass: HomeAssistant) -> bool:
    """Foundation setup for entities."""

    async def async_virtual_service(service: ServiceCall):
        """Call to set value and optional availability."""
        for entity_id in service.data[ATTR_ENTITY_ID]:
            value = service.data[CONF_VALUE]
            available = service.data[CONF_AVAILABLE]
            entity = hass.data[DOMAIN][entity_id]
            await entity.async_virtual_set(value, available)

    hass.services.async_register(
        DOMAIN,
        SERVICE_SET,
        async_virtual_service,
        schema=SERVICE_SCHEMA,
    )
    return True


class BaseEntity(Entity):
    """Base for all entities."""

    _entity_type: str

    def __init__(self, hass: HomeAssistant, entry: ConfigType) -> None:
        """Initialize the universal entity."""
        self._attr_name = entry[CONF_NAME]
        entity_id = f"{self._entity_type}.{entry[CONF_NAME].lower()}"
        hass.data[DOMAIN][entity_id] = self
        self._attr_should_poll = False
        self._attr_device_class = entry.get(CONF_DEVICE_CLASS)
        self._attr_state_class = entry.get(CONF_STATE_CLASS)
        self._attr_native_unit_of_measurement = entry.get(CONF_UNIT_OF_MEASUREMENT)
        self._attr_available = entry[CONF_AVAILABLE]
        if CONF_VALUE in entry:
            self.set_value(entry[CONF_VALUE])
        self._attr_unique_id = f"virtual-{entity_id}"

    async def async_base_added_to_hass(self) -> None:
        """Handle entity which are added."""

    @abstractmethod
    def set_value(self, value: str):
        """Set of entity state/value, depending on type of entity."""

    async def async_virtual_set(self, value: str, available: bool):
        """Manually set value/available and update entity."""
        self.set_value(value)
        self._attr_available = available
        self.async_write_ha_state()
