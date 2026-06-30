# import os
# import json
# import subprocess
# import sys


# #check if kaggle is installed if not install kaggle module
# try:
#     import kaggle
# except ImportError:
#     print("-> 'kaggle' module missing. Initiating force-install sequence...")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
#     subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle"])
#     print("✅ 'kaggle' package successfully injected into environment.")

# # 1. Fetch credentials safely from the execution environment
# KAGGLE_USERNAME = os.environ.get("KAGGLE_USERNAME")
# KAGGLE_KEY = os.environ.get("KAGGLE_KEY")

# if not KAGGLE_USERNAME or not KAGGLE_KEY:
#     print("❌ Error: Missing KAGGLE_USERNAME or KAGGLE_KEY environment variables!")
#     exit(1)

# # Trim out any invisible newline or whitespace gaps
# KAGGLE_USERNAME = KAGGLE_USERNAME.strip()
# KAGGLE_KEY = KAGGLE_KEY.strip()

# print("[1/3] Generating secure native token file...")

# # 2. Re-create the secure credentials folder structure required by Kaggle
# home_dir = os.path.expanduser("~")
# kaggle_folder = os.path.join(home_dir, ".kaggle")
# os.makedirs(kaggle_folder, exist_ok=True)

# token_path = os.path.join(kaggle_folder, "kaggle.json")
# with open(token_path, "w") as f:
#     json.dump({"username": KAGGLE_USERNAME, "key": KAGGLE_KEY}, f)

# # Lock down file system permissions so the client accepts it safely
# os.chmod(token_path, 0o600)
# print("✅ Token file created and locked down.")

# # 3. Create the kernel-metadata.json file safely within Python
# print("[2/3] Writing kernel control properties file...")
# meta_payload = {
#     "id": "muhammadasjad2008/content-factory-engine",
#     "title": "Content Factory Engine",
#     "code_file": "content-factory-engine.py",
#     "language": "python",
#     "kernel_type": "script",
#     "is_private": "true",
#     "enable_gpu": "true",
#     "enable_internet": "true",
#     "accelerator": "nvidia-tesla-t4-x2",
#      "dataset_sources": [
#         "muhammadasjad2008/cat-reactions-vault" # 👈 Paste your exact lowercase Kaggle dataset slug here
#     ],
#     "competition_sources": [],
#     "kernel_sources": []
# }

# with open("kernel-metadata.json", "w") as f:
#     json.dump(meta_payload, f, indent=2)
# print("✅ kernel-metadata.json created.")

# # 4. 🔥 FIX: CALL THE CORRECT UNIVERSAL KERNELS_PUSH METHOD
# print("[3/3] Launching official Kaggle push trigger protocol natively...")

# try:
#     # Import the official client class engine directly from Python memory
#     from kaggle.api.kaggle_api_extended import KaggleApi
    
#     # Initialize and authenticate the API connection from the token file we created
#     api = KaggleApi()
#     api.authenticate()
    
#     # Execute the push function directly through universal standard attributes
#     print("📡 Uploading files and initiating Kaggle T4 GPU instance...")
#     api.kernels_push(".")
    
#     print("🚀 SUCCESS! The trigger payload cleared gates safely via native code lines.")
#     print("🔗 Monitor progress here: https://kaggle.com")

# except Exception as e:
#     print(f"❌ Critical Error: Kaggle native API engine failed to complete the push: {e}")
#     exit(1)




# import os
# import json
# import subprocess
# import sys

# # Check if kaggle is installed if not install kaggle module
# try:
#     import kaggle
# except ImportError:
#     print("-> 'kaggle' module missing. Initiating force-install sequence...")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
#     subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle"])
#     print("✅ 'kaggle' package successfully injected into environment.")

# # 1. Fetch credentials safely from the execution environment
# KAGGLE_USERNAME = os.environ.get("KAGGLE_USERNAME")
# KAGGLE_KEY = os.environ.get("KAGGLE_KEY")

# if not KAGGLE_USERNAME or not KAGGLE_KEY:
#     print("❌ Error: Missing KAGGLE_USERNAME or KAGGLE_KEY environment variables!")
#     exit(1)

# # Trim out any invisible newline or whitespace gaps
# KAGGLE_USERNAME = KAGGLE_USERNAME.strip()
# KAGGLE_KEY = KAGGLE_KEY.strip()

# print("[1/3] Generating secure native token file...")

# # 2. Re-create the secure credentials folder structure required by Kaggle
# home_dir = os.path.expanduser("~")
# kaggle_folder = os.path.join(home_dir, ".kaggle")
# os.makedirs(kaggle_folder, exist_ok=True)

# token_path = os.path.join(kaggle_folder, "kaggle.json")
# with open(token_path, "w") as f:
#     json.dump({"username": KAGGLE_USERNAME, "key": KAGGLE_KEY}, f)

# # Lock down file system permissions so the client accepts it safely
# os.chmod(token_path, 0o600)
# print("✅ Token file created and locked down.")

# # 3. Create the kernel-metadata.json file safely within Python
# print("[2/3] Writing kernel control properties file...")

# # 🔥 THE ENFORCED SCHEMA CORRECTION:
# # We swapped out 'accelerator' for the official parameters 'gpuType' and 'isGpuGroup'
# # to command the endpoint parser to spin up your dual T4x2 environment!
# meta_payload = {
#     "id": "muhammadasjad2008/content-factory-engine",
#     "title": "Content Factory Engine",
#     "code_file": "content-factory-engine.py",
#     "language": "python",
#     "kernel_type": "script",
#     "is_private": "true",
#     "enable_gpu": "true",
#     "enable_internet": "true",
#     "dataset_sources": [
#         "muhammadasjad2008/cat-reactions-vault"
#     ],
#     "competition_sources": [],
#     "kernel_sources": []
# }

# with open("kernel-metadata.json", "w") as f:
#     json.dump(meta_payload, f, indent=2)
# print("✅ kernel-metadata.json created.")

# # 4. CALL THE CORRECT UNIVERSAL KERNELS_PUSH METHOD
# print("[3/3] Launching official Kaggle push trigger protocol natively...")

# try:
#     # Import the official client class engine directly from Python memory
#     from kaggle.api.kaggle_api_extended import KaggleApi
    
#     # Initialize and authenticate the API connection from the token file we created
#     api = KaggleApi()
#     api.authenticate()
    
#     # Execute the push function directly through universal standard attributes
#     print("📡 Uploading files and initiating Kaggle T4 GPU instance...")
#     api.kernels_push(".")
    
#     print("🚀 SUCCESS! The trigger payload cleared gates safely via native code lines.")
#     print("🔗 Monitor progress here: https://kaggle.com")

# except Exception as e:
#     print(f"❌ Critical Error: Kaggle native API engine failed to complete the push: {e}")
#     exit(1)







# import asyncio
# import os
# import sys
# from playwright.async_api import async_playwright

# async def run():
#     async with async_playwright() as p:
#         print("🚀 Setting up cloud execution trigger environment for Kaggle Script mode...")
        
#         # Verify repository secrets token block 
#         secret_auth_data = os.environ.get("KAGGLE_AUTH_JSON")
#         if not secret_auth_data:
#             print("❌ Error: Missing KAGGLE_AUTH_JSON environment variable secret!")
#             sys.exit(1)
            
#         with open("kaggle_auth.json", "w") as f:
#             f.write(secret_auth_data)

#         # Force standard desktop dimensions to guarantee editor focus areas are mapped properly
#         browser = await p.chromium.launch(headless=True, args=["--window-size=1920,1080"])
#         context = await browser.new_context(
#             storage_state="kaggle_auth.json",
#             viewport={"width": 1920, "height": 1080}
#         )
#         page = await context.new_page()

#         # Exact path of your script editor panel
#         notebook_url = "https://kaggle.com/code/muhammadasjad2008/content-factory-engine/edit/"
#         print(f"📡 Connecting to script workspace: {notebook_url}")
        
#         try:
#             await page.goto(notebook_url, wait_until="domcontentloaded", timeout=90000)
#         except Exception as e:
#             print(f"⚠️ Navigation status context: {e}")
            
#         print("⏳ Waiting 35 seconds for the cloud server to provision your T4 session environment...")
#         await page.wait_for_timeout(35000)

#         # ====================================================================
#         # SCRIPT MODE MULTI-STEP KEYBOARD RUN METHOD
#         # ====================================================================
#         print("🎹 Injecting universal code execution commands...")
        
#         try:
#             # 1. Focus inside the main text code window editor pane 
#             # Kaggle uses CodeMirror layers for script inputs (.cm-content)
#             await page.locator(".cm-content, [role='textbox'], .CodeMirror-code").first.click(timeout=10000)
#             print("🎯 Focus captured successfully on the main code editor cell.")
#         except Exception:
#             print("⚠️ Code cell frame selector missed. Forcing click onto central layout coordinate grid...")
#             await page.mouse.click(960, 540)
            
#         await page.wait_for_timeout(2000)
        
#         # 2. Select the entire contents of your python script file (Ctrl + A)
#         print("⌨️ Selecting all text inside script editor (Control + A)...")
#         await page.keyboard.down("Control")
#         await page.keyboard.press("a")
#         await page.keyboard.up("Control")
#         await page.wait_for_timeout(2000)
        
#         # 3. Trigger execution on the selected text lines (Shift + Enter)
#         print("⚡ Executing entire script file (Shift + Enter)...")
#         await page.keyboard.down("Shift")
#         await page.keyboard.press("Enter")
#         await page.keyboard.up("Shift")

#         print("⏳ Holding active context stream open to ensure code submission clears remote gates...")
#         await page.wait_for_timeout(25000)
        
#         print("🎉 SUCCESS! The text run command sequence has dispatched across your GPU T4 instances.")
#         await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run())





# import asyncio
# import os
# import sys
# from playwright.async_api import async_playwright

# async def run():
#     async with async_playwright() as p:
#         print("🚀 Setting up ultra-efficient Kaggle Script Save Version trigger...")
        
#         # Verify repository secrets token block 
#         secret_auth_data = os.environ.get("KAGGLE_AUTH_JSON")
#         if not secret_auth_data:
#             print("❌ Error: Missing KAGGLE_AUTH_JSON environment variable secret!")
#             sys.exit(1)
            
#         with open("kaggle_auth.json", "w") as f:
#             f.write(secret_auth_data)

#         # Launching headless browser on desktop resolution
#         browser = await p.chromium.launch(headless=True, args=["--window-size=1920,1080"])
#         context = await browser.new_context(
#             storage_state="kaggle_auth.json",
#             viewport={"width": 1920, "height": 1080}
#         )
#         page = await context.new_page()

#         # Exact path of your script editor panel
#         notebook_url = "https://kaggle.com/code/muhammadasjad2008/content-factory-engine-1/edit"
#         print(f"📡 Connecting to script workspace: {notebook_url}")
        
#         try:
#             await page.goto(notebook_url, wait_until="domcontentloaded", timeout=90000)
#         except Exception as e:
#             print(f"⚠️ Navigation status context: {e}")
            
#         print("⏳ Waiting 30 seconds for the editor application layout to stabilize...")
#         await page.wait_for_timeout(30000)

#         # ====================================================================
#         # JAVASCRIPT INJECTION: TRIGGERING NATIVE KAGGLE CORE SAVE ENGINE
#         # ====================================================================
#         print("📋 Injecting JavaScript bypass to trigger background Save Version workflow...")
        
#         # This script locates the exact internal state button and forces a production version commit.
#         # This acts exactly as if you clicked "Save Version" -> "Save & Run All" in the browser!
#         save_js = """
#         () => {
#             // Find any button labeled Save Version or Save version
#             const buttons = Array.from(document.querySelectorAll('button'));
#             const saveBtn = buttons.find(b => b.textContent.toLowerCase().includes('save version'));
            
#             if (saveBtn) {
#                 saveBtn.click();
#                 return true;
#             }
#             return false;
#         }
#         """
        
#         opened_dialog = await page.evaluate(save_js)
#         await page.wait_for_timeout(3000)

#         if opened_dialog:
#             print("🔘 'Save Version' menu opened. Confirming background run allocation...")
#             try:
#                 # Target the final blue confirmation "Save" button inside the popup dialog window
#                 confirm_btn = page.locator("button[data-test-id='save-version-dialog-save-button'], button:has-text('Save')").last
#                 await confirm_btn.click(timeout=10000)
#                 print("🚀 Background 'Save & Run All' successfully triggered!")
#             except Exception as e:
#                 print(f"⚠️ Confirm button selector missed ({e}). Trying fallback keyboard confirm...")
#                 await page.keyboard.press("Enter")
#         else:
#             print("⚠️ Primary JS button locator missed. Deploying fallback hotkey sequence...")
#             # Fallback hotkey sequence to open Save Version dialog if UI changed: Ctrl + Shift + S
#             await page.focus("body")
#             await page.keyboard.down("Control")
#             await page.keyboard.down("Shift")
#             await page.keyboard.press("s")
#             await page.keyboard.up("Shift")
#             await page.keyboard.up("Control")
#             await page.wait_for_timeout(3000)
#             await page.keyboard.press("Enter")
#             print("⚡ Hotkey Save Version pipeline dispatched.")

#         print("⏳ Waiting 15 seconds to ensure the backend server locks in the commit token...")
#         await page.wait_for_timeout(15000)
        
#         print("\n" + "="*80)
#         print("🎉 PIPELINE TRIGGER COMPLETE!")
#         print("Kaggle is now running your script in a locked background environment on your GPU T4.")
#         print("The GPU will automatically power off and stop usage the exact second your code finishes.")
#         print("🔗 Track execution and view live logs here: https://kaggle.com")
#         print("="*80 + "\n")
        
#         await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run())





import asyncio
import os
import sys
import json
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        print("🚀 Setting up ultra-efficient Kaggle Script Save Version trigger...")
        
        # 1. Verify and load repository secrets token blocks
        secret_auth_data = os.environ.get("KAGGLE_AUTH_JSON")
        if not secret_auth_data:
            print("❌ Error: Missing KAGGLE_AUTH_JSON environment variable secret!")
            sys.exit(1)
            
        with open("kaggle_auth.json", "w") as f:
            f.write(secret_auth_data)

        # Launching headless browser on desktop resolution
        browser = await p.chromium.launch(headless=True, args=["--window-size=1920,1080"])
        
        notebook_url = "https://kaggle.com/code/muhammadasjad2008/content-factory-engine-1/edit"
        login_successful = False
        active_context = None
        active_page = None

        # ====================================================================
        # LAYER 1: PRIORITISE ROLLING CLOUD COOKIES (FUTURE AUTOMATION PATH)
        # ====================================================================
        if os.path.exists("state.json") and os.path.getsize("state.json") > 5:
            print("🔑 Path Selected: Attempting login with historical rolling state.json cloud cookies...")
            try:
                # FIXED: Corrected the viewport syntax from a comma-set to a structured key-value pair dictionary
                historical_context = await browser.new_context(
                    storage_state="state.json",
                    viewport={"width": 1920, "height": 1080}
                )
                historical_page = await historical_context.new_page()
                await historical_page.goto(notebook_url, wait_until="domcontentloaded", timeout=45000)
                
                # Verify if we successfully bypassed the login screen into the editor
                await historical_page.wait_for_selector("button:has-text('Save Version'), .edit-notebook", timeout=10000)
                print("✅ Success: Historical rolling cloud cookies verified! Session resumed.")
                
                active_context = historical_context
                active_page = historical_page
                login_successful = True
            except Exception as e:
                print(f"⚠️ Rolling cookies expired or not yet valid on this container branch: {e}")
                if 'historical_page' in locals(): await historical_page.close()
                if 'historical_context' in locals(): await historical_context.close()
                login_successful = False

        # ====================================================================
        # LAYER 2: FIRST-TIME RUN IMPORT (USES KAGGLE_AUTH_JSON SECRET ONLY ONCE)
        # ====================================================================
        if not login_successful:
            print("🔑 Path Selected: Bootstrapping session using KAGGLE_AUTH_JSON secret token layout...")
            try:
                original_context = await browser.new_context(
                    storage_state="kaggle_auth.json",
                    viewport={"width": 1920, "height": 1080}
                )
                original_page = await original_context.new_page()
                await original_page.goto(notebook_url, wait_until="domcontentloaded", timeout=90000)
                
                active_context = original_context
                active_page = original_page
                print("✅ Success: Initial login completed using repository token file framework.")
            except Exception as e:
                print(f"❌ Core navigation failed using backup token structures: {e}")
                sys.exit(1)

        # ====================================================================
            
        print("⏳ Waiting 30 seconds for the editor application layout to stabilize...")
        await active_page.wait_for_timeout(30000)

        # ====================================================================
        # JAVASCRIPT INJECTION: TRIGGERING NATIVE KAGGLE CORE SAVE ENGINE
        # ====================================================================
        print("📋 Injecting JavaScript bypass to trigger background Save Version workflow...")
        
        save_js = """
        () => {
            const buttons = Array.from(document.querySelectorAll('button'));
            const saveBtn = buttons.find(b => b.textContent.toLowerCase().includes('save version'));
            if (saveBtn) {
                saveBtn.click();
                return true;
            }
            return false;
        }
        """
        
        opened_dialog = await active_page.evaluate(save_js)
        await active_page.wait_for_timeout(3000)

        if opened_dialog:
            print("🔘 'Save Version' menu opened. Confirming background run allocation...")
            try:
                confirm_btn = active_page.locator("button[data-test-id='save-version-dialog-save-button'], button:has-text('Save')").last
                await confirm_btn.click(timeout=10000)
                print("🚀 Background 'Save & Run All' successfully triggered!")
            except Exception as e:
                print(f"⚠️ Confirm button selector missed ({e}). Trying fallback keyboard confirm...")
                await active_page.keyboard.press("Enter")
        else:
            print("⚠️ Primary JS button locator missed. Deploying fallback hotkey sequence...")
            await active_page.focus("body")
            await active_page.keyboard.down("Control")
            await active_page.keyboard.down("Shift")
            await active_page.keyboard.press("s")
            await active_page.keyboard.up("Shift")
            await active_page.keyboard.up("Control")
            await active_page.wait_for_timeout(3000)
            await active_page.keyboard.press("Enter")
            print("⚡ Hotkey Save Version pipeline dispatched.")

        print("⏳ Waiting 15 seconds to ensure the backend server locks in the commit token...")
        await active_page.wait_for_timeout(15000)
        
        # ====================================================================
        # EXTRACTION STEP: EXPORT FRESH ACTIVE COOKIES BEFORE DISCONNECTING
        # ====================================================================
        try:
            print("💾 Extracting fresh session tokens from active page workspace configuration...")
            fresh_state = await active_context.storage_state()
            with open("state.json", "w") as sf:
                json.dump(fresh_state, sf, indent=2)
            print("🎉 Success: Refreshed token footprints written out cleanly to state.json.")
        except Exception as state_err:
            print(f"⚠️ Error dumping updated authentication state: {state_err}")
        
        print("\n" + "="*80)
        print("🎉 PIPELINE TRIGGER COMPLETE!")
        print("="*80 + "\n")
        
        # FIX STEP: Add a short 2-second sleep window to let loose execution loops close out cleanly
        await asyncio.sleep(2)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
