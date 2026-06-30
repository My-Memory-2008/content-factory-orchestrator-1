

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
#         notebook_url = "https://www.kaggle.com/code/muhammadasjad2008/scheduler-1/edit"
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
        
        # 1. Fetch official API credentials from GitHub Secrets
        KAGGLE_USER = os.environ.get("KAGGLE_USERNAME")
        KAGGLE_KEY = os.environ.get("KAGGLE_KEY")
        
        if not KAGGLE_USER or not KAGGLE_KEY:
            print("❌ Error: Missing KAGGLE_USERNAME or KAGGLE_KEY secrets!")
            sys.exit(1)

        # Launching headless browser on desktop resolution
        browser = await p.chromium.launch(headless=True, args=["--window-size=1920,1080"])
        
        notebook_url = "https://kaggle.com/code/muhammadasjad2008/scheduler-1/edit"
        login_successful = False
        active_context = None
        active_page = None

        # ====================================================================
        # LAYER 1: TRY ROLLING COOKIES (FAST PATH)
        # ====================================================================
        if os.path.exists("state.json") and os.path.getsize("state.json") > 5:
            print("🔑 Attempting login with historical rolling state.json session cookies...")
            try:
                historical_context = await browser.new_context(
                    storage_state="state.json",
                    viewport={"width": 1920, "height": 1080}
                )
                historical_page = await historical_context.new_page()
                await historical_page.goto(notebook_url, wait_until="domcontentloaded", timeout=45000)
                
                # Verify if we are actually in the editor or got booted to login page
                await historical_page.wait_for_selector("button:has-text('Save Version'), .edit-notebook", timeout=10000)
                print("✅ Historical rolling cookies verified! Session successfully resumed.")
                
                active_context = historical_context
                active_page = historical_page
                login_successful = True
            except Exception as e:
                print(f"⚠️ Historical session cookies expired or flagged by IP jump: {e}")
                if 'historical_page' in locals(): await historical_page.close()
                if 'historical_context' in locals(): await historical_context.close()
                login_successful = False

        # ====================================================================
        # LAYER 2: PERMANENT FALLBACK (NATIVE KAGGLE LOGIN VIA API CREDENTIALS)
        # ====================================================================
        if not login_successful:
            print("🔑 Rolling cookies failed. Executing permanent API-driven login fallback...")
            try:
                original_context = await browser.new_context(viewport={"width": 1920, "height": 1080})
                original_page = await original_context.new_page()
                
                # Navigate straight to Kaggle's clean login gateway
                await original_page.goto("Use code with caution.pythonhttps://kaggle.comUse code with caution.python", wait_until="domcontentloaded")
                
                # Click 'Sign in with Kaggle' to reveal standard user/pass/key fields
                await original_page.click("button:has-text('Sign in with Kaggle'), button:has-text('Email')")
                
                # Kaggle lets you log in using your Username and your permanent API Secret Key!
                await original_page.fill("input[name='username'], input[type='text']", KAGGLE_USER)
                await original_page.fill("input[name='password'], input[type='password']", KAGGLE_KEY)
                
                # Submit login form
                await original_page.click("button[type='submit'], button:has-text('Sign In')")
                await original_page.wait_for_timeout(5000)
                
                # Now navigate to your notebook editor completely authenticated
                print("📡 Routing authenticated browser to editor space...")
                await original_page.goto(notebook_url, wait_until="domcontentloaded", timeout=60000)
                
                active_context = original_context
                active_page = original_page
            except Exception as e:
                print(f"❌ Core API fallback login failed: {e}")
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
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
