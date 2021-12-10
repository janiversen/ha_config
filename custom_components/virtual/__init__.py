"""Integration: virtual."""

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .base_entity import DOMAIN, async_base_setup


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up integration."""

    hass.data.setdefault(DOMAIN, {})

    return await async_base_setup(hass)
