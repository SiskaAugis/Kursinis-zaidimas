# achievements.py (Corrected race_against_ai)

from UrsinaAchievements import create_achievement # Assuming this import is correct

class RallyAchievements():
    def __init__(self, car, main_menu, sand_track, grass_track, snow_track, forest_track, savannah_track, lake_track):
        self.car = car
        self.main_menu = main_menu
        self.sand_track = sand_track
        self.grass_track = grass_track
        self.snow_track = snow_track
        self.forest_track = forest_track
        self.savannah_track = savannah_track
        self.lake_track = lake_track

        self.time_spent = 0

        # Initialize achievement condition checkers for different tracks/categories
        # (Assuming these classes are defined below or imported correctly)
        sand_achievements = SandTrackAchievements(self.car, self.main_menu, self.sand_track)
        grass_achievements = GrassTrackAchievements(self.car, self.main_menu, self.grass_track)
        snow_achievements = SnowTrackAchievements(self.car, self.main_menu, self.snow_track)
        forest_achievements = ForestTrackAchievements(self.car, self.main_menu, self.forest_track)
        savannah_achievements = SavannahTrackAchievements(self.car, self.main_menu, self.savannah_track)
        lake_achievements = LakeTrackAchievements(self.car, self.main_menu, self.lake_track)
        car_achievements = CarAchievements(self.car, self.main_menu, self.sand_track, self.grass_track, self.snow_track, self.forest_track, self.savannah_track, self.lake_track)

        # --- Register Achievements ---
        # General Achievements
        create_achievement("Play the game!", self.play_the_game, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Race against AI!", self.race_against_ai, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Go to the Garage!", self.garage, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Play Time Trial!", self.time_trial, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Drift Gamemode!", self.unlock_drift, icon = "confetti.png", ringtone = "unlock.mp3")

        # First Play Achievements
        create_achievement("Race on Sand Track for the first time!", sand_achievements.play_sand_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Race on Grass Track for the first time!", grass_achievements.play_grass_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Race on Snow Track for the first time!", snow_achievements.play_snow_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Race on Forest Track for the first time!", forest_achievements.play_forest_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Race on Savannah Track for the first time!", savannah_achievements.play_savannah_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Race on Lake Track for the first time!", lake_achievements.play_lake_track, icon = "confetti.png", ringtone = "unlock.mp3")

        # Sand Track Time Achievements
        create_achievement("Get under 20s on Sand Track!", sand_achievements.twenty_seconds_sand_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 17s on Sand Track!", sand_achievements.seventeen_seconds_sand_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 15s on Sand Track!", sand_achievements.fifteen_seconds_sand_track, icon = "confetti.png", ringtone = "unlock.mp3")

        # Grass Track Time Achievements
        create_achievement("Get under 22s on Grass Track!", grass_achievements.twentytwo_seconds_grass_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 20s on Grass Track!", grass_achievements.twenty_seconds_grass_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 18s on Grass Track!", grass_achievements.eighteen_seconds_grass_track, icon = "confetti.png", ringtone = "unlock.mp3")

        # Snow Track Time Achievements
        create_achievement("Get under 40s on Snow Track!", snow_achievements.fourty_seconds_snow_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 36s on Snow Track!", snow_achievements.thirtysix_seconds_snow_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 33s on Snow Track!", snow_achievements.thirtythree_seconds_snow_track, icon = "confetti.png", ringtone = "unlock.mp3")

        # Forest Track Time Achievements
        create_achievement("Get under 30s on Forest Track!", forest_achievements.thirty_seconds_forest_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 28s on Forest Track!", forest_achievements.twentyeight_seconds_forest_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 26s on Forest Track!", forest_achievements.twentysix_seconds_forest_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 25s on Forest Track!", forest_achievements.twentyfive_seconds_forest_track, icon = "confetti.png", ringtone = "unlock.mp3")

        # Savannah Track Time Achievements
        create_achievement("Get under 20s on Savannah Track!", savannah_achievements.twenty_seconds_savannah_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 18s on Savannah Track!", savannah_achievements.eighteen_seconds_savannah_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 16s on Savannah Track!", savannah_achievements.sixteen_seconds_savannah_track, icon = "confetti.png", ringtone = "unlock.mp3")

        # Lake Track Time Achievements
        create_achievement("Get under 60s on Lake Track!", lake_achievements.sixty_seconds_lake_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 55s on Lake Track!", lake_achievements.fiftyfive_seconds_lake_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 50s on Lake Track!", lake_achievements.fifty_seconds_lake_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Get under 47s on Lake Track!", lake_achievements.fourtyseven_seconds_lake_track, icon = "confetti.png", ringtone = "unlock.mp3")

        # Car Unlock Achievements
        create_achievement("Unlock Muscle Car!", car_achievements.unlock_muscle_car, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Limo!", car_achievements.unlock_limo, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Lorry!", car_achievements.unlock_lorry, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Hatchback!", car_achievements.unlock_hatchback, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Rally Car!", car_achievements.unlock_rally, icon = "confetti.png", ringtone = "unlock.mp3")

        # Sports Car Texture Unlock Achievements
        create_achievement("Unlock Sports Car Green!", car_achievements.sports_green, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Sports Car Orange!", car_achievements.sports_orange, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Sports Car White!", car_achievements.sports_white, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Sports Car Black!", car_achievements.sports_black, icon = "confetti.png", ringtone = "unlock.mp3")
        # Assuming Blue is unlocked by default or via another achievement

        # Muscle Car Texture Unlock Achievements
        create_achievement("Unlock Muscle Car Red!", car_achievements.muscle_red, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Muscle Car Blue!", car_achievements.muscle_blue, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Muscle Car Green!", car_achievements.muscle_green, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Muscle Car White!", car_achievements.muscle_white, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Muscle Car Black!", car_achievements.muscle_black, icon = "confetti.png", ringtone = "unlock.mp3")

        # Limo Texture Unlock Achievements
        create_achievement("Unlock Limo Red!", car_achievements.limo_red, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Limo Blue!", car_achievements.limo_blue, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Limo Green!", car_achievements.limo_green, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Limo White!", car_achievements.limo_white, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Limo Orange!", car_achievements.limo_orange, icon = "confetti.png", ringtone = "unlock.mp3")

        # Lorry Texture Unlock Achievements
        create_achievement("Unlock Lorry Red!", car_achievements.lorry_red, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Lorry Blue!", car_achievements.lorry_blue, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Lorry Green!", car_achievements.lorry_green, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Lorry Orange!", car_achievements.lorry_orange, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Lorry Black!", car_achievements.lorry_black, icon = "confetti.png", ringtone = "unlock.mp3")

        # Hatchback Texture Unlock Achievements
        create_achievement("Unlock Hatchback Red!", car_achievements.hatchback_red, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Hatchback Blue!", car_achievements.hatchback_blue, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Hatchback White!", car_achievements.hatchback_white, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Hatchback Orange!", car_achievements.hatchback_orange, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Hatchback Black!", car_achievements.hatchback_black, icon = "confetti.png", ringtone = "unlock.mp3")

        # Rally Car Texture Unlock Achievements
        create_achievement("Unlock Rally Car White!", car_achievements.rally_white, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Rally Car Blue!", car_achievements.rally_blue, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Rally Car Green!", car_achievements.rally_green, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Rally Car Orange!", car_achievements.rally_orange, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Rally Car Black!", car_achievements.rally_black, icon = "confetti.png", ringtone = "unlock.mp3")

        # Mandaw Challenge Achievements
        create_achievement("Beat Mandaw in Sand Track!", self.beat_mandaw_in_sand_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Beat Mandaw in Grass Track!", self.beat_mandaw_in_grass_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Beat Mandaw in Snow Track!", self.beat_mandaw_in_snow_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Beat Mandaw in Forest Track!", self.beat_mandaw_in_forest_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Beat Mandaw in Savannah Track!", self.beat_mandaw_in_savannah_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Beat Mandaw in Lake Track!", self.beat_mandaw_in_lake_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Beat Mandaw in Every Track!", self.beat_mandaw_in_everything, icon = "confetti.png", ringtone = "unlock.mp3")

        # Track Unlock Achievements
        create_achievement("Unlock Grass Track!", self.unlock_grass_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Snow Track!", self.unlock_snow_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Forest Track!", self.unlock_forest_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Savannah Track!", self.unlock_savannah_track, icon = "confetti.png", ringtone = "unlock.mp3")
        create_achievement("Unlock Lake Track!", self.unlock_lake_track, icon = "confetti.png", ringtone = "unlock.mp3")

    # --- Achievement Check Functions ---

    def play_the_game(self):
        """Checks if the game has been played for more than 3 seconds."""
        return self.time_spent > 3

    def race_against_ai(self):
        """Checks if at least one AI car is currently enabled."""
        # --- FIX: Check if ai_list exists, is not empty, and the first AI is enabled ---
        if hasattr(self.car, 'ai_list') and self.car.ai_list:
            # Check if the first AI object exists and has the 'enabled' attribute
            if len(self.car.ai_list) > 0 and hasattr(self.car.ai_list[0], 'enabled'):
                # Return True if the first AI car is enabled
                return self.car.ai_list[0].enabled
        # Return False if ai_list is empty or first AI check fails
        return False
        # --- Alternative: Check if *any* AI is enabled ---
        # if hasattr(self.car, 'ai_list') and self.car.ai_list:
        #     for ai_car in self.car.ai_list:
        #         if hasattr(ai_car, 'enabled') and ai_car.enabled:
        #             return True # Return True if any AI is enabled
        # return False # Return False if no AI cars are enabled

    def garage(self):
        """Checks if the garage menu is currently enabled."""
        # Check if main_menu and garage_menu exist and are not None
        if hasattr(self, 'main_menu') and self.main_menu and hasattr(self.main_menu, 'garage_menu') and self.main_menu.garage_menu:
             return self.main_menu.garage_menu.enabled
        return False # Return False if menus don't exist

    def time_trial(self):
        """Checks if the current gamemode is 'time trial'."""
        # Check if car exists and has the gamemode attribute
        if hasattr(self.car, 'gamemode'):
            return self.car.gamemode == "time trial"
        return False # Return False if attribute doesn't exist

    def unlock_drift(self):
        """Checks if all tracks are unlocked, unlocks drift mode if true."""
        # Check if all track objects exist before accessing 'unlocked'
        if self.sand_track and self.grass_track and self.snow_track and \
           self.forest_track and self.savannah_track and self.lake_track:
            # Check if all tracks have the 'unlocked' attribute and it's True
            if self.sand_track.unlocked and self.grass_track.unlocked and \
               self.snow_track.unlocked and self.forest_track.unlocked and \
               self.savannah_track.unlocked and self.lake_track.unlocked:
                # If all tracks unlocked, set drift unlocked on car and save
                if hasattr(self.car, 'drift_unlocked'):
                    self.car.drift_unlocked = True
                if hasattr(self.car, 'save_unlocked'):
                    self.car.save_unlocked()
                return True # Return True to trigger achievement
        return False # Return False otherwise

    # --- Track Unlock Checks ---
    # (These methods check race times to unlock subsequent tracks)

    def unlock_grass_track(self):
        """Unlocks Grass Track if Sand Track time is <= 22s."""
        # Check if currently playing Sand Track and car finished race
        if self.sand_track and self.sand_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            # Check if time condition met
            if self.car.last_count <= 22:
                # Unlock Grass Track on the track object and save via car
                if hasattr(self.grass_track, 'unlocked'): self.grass_track.unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True # Trigger achievement
        return False

    def unlock_snow_track(self):
        """Unlocks Snow Track if Grass Track time is <= 23s."""
        if self.grass_track and self.grass_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 23:
                if hasattr(self.snow_track, 'unlocked'): self.snow_track.unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def unlock_forest_track(self):
        """Unlocks Forest Track if Snow Track time is <= 40s."""
        if self.snow_track and self.snow_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 40:
                if hasattr(self.forest_track, 'unlocked'): self.forest_track.unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def unlock_savannah_track(self):
        """Unlocks Savannah Track if Forest Track time is <= 32s."""
        if self.forest_track and self.forest_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 32:
                if hasattr(self.savannah_track, 'unlocked'): self.savannah_track.unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def unlock_lake_track(self):
        """Unlocks Lake Track if Savannah Track time is <= 20s."""
        if self.savannah_track and self.savannah_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 20:
                if hasattr(self.lake_track, 'unlocked'): self.lake_track.unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    # --- Mandaw Challenge Checks ---
    # (These check if player beat a specific time on a specific track)

    def beat_mandaw_in_sand_track(self):
        """Checks if player beat Mandaw's time on Sand Track."""
        if self.sand_track and self.sand_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 13.09:
                if hasattr(self.car, 'beat_mandaw_sand_track'): self.car.beat_mandaw_sand_track = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def beat_mandaw_in_grass_track(self):
        """Checks if player beat Mandaw's time on Grass Track (unlocks Banana)."""
        if self.grass_track and self.grass_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 15.55:
                if hasattr(self.car, 'beat_mandaw_grass_track'): self.car.beat_mandaw_grass_track = True
                if hasattr(self.car, 'banana_unlocked'): self.car.banana_unlocked = True # Unlock Banana cosmetic
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def beat_mandaw_in_snow_track(self):
        """Checks if player beat Mandaw's time on Snow Track."""
        if self.snow_track and self.snow_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 27.41:
                if hasattr(self.car, 'beat_mandaw_snow_track'): self.car.beat_mandaw_snow_track = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def beat_mandaw_in_forest_track(self):
        """Checks if player beat Mandaw's time on Forest Track."""
        if self.forest_track and self.forest_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 21.73:
                if hasattr(self.car, 'beat_mandaw_forest_track'): self.car.beat_mandaw_forest_track = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def beat_mandaw_in_savannah_track(self):
        """Checks if player beat Mandaw's time on Savannah Track."""
        if self.savannah_track and self.savannah_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 12.31:
                if hasattr(self.car, 'beat_mandaw_savannah_track'): self.car.beat_mandaw_savannah_track = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def beat_mandaw_in_lake_track(self):
        """Checks if player beat Mandaw's time on Lake Track."""
        if self.lake_track and self.lake_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 39.45:
                if hasattr(self.car, 'beat_mandaw_lake_track'): self.car.beat_mandaw_lake_track = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def beat_mandaw_in_everything(self):
        """Checks if player beat Mandaw on all tracks (unlocks Surfin Bird)."""
        # Check if car object has all the necessary boolean flags
        required_flags = [
            'beat_mandaw_sand_track', 'beat_mandaw_grass_track', 'beat_mandaw_snow_track',
            'beat_mandaw_forest_track', 'beat_mandaw_savannah_track', 'beat_mandaw_lake_track'
        ]
        if all(hasattr(self.car, flag) for flag in required_flags):
            # Check if all flags are True
            if all(getattr(self.car, flag) for flag in required_flags):
                # Unlock Surfin Bird cosmetic
                if hasattr(self.car, 'surfinbird_unlocked'): self.car.surfinbird_unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False


# ==============================================================
# === Track-Specific Achievement Classes =======================
# ==============================================================
# These classes group achievements for specific tracks for better organization.

class SandTrackAchievements():
    def __init__(self, car, main_menu, sand_track):
        self.car = car
        self.main_menu = main_menu
        self.sand_track = sand_track

    def play_sand_track(self):
        """Checks if Sand Track has been played."""
        return self.sand_track and hasattr(self.sand_track, 'played') and self.sand_track.played

    def twenty_seconds_sand_track(self):
        """Checks if Sand Track time is <= 20s."""
        if self.sand_track and self.sand_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 20
        return False

    def seventeen_seconds_sand_track(self):
        """Checks if Sand Track time is <= 17s."""
        if self.sand_track and self.sand_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 17
        return False

    def fifteen_seconds_sand_track(self):
        """Checks if Sand Track time is <= 15s (unlocks Viking Helmet)."""
        if self.sand_track and self.sand_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 15:
                # Unlock Viking Helmet cosmetic
                if hasattr(self.car, 'viking_helmet_unlocked'): self.car.viking_helmet_unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False


class GrassTrackAchievements():
    def __init__(self, car, main_menu, grass_track):
        self.car = car
        self.main_menu = main_menu
        self.grass_track = grass_track

    def play_grass_track(self):
        """Checks if Grass Track has been played."""
        return self.grass_track and hasattr(self.grass_track, 'played') and self.grass_track.played

    def twentytwo_seconds_grass_track(self):
        """Checks if Grass Track time is <= 22s."""
        if self.grass_track and self.grass_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 22
        return False

    def twenty_seconds_grass_track(self):
        """Checks if Grass Track time is <= 20s."""
        if self.grass_track and self.grass_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 20
        return False

    def eighteen_seconds_grass_track(self):
        """Checks if Grass Track time is <= 18s."""
        if self.grass_track and self.grass_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 18
        return False


class SnowTrackAchievements():
    def __init__(self, car, main_menu, snow_track):
        self.car = car
        self.main_menu = main_menu
        self.snow_track = snow_track

    def play_snow_track(self):
        """Checks if Snow Track has been played."""
        return self.snow_track and hasattr(self.snow_track, 'played') and self.snow_track.played

    def fourty_seconds_snow_track(self):
        """Checks if Snow Track time is <= 40s."""
        if self.snow_track and self.snow_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 40
        return False

    def thirtysix_seconds_snow_track(self):
        """Checks if Snow Track time is <= 36s."""
        # Note: Original code had 35, assuming 36 based on achievement name
        if self.snow_track and self.snow_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 36
        return False

    def thirtythree_seconds_snow_track(self):
        """Checks if Snow Track time is <= 33s."""
        # Note: Original code had 32, assuming 33 based on achievement name
        if self.snow_track and self.snow_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 33
        return False


class ForestTrackAchievements():
    def __init__(self, car, main_menu, forest_track):
        self.car = car
        self.main_menu = main_menu
        self.forest_track = forest_track

    def play_forest_track(self):
        """Checks if Forest Track has been played."""
        return self.forest_track and hasattr(self.forest_track, 'played') and self.forest_track.played

    def thirty_seconds_forest_track(self):
        """Checks if Forest Track time is <= 30s."""
        if self.forest_track and self.forest_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 30
        return False

    def twentyeight_seconds_forest_track(self):
        """Checks if Forest Track time is <= 28s."""
        if self.forest_track and self.forest_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 28
        return False

    def twentysix_seconds_forest_track(self):
        """Checks if Forest Track time is <= 26s."""
        if self.forest_track and self.forest_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 26
        return False

    def twentyfive_seconds_forest_track(self):
        """Checks if Forest Track time is <= 25s (unlocks Duck)."""
        if self.forest_track and self.forest_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 25:
                # Unlock Duck cosmetic
                if hasattr(self.car, 'duck_unlocked'): self.car.duck_unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False


class SavannahTrackAchievements():
    def __init__(self, car, main_menu, savannah_track):
        self.car = car
        self.main_menu = main_menu
        self.savannah_track = savannah_track

    def play_savannah_track(self):
        """Checks if Savannah Track has been played."""
        return self.savannah_track and hasattr(self.savannah_track, 'played') and self.savannah_track.played

    def twenty_seconds_savannah_track(self):
        """Checks if Savannah Track time is <= 20s."""
        if self.savannah_track and self.savannah_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 20
        return False

    def eighteen_seconds_savannah_track(self):
        """Checks if Savannah Track time is <= 18s."""
        if self.savannah_track and self.savannah_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 18
        return False

    def sixteen_seconds_savannah_track(self):
        """Checks if Savannah Track time is <= 16s."""
        # Note: Original code had 17, assuming 16 based on achievement name
        if self.savannah_track and self.savannah_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 16
        return False


class LakeTrackAchievements():
    def __init__(self, car, main_menu, lake_track):
        self.car = car
        self.main_menu = main_menu
        self.lake_track = lake_track

    def play_lake_track(self):
        """Checks if Lake Track has been played."""
        return self.lake_track and hasattr(self.lake_track, 'played') and self.lake_track.played

    def sixty_seconds_lake_track(self):
        """Checks if Lake Track time is <= 60s."""
        if self.lake_track and self.lake_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 60
        return False

    def fiftyfive_seconds_lake_track(self):
        """Checks if Lake Track time is <= 55s."""
        if self.lake_track and self.lake_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 55
        return False

    def fifty_seconds_lake_track(self):
        """Checks if Lake Track time is <= 50s."""
        if self.lake_track and self.lake_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 50
        return False

    def fourtyseven_seconds_lake_track(self):
        """Checks if Lake Track time is <= 47s."""
        if self.lake_track and self.lake_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            return self.car.last_count <= 47
        return False


# ==============================================================
# === Car/Texture Unlock Achievement Class =====================
# ==============================================================

class CarAchievements():
    """Groups achievements related to unlocking cars and textures."""
    def __init__(self, car, main_menu, sand_track, grass_track, snow_track, forest_track, savannah_track, lake_track):
        self.car = car
        self.main_menu = main_menu
        # Store track references if needed for specific car unlocks tied to tracks
        self.sand_track = sand_track
        self.grass_track = grass_track
        self.snow_track = snow_track
        self.forest_track = forest_track
        self.savannah_track = savannah_track
        self.lake_track = lake_track

    # --- Car Unlocks ---
    def unlock_muscle_car(self):
        """Unlocks Muscle Car if Savannah Track time is <= 18s."""
        if self.savannah_track and self.savannah_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 18:
                if hasattr(self.car, 'muscle_unlocked'): self.car.muscle_unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def unlock_limo(self):
        """Unlocks Limo if Grass Track time is <= 20s."""
        if self.grass_track and self.grass_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 20:
                if hasattr(self.car, 'limo_unlocked'): self.car.limo_unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def unlock_lorry(self):
        """Unlocks Lorry if Forest Track time is <= 28s."""
        if self.forest_track and self.forest_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 28:
                if hasattr(self.car, 'lorry_unlocked'): self.car.lorry_unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def unlock_hatchback(self):
        """Unlocks Hatchback if Sand Track time is <= 20s."""
        if self.sand_track and self.sand_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 20:
                if hasattr(self.car, 'hatchback_unlocked'): self.car.hatchback_unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    def unlock_rally(self):
        """Unlocks Rally Car if Lake Track time is <= 60s."""
        if self.lake_track and self.lake_track.enabled and hasattr(self.car, 'last_count') and self.car.last_count != 0:
            if self.car.last_count <= 60:
                if hasattr(self.car, 'rally_unlocked'): self.car.rally_unlocked = True
                if hasattr(self.car, 'save_unlocked'): self.car.save_unlocked()
                return True
        return False

    # --- Sports Car Textures ---
    def sports_green(self):
        if self.grass_track and self.grass_track.enabled and self.car.car_type == "sports" and self.car.last_count != 0:
            if self.car.last_count <= 22:
                self.car.sports_green_unlocked = True; self.car.save_unlocked(); return True
        return False

    def sports_orange(self):
        if self.savannah_track and self.savannah_track.enabled and self.car.car_type == "sports" and self.car.last_count != 0:
            if self.car.last_count <= 18:
                self.car.sports_orange_unlocked = True; self.car.save_unlocked(); return True
        return False

    def sports_white(self):
        if self.snow_track and self.snow_track.enabled and self.car.car_type == "sports" and self.car.last_count != 0:
            if self.car.last_count <= 37:
                self.car.sports_white_unlocked = True; self.car.save_unlocked(); return True
        return False

    def sports_black(self):
        if self.forest_track and self.forest_track.enabled and self.car.car_type == "sports" and self.car.last_count != 0:
            if self.car.last_count <= 29:
                self.car.sports_black_unlocked = True; self.car.save_unlocked(); return True
        return False

    # --- Muscle Car Textures ---
    def muscle_red(self):
        if self.savannah_track and self.savannah_track.enabled and self.car.car_type == "muscle" and self.car.last_count != 0:
             if self.car.last_count <= 17:
                 self.car.muscle_red_unlocked = True; self.car.save_unlocked(); return True
        return False

    def muscle_blue(self):
        if self.lake_track and self.lake_track.enabled and self.car.car_type == "muscle" and self.car.last_count != 0:
             if self.car.last_count <= 52:
                 self.car.muscle_blue_unlocked = True; self.car.save_unlocked(); return True
        return False

    def muscle_green(self):
        if self.grass_track and self.grass_track.enabled and self.car.car_type == "muscle" and self.car.last_count != 0:
             if self.car.last_count <= 20:
                 self.car.muscle_green_unlocked = True; self.car.save_unlocked(); return True
        return False

    def muscle_white(self):
        if self.snow_track and self.snow_track.enabled and self.car.car_type == "muscle" and self.car.last_count != 0:
             if self.car.last_count <= 38:
                 self.car.muscle_white_unlocked = True; self.car.save_unlocked(); return True
        return False

    def muscle_black(self):
        if self.forest_track and self.forest_track.enabled and self.car.car_type == "muscle" and self.car.last_count != 0:
             if self.car.last_count <= 28:
                 self.car.muscle_black_unlocked = True; self.car.save_unlocked(); return True
        return False

    # --- Limo Textures ---
    def limo_red(self):
        if self.sand_track and self.sand_track.enabled and self.car.car_type == "limo" and self.car.last_count != 0:
             if self.car.last_count <= 19:
                 self.car.limo_red_unlocked = True; self.car.save_unlocked(); return True
        return False

    def limo_blue(self):
        if self.lake_track and self.lake_track.enabled and self.car.car_type == "limo" and self.car.last_count != 0:
             if self.car.last_count <= 60:
                 self.car.limo_blue_unlocked = True; self.car.save_unlocked(); return True
        return False

    def limo_green(self):
        if self.forest_track and self.forest_track.enabled and self.car.car_type == "limo" and self.car.last_count != 0:
             if self.car.last_count <= 28:
                 self.car.limo_green_unlocked = True; self.car.save_unlocked(); return True
        return False

    def limo_white(self):
        if self.snow_track and self.snow_track.enabled and self.car.car_type == "limo" and self.car.last_count != 0:
             if self.car.last_count <= 38:
                 self.car.limo_white_unlocked = True; self.car.save_unlocked(); return True
        return False

    def limo_orange(self):
        if self.savannah_track and self.savannah_track.enabled and self.car.car_type == "limo" and self.car.last_count != 0:
             if self.car.last_count <= 18:
                 self.car.limo_orange_unlocked = True; self.car.save_unlocked(); return True
        return False

    # --- Lorry Textures ---
    def lorry_red(self):
        if self.sand_track and self.sand_track.enabled and self.car.car_type == "lorry" and self.car.last_count != 0:
             if self.car.last_count <= 20:
                 self.car.lorry_red_unlocked = True; self.car.save_unlocked(); return True
        return False

    def lorry_blue(self):
        if self.lake_track and self.lake_track.enabled and self.car.car_type == "lorry" and self.car.last_count != 0:
             if self.car.last_count <= 70:
                 self.car.lorry_blue_unlocked = True; self.car.save_unlocked(); return True
        return False

    def lorry_green(self):
        if self.grass_track and self.grass_track.enabled and self.car.car_type == "lorry" and self.car.last_count != 0:
             if self.car.last_count <= 21:
                 self.car.lorry_green_unlocked = True; self.car.save_unlocked(); return True
        return False

    def lorry_black(self):
        if self.snow_track and self.snow_track.enabled and self.car.car_type == "lorry" and self.car.last_count != 0:
             if self.car.last_count <= 38:
                 self.car.lorry_black_unlocked = True; self.car.save_unlocked(); return True
        return False

    def lorry_orange(self):
        if self.savannah_track and self.savannah_track.enabled and self.car.car_type == "lorry" and self.car.last_count != 0:
             if self.car.last_count <= 19:
                 self.car.lorry_orange_unlocked = True; self.car.save_unlocked(); return True
        return False

    # --- Hatchback Textures ---
    def hatchback_red(self):
        if self.sand_track and self.sand_track.enabled and self.car.car_type == "hatchback" and self.car.last_count != 0:
             if self.car.last_count <= 18:
                 self.car.hatchback_red_unlocked = True; self.car.save_unlocked(); return True
        return False

    def hatchback_blue(self):
        if self.lake_track and self.lake_track.enabled and self.car.car_type == "hatchback" and self.car.last_count != 0:
             if self.car.last_count <= 65:
                 self.car.hatchback_blue_unlocked = True; self.car.save_unlocked(); return True
        return False

    def hatchback_white(self):
        if self.grass_track and self.grass_track.enabled and self.car.car_type == "hatchback" and self.car.last_count != 0:
             if self.car.last_count <= 20:
                 self.car.hatchback_white_unlocked = True; self.car.save_unlocked(); return True
        return False

    def hatchback_black(self):
        if self.snow_track and self.snow_track.enabled and self.car.car_type == "hatchback" and self.car.last_count != 0:
             if self.car.last_count <= 37:
                 self.car.hatchback_black_unlocked = True; self.car.save_unlocked(); return True
        return False

    def hatchback_orange(self):
        if self.savannah_track and self.savannah_track.enabled and self.car.car_type == "hatchback" and self.car.last_count != 0:
             if self.car.last_count <= 18:
                 self.car.hatchback_orange_unlocked = True; self.car.save_unlocked(); return True
        return False

    # --- Rally Car Textures ---
    def rally_white(self):
        if self.sand_track and self.sand_track.enabled and self.car.car_type == "rally" and self.car.last_count != 0:
             if self.car.last_count <= 17:
                 self.car.rally_white_unlocked = True; self.car.save_unlocked(); return True
        return False

    def rally_blue(self):
        if self.lake_track and self.lake_track.enabled and self.car.car_type == "rally" and self.car.last_count != 0:
             if self.car.last_count <= 52:
                 self.car.rally_blue_unlocked = True; self.car.save_unlocked(); return True
        return False

    def rally_green(self):
        if self.grass_track and self.grass_track.enabled and self.car.car_type == "rally" and self.car.last_count != 0:
             if self.car.last_count <= 19:
                 self.car.rally_green_unlocked = True; self.car.save_unlocked(); return True
        return False

    def rally_black(self):
        if self.snow_track and self.snow_track.enabled and self.car.car_type == "rally" and self.car.last_count != 0:
             if self.car.last_count <= 35:
                 self.car.rally_black_unlocked = True; self.car.save_unlocked(); return True
        return False

    def rally_orange(self):
        if self.savannah_track and self.savannah_track.enabled and self.car.car_type == "rally" and self.car.last_count != 0:
             if self.car.last_count <= 16:
                 self.car.rally_orange_unlocked = True; self.car.save_unlocked(); return True
        return False

