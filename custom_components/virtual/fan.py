"""Implementation of entity: virtual fan."""
from __future__ import annotations

import logging

from homeassistant.components.fan import FanEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .base_entity import BASE_SCHEMA, BaseEntity

_LOGGER = logging.getLogger(__name__)


PLATFORM_SCHEMA = BASE_SCHEMA.extend({})


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
):
    """Virtual fan setup."""
    async_add_entities([VirtualFan(hass, config)], True)


class VirtualFan(BaseEntity, FanEntity):
    """An implementation of a Virtual Fan."""

    _entity_type: str = "fan"

    def set_value(self, value: str):
        """Set of sensor value."""
        self._attr_native_value = value
