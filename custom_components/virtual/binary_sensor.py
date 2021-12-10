"""Implementation of entity: virtual binary sensor."""
from __future__ import annotations

import logging

import voluptuous as vol

from homeassistant.components.binary_sensor import (
    DEVICE_CLASSES_SCHEMA,
    BinarySensorEntity,
)
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
    """Virtual binary sensor setup."""
    async_add_entities([VirtualBinarySensor(hass, config)], True)


class VirtualBinarySensor(BaseEntity, BinarySensorEntity):
    """An implementation of a Virtual Binary Sensor."""

    _entity_type: str = "binary_sensor"

    def set_value(self, value: str):
        """Set of binary sensor value."""
        self._attr_is_on = value == STATE_ON
