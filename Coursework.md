Rally Game Coursework Report
Introduction
Goal: The primary goal of this coursework was to develop a functional 3D rally racing game using the Python programming language and the Ursina game engine. The aim was to create an interactive experience incorporating core game mechanics like vehicle control, multiple environments (tracks), AI opponents, and a user interface for navigation and settings.

Topic & Application: The chosen topic is a single-player rally racing simulation. The application is a desktop game where the player controls a car and competes across various themed tracks. Key features include different car models (selectable via a garage), distinct track environments (sand, grass, snow, forest, savannah, lake), AI-controlled opponents, game modes (Race, Time Trial, Drift - implied by car.py logic), highscore tracking, and potentially unlockable content managed through an achievement system.

How to Run:

Prerequisites: Ensure Python (version 3.x) is installed on the system. The system PATH variable must be configured correctly to find the python and pip commands.

Install Dependencies: Open a command prompt or terminal, navigate to the project's root directory (Rally-master), and install the required packages using pip, primarily Ursina and any dependencies it has (like Panda3D). If a requirements.txt file is provided, run: pip install -r requirements.txt. Otherwise, install Ursina directly: pip install ursina.

Run: Execute the main script from the command line within the project directory:

python main.py

Assets: Ensure the assets folder (containing models, textures, sounds, fonts) and the tracks folder (containing individual track .py files) are present in the same directory as main.py. The highscore folder should also be present or will be created automatically.

How to Use:

Menus: Use the mouse cursor to click on buttons in the menus (Start Menu, Main Menu, Race Mode Select, Map Select, Garage, Settings, Pause Menu).

Driving: Control the car using keyboard inputs (default likely WASD or ZQSD for movement/steering, Space for handbrake - based on typical car.py implementations).

Pause: Press the Escape key during gameplay to open the Pause Menu, allowing you to resume, respawn, or return to the main menu.

Navigation: Follow the on-screen menu prompts to select game modes, tracks, customize the car in the garage, or adjust settings.

Body/Analysis
The application is structured using object-oriented principles in Python, leveraging the Ursina engine, which builds upon Panda3D. The core architecture relies heavily on Composition, where the main Game class acts as an orchestrator, creating and managing instances of various subsystems.

Game Class (Composition Root): The Game class serves as the central hub. Its __init__ method demonstrates composition by creating instances of essential components and storing them as attributes (e.g., self.assets, self.car, self.lighting, self.main_menu). It controls the overall initialization sequence and lifecycle.

# Game.__init__ shows creation and ownership of components
class Game:
    def __init__(self, run_mode='game'):
        # ... initialize Ursina app ...
        self.assets = Assets() # Creates Assets instance
        self.assets.load()
        self.setup_window()
        self.car = Car(...) # Creates Car instance
        # ... creates factories ...
        self.tracks = self.create_tracks(...) # Creates Track list
        self._assign_tracks_to_car()
        self.ai_cars = self.create_ai_cars(...) # Creates AI list
        # ... creates MainMenu, Achievements, Lighting, Sky ...
        self.setup_update_loop()

Asset Management (Assets Class): Encapsulation is used in the Assets class, which bundles lists of model and texture filenames (self.models_to_load, self.textures_to_load) along with the load method responsible for loading them using Ursina's load_model and load_texture functions. This abstracts the loading details away from the main Game class.

# Assets.load abstracts loading details
class Assets:
    def load(self):
        print("\nLoading Assets...")
        for model_name in self.models_to_load:
            try:
                load_model(model_name)
            # ... error handling ...
        for texture_name in self.textures_to_load:
            try:
                load_texture(texture_name)
            # ... error handling ...

Factories (TrackFactory, AICarFactory): The Simple Factory pattern is employed to decouple the Game class from the specific instantiation logic of Track and AICar objects. The Game class requests objects from the factories based on type (for tracks) or parameters (for AI cars), making it easier to add new track or AI types without modifying the Game class extensively.

# TrackFactory encapsulates track creation
class TrackFactory:
    @staticmethod
    def create_track(track_type: str, car: Car) -> BaseTrack | None:
        track_classes = { # Maps string to class
            "sand": SandTrack, "grass": GrassTrack, # ... etc
        }
        track_class = track_classes.get(track_type.lower())
        if track_class:
            try:
                return track_class(car) # Instantiates the specific class
            # ... error handling ...
        # ...

The Game class then uses these factories:

# Game class uses the factory
def create_tracks(self, track_types: list[str]):
    tracks = []
    for track_type in track_types:
        # Delegate creation to the factory
        track_instance = self.track_factory.create_track(track_type, self.car)
        if track_instance:
            tracks.append(track_instance)
    return tracks

Component Initialization Order: The Game.__init__ method carefully orders the creation of components. For instance, Assets is created and loaded before setup_window because the window setup requires the font loaded by Assets. The Car is created before Tracks and AI Cars because they require a reference to the player's car during their own initialization.

Subsystem Interaction (Aggregation/Dependency): While Game composes most parts, interactions between components often involve passing references (Aggregation or simple Dependency). For example, the Car object is passed to Track constructors, MainMenu, Achievements, and Lighting. The MainMenu might receive a reference to the SunLight object (owned by Lighting) to control graphics settings.

Main Execution (if __name__ == "__main__":): This standard Python construct ensures that the game initialization (game = Game()) and the start of the game loop (game.run_game()) only occur when main.py is executed directly, not when it might be imported as a module by another script (like a test runner). It also includes basic error handling for fatal initialization issues and a check for a --test argument to run unit tests instead.

if __name__ == "__main__":
    if '--test' in sys.argv:
        # ... run unit tests ...
    else:
        # Run the game normally
        print("Script started directly. Initializing Game...")
        game_instance = None
        try:
            # Composition Root: Creating the main Game object
            game_instance = Game(run_mode='game')
            # Start the application loop
            game_instance.run_game()

Functional Requirements: The code structure supports the core requirements: a 3D environment (via Ursina), asset loading, distinct track entities, player car control (handled within car.py), AI car entities, lighting (SunLight, AmbientLight), and a multi-screen UI (MainMenu).

Results
The program successfully initializes the Ursina engine, loads a significant number of 3D models and textures, and sets up the core game structure, demonstrating the feasibility of creating a 3D rally game with this framework.

The use of Composition in the Game class provides a clear structure for managing different game subsystems, while Factories help in decoupling object creation logic.

Challenge: Ensuring the correct initialization order of components was critical, as demonstrated by AttributeErrors encountered during development when dependencies (like Assets needed by setup_window) were not ready.

Challenge: Integrating external libraries (UrsinaAchievements) and handling their data file dependencies (achievements.json) required specific configuration (--add-data) when building an executable with PyInstaller.

Challenge: Environment configuration issues (specifically Python's Scripts directory not being in the system PATH) initially hindered the use of command-line tools like pyinstaller, requiring manual PATH adjustments or alternative execution methods (python -m pyinstaller).

Observation: Collision errors noted in the logs (:collide(error): Invalid points in CollisionPolygon:) suggest potential issues with the 3D models used for track boundaries, which could lead to physics glitches during gameplay and require model adjustments in a 3D modeling tool.