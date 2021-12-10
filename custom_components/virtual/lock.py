"""Implementation of entity: virtual lock."""
from __future__ import annotations

import logging

from homeassistant.components.lock import LockEntity
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
    """Virtual lock setup."""
    async_add_entities([VirtualLock(hass, config)], True)


class VirtualLock(BaseEntity, LockEntity):
    """An implementation of a Virtual lock."""

    _entity_type: str = "lock"

    def set_value(self, value: str):
        """Set of lock value."""
        self._attr_is_on = value == STATE_ON
