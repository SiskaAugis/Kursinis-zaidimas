# sun.py (Corrected)

from panda3d.core import DirectionalLight
from ursina import Entity
import sys
import os

class SunLight(Entity):
    # Added **kwargs here (which you did correctly)
    def __init__(self, direction, resolution, car, **kwargs):
        # --- FIX: Pass **kwargs to super().__init__ ---
        super().__init__(**kwargs)
        # ---------------------------------------------

        self.car = car
        self.resolution = resolution

        self.dlight = DirectionalLight("sun")

        # Basic validation for resolution
        if isinstance(resolution, int) and resolution > 0:
            self.dlight.setShadowCaster(True, self.resolution, self.resolution)
            lens = self.dlight.getLens()
            lens.setNearFar(-80, 200)
            lens.setFilmSize((100, 100))
        else:
            print(f"Warning: Invalid SunLight shadow resolution: {resolution}. Disabling shadows.")
            self.dlight.setShadowCaster(False, 1, 1) # Disable shadows if resolution is bad

        self.dlnp = render.attachNewNode(self.dlight)
        self.dlnp.lookAt(direction)
        render.setLight(self.dlnp)
        print("SunLight Initialized.") # Confirmation print


    def update(self):
        # Check if self.car and its attribute exist before accessing
        if hasattr(self, 'car') and self.car and hasattr(self.car, 'world_position'):
            self.dlnp.setPos(self.car.world_position)
        elif hasattr(self, 'car') and self.car: # Fallback if world_position doesn't exist
             self.dlnp.setPos(self.car.position)


    def update_resolution(self):
        # Basic validation for resolution
        if isinstance(self.resolution, int) and self.resolution > 0:
            print(f"Updating SunLight shadow resolution to: {self.resolution}")
            self.dlight.setShadowCaster(True, self.resolution, self.resolution)
        else:
            print(f"Warning: Invalid SunLight shadow resolution: {self.resolution}. Disabling shadows.")
            self.dlight.setShadowCaster(False, 1, 1) # Disable shadows