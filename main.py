
from ursina import *
import sys
import time
from abc import ABC, abstractmethod
import os

try:
    from masinos import Car
    from ai import AICar
    from sun import SunLight
except ImportError as e:
    print(f"FATAL ERROR: Could not import entity classes (Car, AICar, SunLight). Check files exist. Error: {e}")
    sys.exit()

try:
    from meniu import MainMenu
    from achievements import RallyAchievements
except ImportError as e:
    print(f"FATAL ERROR: Could not import game logic classes (MainMenu, RallyAchievements). Check files exist. Error: {e}")
    sys.exit()


try:
    from tracks.sand_track import SandTrack
    from tracks.grass_track import GrassTrack
    from tracks.snow_track import SnowTrack
    from tracks.forest_track import ForestTrack
    from tracks.savannah_track import SavannahTrack
    from tracks.lake_track import LakeTrack
except ImportError as e:
    print(f"FATAL ERROR: Could not import track classes. Make sure the 'tracks' folder exists and contains the necessary .py files. Error: {e}")
    sys.exit()



# ==============================================================
# === Helper Class Definitions =================================
# ==============================================================

class Assets:
    """
    Handles loading and caching of game assets (models and textures).
    """
    def __init__(self):
        """Initializes the lists of assets to load."""
        self.asset_folder = Path("./assets/")
        print(f"Asset folder path determined as: {self.asset_folder.resolve()}")

        self.models_to_load = [
            
            "sports-car.obj", "muscle-car.obj", "limousine.obj",
            "lorry.obj", "hatchback.obj", "rally-car.obj",
            
            "sand_track.obj", "grass_track.obj", "snow_track.obj",
            "forest_track.obj", "savannah_track.obj",
            "lake_track.obj", "particles.obj",
            
            "sand_track_bounds.obj", "grass_track_bounds.obj",
            "snow_track_bounds.obj",
            "forest_track_bounds.obj", "savannah_track_bounds.obj",
            "lake_track_bounds.obj",
            
            "rocks-sand.obj", "cacti-sand.obj", "trees-grass.obj",
            "thintrees-grass.obj", "rocks-grass.obj",
            "grass-grass_track.obj", "trees-snow.obj",
            "thintrees-snow.obj", "rocks-snow.obj", "trees-forest.obj",
            "thintrees-forest.obj", "rocks-savannah.obj",
            "trees-savannah.obj",
            "trees-lake.obj", "thintrees-lake.obj", "rocks-lake.obj",
            "bigrocks-lake.obj", "grass-lake.obj", "lake_bounds.obj",
            
            "viking_helmet.obj", "duck.obj", "banana.obj",
            "surfinbird.obj", "surfboard.obj",
        ]
        self.textures_to_load = [
            "sports-red.png", "sports-orange.png", "sports-green.png",
            "sports-white.png", "sports-black.png", "sports-blue.png",
            "muscle-red.png", "muscle-orange.png", "muscle-green.png",
            "muscle-white.png", "muscle-black.png", "muscle-blue.png",
            "limo-red.png", "limo-orange.png", "limo-green.png",
            "limo-white.png", "limo-black.png", "limo-blue.png",
            "lorry-red.png", "lorry-orange.png", "lorry-green.png",
            "lorry-white.png", "lorry-black.png", "lorry-blue.png",
            "hatchback-red.png", "hatchback-orange.png",
            "hatchback-green.png", "hatchback-white.png",
            "hatchback-black.png", "hatchback-blue.png",
            "rally-red.png", "rally-orange.png", "rally-green.png",
            "rally-white.png", "rally-black.png", "rally-blue.png",
            "sand_track.png", "grass_track.png", "snow_track.png",
            "forest_track.png",
            "savannah_track.png", "lake_track.png",
            "rock-sand.png", "cactus-sand.png", "tree-grass.png",
            "thintree-grass.png", "rock-grass.png",
            "grass-grass_track.png", "tree-snow.png",
            "thintree-snow.png", "rock-snow.png", "tree-forest.png",
            "thintree-forest.png", "rock-savannah.png",
            "tree-savannah.png",
            "tree-lake.png", "rock-lake.png", "grass-lake.png",
            "thintree-lake.png", "bigrock-lake.png",
            "particle_sand_track.png", "particle_grass_track.png",
            "particle_snow_track.png",
            "particle_forest_track.png", "particle_savannah_track.png",
            "particle_lake_track.png",
            "viking_helmet.png", "duck.png", "banana.png",
            "surfinbird.png", "surfboard.png",
            "viking_helmet-icon.png", "duck-icon.png",
            "banana-icon.png", "surfinbird-icon.png", "surfboard-icon.png"
        ]
        print("Assets lists created.")

    def load(self):
        """Loads all models and textures specified in the lists."""
        print("\nLoading Assets...")
        loaded_models = 0
        loaded_textures = 0
        for model_name in self.models_to_load:
            try:
                load_model(model_name)
                loaded_models += 1
            except Exception as e:
                print(f"Warning: Could not load model '{model_name}'. Error: {e}")

        for texture_name in self.textures_to_load:
            try:
                load_texture(texture_name)
                loaded_textures += 1
            except Exception as e:
                print(f"Warning: Could not load texture '{texture_name}'. Error: {e}")
        print(f"Finished loading assets: {loaded_models} models, {loaded_textures} textures.")


class Lighting:
    """
    Manages the game's lighting (Sun and Ambient).
    """
    def __init__(self, car):
        """Initializes the lighting components."""
        print("\nSetting up Lighting...")
        self.sun = None
        self.ambient = None

        try:
            self.sun = SunLight(
                 parent=scene,
                 direction=(-0.7, -0.9, 0.5),
                 resolution=2048,
                 car=car
            )
        except Exception as e:
            print(f"ERROR: Failed to create SunLight. Error: {e}")

        try:
            self.ambient = AmbientLight(
                 parent=scene,
                 color=Vec4(0.5, 0.55, 0.66, 1) * 0.75
            )
        except Exception as e:
            print(f"ERROR: Failed to create AmbientLight. Error: {e}")

        render.setShaderAuto()
        print("Lighting setup complete.")


class BaseTrack(Entity, ABC):
    """
    Abstract Base Class for tracks.
    """
    def __init__(self, player_car, **kwargs):
        super().__init__(**kwargs)
        self.player_car = player_car
        self.played = False
        self.unlocked = False

    @abstractmethod
    def get_track_name(self) -> str:
        """Return the display name of the track."""
        pass

    @abstractmethod
    def setup_environment(self):
        """Set up track-specific environment details."""
        pass

    def display_info(self):
        """Prints basic info about the track."""
        try:
            print(f"Track Info: {self.get_track_name()}")
        except Exception:
            print(f"Track Info: {type(self).__name__} (get_track_name error)")

# ==============================================================
# === Main Game Class ==========================================
# ==============================================================

class Game:
    """
    Encapsulates the main game logic and manages game components.
    """
    def __init__(self):
        """Initializes the game application and its components."""
        try:
            self.app = Ursina()
        except Exception as e:
             print(f"FATAL: Failed to initialize Ursina App. Error: {e}")
             sys.exit()

        self.assets = Assets()
        self.assets.load()

        self.setup_window()

        try:
            self.car = Car(position=(0, 1, 0))
            self.car.sports_car()
            print("Actual Car object created from car.py")
        except Exception as e:
            print(f"ERROR: Failed to create Car object. Error: {e}")
            sys.exit()

        self.tracks = self.create_tracks()
        if not self.tracks:
             print("WARNING: No tracks were created successfully.")
        self._assign_tracks_to_car()

        try:
            self.ai_cars = self.create_ai_cars()
            print(f"Actual AICar objects created: {len(self.ai_cars)}")
        except Exception as e:
            print(f"ERROR: Failed to create AICar objects. Error: {e}")
            self.ai_cars = []

        # Create UI / Game Logic Components
        try:
            self.main_menu = MainMenu(self.car, self.ai_cars, *self.tracks)
        except Exception as e:
            print(f"ERROR: Failed to create MainMenu. Error: {e}")
            sys.exit()

        try:
            self.achievements = RallyAchievements(self.car, self.main_menu, *self.tracks)
        except Exception as e:
            print(f"ERROR: Failed to create RallyAchievements. Error: {e}")
            self.achievements = None

        try:
            self.lighting = Lighting(self.car)
            if hasattr(self.main_menu, 'sun') and self.lighting and hasattr(self.lighting, 'sun'):
                self.main_menu.sun = self.lighting.sun
        except Exception as e:
            print(f"ERROR: Failed to create Lighting. Error: {e}")


        try:
            self.sky = Sky(texture="sky")
        except Exception as e:
            print(f"ERROR: Failed to create Sky. Error: {e}")

        # Setup Update Loop
        self.setup_update_loop()
        print("Game initialization complete.")


    def setup_window(self):
        """Configures the main application window."""
        print("Setting up window...")
        window.title = "Rally"
        window.borderless = False
        window.cog_button.disable()
        window.fps_counter.disable()
        window.exit_button.disable()

        if sys.platform != "darwin":
            window.fullscreen = True
        else:
            try:
                screen_res = window.screen_resolution
                if screen_res and hasattr(window, 'fullscreen_size'):
                    window.size = window.fullscreen_size
                    window.position = Vec2(
                        int((screen_res[0] - window.fullscreen_size[0]) / 2),
                        int((screen_res[1] - window.fullscreen_size[1]) / 2),
                    )
                else:
                     print("Warning: Could not get screen resolution/fullscreen size (macOS). Using defaults.")
                     window.size = (1280, 720)
                     window.center_on_screen()
            except Exception as e:
                 print(f"Warning: Error setting window size/position (macOS). {e}")
                 window.size = (1280, 720)
                 window.center_on_screen()

        try:
             font_path = os.path.join(self.assets.asset_folder.resolve(), "Roboto.ttf")
             if os.path.exists(font_path):
                 Text.default_font = font_path
             else:
                 print(f"Warning: Font file not found at '{font_path}'. Using Ursina's default.")
                 Text.default_font = None
        except Exception as e:
             print(f"Warning: Error setting default font. {e}")
             Text.default_font = None

        Text.default_resolution = 1080 * Text.size
        print("Window setup complete.")


    def create_tracks(self):
        """Creates track objects using the imported classes."""
        print("\nCreating Tracks...")
        tracks = []
        track_classes = [SandTrack, GrassTrack, SnowTrack, ForestTrack, SavannahTrack, LakeTrack]
        for TrackClass in track_classes:
            try:
                track_instance = TrackClass(self.car)
                tracks.append(track_instance)
                print(f"  Created {TrackClass.__name__}")
            except Exception as e:
                print(f"ERROR: Failed to create instance of {TrackClass.__name__}. Error: {e}")
        print(f"Finished creating tracks: {len(tracks)} loaded.")
        return tracks

    def _assign_tracks_to_car(self):
        """Assigns created track instances to attributes on the car object."""
        print("Assigning track references to car...")
        track_map = {
            "sand_track": SandTrack, "grass_track": GrassTrack, "snow_track": SnowTrack,
            "forest_track": ForestTrack, "savannah_track": SavannahTrack, "lake_track": LakeTrack
        }
        assigned_count = 0
        for attr_name, track_class in track_map.items():
            found_track = next((t for t in self.tracks if isinstance(t, track_class)), None)
            if found_track:
                try:
                    if not hasattr(self.car, attr_name):
                        print(f"  Note: Car class doesn't explicitly define '{attr_name}', adding dynamically.")
                    setattr(self.car, attr_name, found_track)
                    assigned_count += 1
                except Exception as e:
                    print(f"Warning: Could not assign track to car.{attr_name}. Error: {e}")
            else:
                print(f"Warning: Instance of {track_class.__name__} not found in self.tracks list.")
                if hasattr(self.car, attr_name):
                    try:
                        setattr(self.car, attr_name, None)
                    except Exception as e:
                        print(f"Warning: Could not set car.{attr_name} to None. Error: {e}")
        print(f"Assigned {assigned_count} track references.")


    def create_ai_cars(self):
        """Creates AI car objects using the imported AICar class."""
        print("\nCreating AI Cars...")
        ai_cars = []
        positions = [(2, 1, 5), (-2, 1, 5), (4, 1, 10)]
        for i, pos in enumerate(positions):
            try:
                ai_instance = AICar(self.car, [], *self.tracks, position=pos)
                ai_cars.append(ai_instance)
                print(f"  Created AICar {i+1}")
            except Exception as e:
                print(f"ERROR: Failed to create AICar instance {i+1}. Error: {e}")

        for ai in ai_cars:
            ai.ai_list = ai_cars
        if hasattr(self.car, 'ai_list'):
             self.car.ai_list = ai_cars
        else:
             print("Warning: Car object missing 'ai_list' attribute.")
        print("AI lists assigned.")
        return ai_cars

    def setup_update_loop(self):
        """Sets up the main update function called by Ursina."""
        print("Setting up main update loop...")
        def main_update():
            """This function is called every frame by Ursina."""

            if self.achievements and hasattr(self.achievements, 'time_spent'):
                is_paused = hasattr(self.main_menu, 'pause_menu') and self.main_menu.pause_menu.enabled
                if not is_paused:
                    if self.achievements.time_spent < 36000:
                        self.achievements.time_spent += time.dt


        self.app.update = main_update
        print("Main update loop assigned.")


    def demonstrate_polymorphism(self):
        """(Optional) Demonstrates calling a common method on different track types."""
        print("\n--- Demonstrating Polymorphism ---")
        if not self.tracks:
            print("No tracks available for polymorphism demo.")
            return
        print("Calling 'display_info()' on each track object:")
        for track in self.tracks:
            try:
                if hasattr(track, 'display_info') and callable(track.display_info):
                    track.display_info()
                else:
                    print(f"Track Info: {type(track).__name__} (display_info missing)")
            except Exception as e:
                print(f"Error calling display_info on {type(track).__name__}: {e}")
        print("--- End Polymorphism Demonstration ---")

    def run_game(self):
        """Starts the Ursina application main loop."""
        print("\nStarting Game Loop...")
        try:
            self.app.run()
        except Exception as e:
             print(f"ERROR during game run: {e}")
             import traceback
             traceback.print_exc()
        finally:
             print("Game loop finished or interrupted.")


if __name__ == "__main__":
    print("Script started directly. Initializing Game...")
    game_instance = None
    try:
        game_instance = Game()
        game_instance.run_game()
    except SystemExit:
         print("Game initialization failed, exiting.")
    except Exception as e:
         print(f"FATAL ERROR: An unexpected error occurred.")
         import traceback
         traceback.print_exc()

    print("Application exiting.")
