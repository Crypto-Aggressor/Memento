# To register Cmder as a context menu option, follow these steps

1. **Open a Terminal as Administrator**:
   - Open the Start menu.
   - Search for "cmd" or "Command Prompt."
   - Right-click on "Command Prompt" and select "Run as administrator."

2. **Navigate to the Cmder Directory**:
   - Use the `cd` command to navigate to the directory where you've placed Cmder. For example:

     ```shell
     cd C:\path\to\cmder
     ```

3. **Execute the Registration Command**:
   - Run the following command to register Cmder as a context menu option:

     ```shell
     .\cmder.exe /REGISTER ALL
     ```

This will add Cmder to the context menu, allowing you to launch it directly from the right-click menu in Windows Explorer.

Remember to replace `C:\path\to\cmder` with the actual path where you've placed the Cmder executable.
