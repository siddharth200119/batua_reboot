# Automatically load a .env file from the root directory
set dotenv-load := true

# Export all justfile variables directly to sub-commands
set export := true

# Change the shell used to execute standard recipes
set shell := ["bash", "-c"]

#Launch Emulator set in env
launch-emulator:
  flutter emulators --launch $EMULATOR_DEVICE_ID
