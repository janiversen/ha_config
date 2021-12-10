"""Implementation of entity: virtual switch."""
from __future__ import annotations

import logging

from homeassistant.components.switch import SwitchEntity
from homeassistant.const import STATE_ON
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
    """Virtual switch setup."""
    async_add_entities([VirtualSwitch(hass, config)], True)


class VirtualSwitch(BaseEntity, SwitchEntity):
    """An implementation of a Virtual switch."""

    _entity_type: str = "switch"

    def set_value(self, value: str):
        """Set of switch value."""
        self._attr_native_value = value == STATE_ON

    def is_on(self) -> bool:
        """Return switch value."""
        return self._attr_native_value
