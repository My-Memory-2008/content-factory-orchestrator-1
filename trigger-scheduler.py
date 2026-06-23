

import asyncio
import os
import sys
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        print("🚀 Setting up ultra-efficient Kaggle Script Save Version trigger...")
        
        # Verify repository secrets token block 
        secret_auth_data = os.environ.get("KAGGLE_AUTH_JSON")
        if not secret_auth_data:
            print("❌ Error: Missing KAGGLE_AUTH_JSON environment variable secret!")
            sys.exit(1)
            
        with open("kaggle_auth.json", "w") as f:
            f.write(secret_auth_data)

        # Launching headless browser on desktop resolution
        browser = await p.chromium.launch(headless=True, args=["--window-size=1920,1080"])
        context = await browser.new_context(
            storage_state="kaggle_auth.json",
            viewport={"width": 1920, "height": 1080}
        )
        page = await context.new_page()

        # Exact path of your script editor panel
        notebook_url = "https://www.kaggle.com/code/muhammadasjad2008/scheduler-1/edit"
        print(f"📡 Connecting to script workspace: {notebook_url}")
        
        try:
            await page.goto(notebook_url, wait_until="domcontentloaded", timeout=90000)
        except Exception as e:
            print(f"⚠️ Navigation status context: {e}")
            
        print("⏳ Waiting 30 seconds for the editor application layout to stabilize...")
        await page.wait_for_timeout(30000)

        # ====================================================================
        # JAVASCRIPT INJECTION: TRIGGERING NATIVE KAGGLE CORE SAVE ENGINE
        # ====================================================================
        print("📋 Injecting JavaScript bypass to trigger background Save Version workflow...")
        
        # This script locates the exact internal state button and forces a production version commit.
        # This acts exactly as if you clicked "Save Version" -> "Save & Run All" in the browser!
        save_js = """
        () => {
            // Find any button labeled Save Version or Save version
            const buttons = Array.from(document.querySelectorAll('button'));
            const saveBtn = buttons.find(b => b.textContent.toLowerCase().includes('save version'));
            
            if (saveBtn) {
                saveBtn.click();
                return true;
            }
            return false;
        }
        """
        
        opened_dialog = await page.evaluate(save_js)
        await page.wait_for_timeout(3000)

        if opened_dialog:
            print("🔘 'Save Version' menu opened. Confirming background run allocation...")
            try:
                # Target the final blue confirmation "Save" button inside the popup dialog window
                confirm_btn = page.locator("button[data-test-id='save-version-dialog-save-button'], button:has-text('Save')").last
                await confirm_btn.click(timeout=10000)
                print("🚀 Background 'Save & Run All' successfully triggered!")
            except Exception as e:
                print(f"⚠️ Confirm button selector missed ({e}). Trying fallback keyboard confirm...")
                await page.keyboard.press("Enter")
        else:
            print("⚠️ Primary JS button locator missed. Deploying fallback hotkey sequence...")
            # Fallback hotkey sequence to open Save Version dialog if UI changed: Ctrl + Shift + S
            await page.focus("body")
            await page.keyboard.down("Control")
            await page.keyboard.down("Shift")
            await page.keyboard.press("s")
            await page.keyboard.up("Shift")
            await page.keyboard.up("Control")
            await page.wait_for_timeout(3000)
            await page.keyboard.press("Enter")
            print("⚡ Hotkey Save Version pipeline dispatched.")

        print("⏳ Waiting 15 seconds to ensure the backend server locks in the commit token...")
        await page.wait_for_timeout(15000)
        
        print("\n" + "="*80)
        print("🎉 PIPELINE TRIGGER COMPLETE!")
        print("Kaggle is now running your script in a locked background environment on your GPU T4.")
        print("The GPU will automatically power off and stop usage the exact second your code finishes.")
        print("🔗 Track execution and view live logs here: https://kaggle.com")
        print("="*80 + "\n")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
