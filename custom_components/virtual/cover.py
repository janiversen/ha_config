"""Implementation of entity: virtual cover."""
from __future__ import annotations

import logging

import voluptuous as vol

from homeassistant.components.cover import DEVICE_CLASSES_SCHEMA, CoverEntity
from homeassistant.const import CONF_DEVICE_CLASS, STATE_ON
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .base_entity import BASE_SCHEMA, BaseEntity

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = BASE_SCHEMA.extend(
    {
        vol.Optional(CONF_DEVICE_CLASS): DEVICE_CLASSES_SCHEMA,
    }
)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
):
    """Virtual cover setup."""
    async_add_entities([VirtualCover(hass, config)], True)


class VirtualCover(BaseEntity, CoverEntity):
    """An implementation of a Virtual Cover."""

    _entity_type: str = "cover"

    def __init__(self, hass: HomeAssistant, entry: ConfigType) -> None:
        """Initialize the cover entity."""
        self._attr_is_closed: bool = False

    def set_value(self, value: str):
        """Set of cover value."""
        self._attr_is_closed = value == STATE_ON
