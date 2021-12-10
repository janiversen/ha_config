"""Implementation of entity: virtual light."""
from __future__ import annotations

import logging

from homeassistant.components.light import LightEntity
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
    """Virtual light setup."""
    async_add_entities([VirtualLight(hass, config)], True)


class VirtualLight(BaseEntity, LightEntity):
    """An implementation of a Virtual light."""

    _entity_type: str = "light"

    def is_on(self) -> bool:
        """Return if the lights are on based on the statemachine."""
        return self._attr_native_value == STATE_ON

    def set_value(self, value: str):
        """Set of sensor value."""
        self._attr_native_value = value
