## Running Cmder Shell as VS Code Terminal

👉 **Note:** Before you continue, make sure to update both VS Code and Cmder to the latest versions respectively, as the configuration has been changed in the recent versions.

1. Ensure that both VS Code and Cmder are updated to their latest versions.

2. Press `Ctrl + ,` to access VS Code Settings, then search for `terminal profiles windows`, and click `Edit in settings.json`.

3. Alternatively, open the settings.json file by using the Command Palette (`Ctrl + Shift + P`), typing `settings.json`, and hitting Enter.

4. In the settings.json file, append or modify the following terminal profile for Cmder:

   ```json
   "terminal.integrated.defaultProfile.windows": "Cmder",

   "terminal.integrated.profiles.windows": {
       "Cmder": {
           "name": "Cmder",
           "path": [
               "${env:windir}\\Sysnative\\cmd.exe",
               "${env:windir}\\System32\\cmd.exe"
           ],
           "args": ["/k", "${env:cmder_root}\\vendor\\bin\\vscode_init.cmd"],
           "icon": "terminal-cmd",
           "color": "terminal.ansiGreen"
       },
   }

  👉 **Note:** Ensure that the CMDER_ROOT environment variable is correctly configured. Alternatively, you can replace ${env:cmder_root} with the actual path to your Cmder installation (not recommended).
