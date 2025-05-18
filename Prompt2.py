def get_task_prompt(job_link):

    task= f"""


            **Objective:** Apply to the job found at the provided link `{job_link}` using the "Easy Apply" feature, **strictly within a single browser tab.**

            **Agent Role:** You are an AI agent interacting with a web browser. Your task is to follow the steps below precisely to apply for the specified job, maintaining all activity within the current, single browser tab.

            **Core Principle: Single Tab Operation**
            *   **No New Tabs:** Under no circumstances should you intentionally open a new browser tab or window.
            *   **Close Accidental Tabs:** If any action inadvertently causes a new tab or window to open, **immediately close the new tab/window** and return your focus to the original tab where the job application process was initiated.
            *   **Maintain One Active Tab:** Your entire workflow must occur within the single, initial browser tab.

            **Context:** You will start by navigating directly to a job posting page.

            **Instructions:**

            **Phase 1: Navigate to Job & Initiate Application**

            1.  **Verify Single Tab:** Before starting, confirm you are operating in a single browser tab. If multiple tabs are open, close all but the one intended for this task.
            2.  **Navigate to Job Link:** Open your web browser and go directly to the URL specified in the variable `{job_link}`. **Ensure this action occurs within the current, single tab.** If it attempts to open `{job_link}` in a new tab, close that new tab and try navigating in the current tab again.
            3.  **Verify Page Load:** Ensure the webpage at `{job_link}` has fully loaded within the current tab.
            4.  **Locate "Easy Apply" Button:** Carefully scan the job details section on the current page. Find the button specifically labeled **"Easy Apply"** (or a very similar phrase like "Apply easily").
                *   **Hint:** This button might require scrolling down slightly within the job details section.
                *   **Constraint:** *Do not* click buttons labeled "Apply on company site", "Apply now", or just "Apply" if an "Easy Apply" option is present. Prioritize "Easy Apply".
                *   **If "Easy Apply" is NOT found:** Stop the process. The specific job at `{job_link}` does not support the "Easy Apply" method.
            5.  **Click "Easy Apply":** Once found, click the "Easy Apply" button. This should open a dialog box or modal window for the application form **within the current tab.** If it attempts to open a new tab, stop this action, close the new tab, and see if there's an alternative "Easy Apply" interaction that keeps it in the current tab.

            **Phase 2: Filling the "Easy Apply" Form**

            6.  **Process Form Questions:** Interact with the form presented in the "Easy Apply" dialog box step-by-step, **remaining in the current tab.**
                *   **Focus on Required Fields:** Only answer questions explicitly marked as **required** (usually indicated by an asterisk `*`).
                *   **Skip Pre-filled/Answered Questions:** If a question already has an answer selected or text entered (other than default placeholder text), **skip it** and move to the next question.
                *   **Handle Dropdowns:**
                    *   Click the dropdown element to reveal the options.
                    *   **Wait 2 seconds** for the options to fully load.
                    *   Select the most **affirmative or positive option** available (e.g., "Yes", "Agree", the first valid option if unsure). Avoid options like "No", "Decline", "None", or leaving it blank if required.
                *   **Handle Text Inputs:** For required text input fields, provide concise and relevant information if necessary.
                *   **CRITICAL CONSTRAINT:** **ABSOLUTELY DO NOT** click any buttons or links related to **"Upload Resume"**, **"Attach Resume"**, **"Resume"**, or similar file upload actions. *Avoid interacting with resume sections entirely.*
                *   **Tab Check:** Periodically verify you are still in the single, original tab. If a new tab has opened, close it immediately and return.

            **Phase 3: Form Navigation & Submission**

            7.  **Check Form Completion:** Once you have addressed all *required* questions on the current form page:
                *   **Scroll Down:** Scroll down within the "Easy Apply" dialog/modal.
                *   **Find Navigation Button:** Look for one of the following buttons near the bottom: **"Next"**, **"Review"**, or **"Submit"**.
                *   **Click Navigation Button:** Click the first button you find among "Next", "Review", or "Submit". **Ensure this click stays within the current tab.**
            8.  **Handle "Review" Page (If Applicable):**
                *   If clicking the button took you to a "Review" page:
                    *   Scroll down to the bottom of the review page.
                    *   Locate and click the **"Submit"** or **"Submit application"** button. **Ensure this click stays within the current tab.**
            9.  **Handle "Next" Page (If Applicable):**
                *   If clicking the button took you to another page of questions, return to **Step 6 (Process Form Questions)** for the new page.
            10. **Handle Submission Confirmation:**
                *   After clicking "Submit", you might see a confirmation message or page.
                *   Locate and click the **"Done"** button (or similar, like "Close", "Okay"). **Ensure this click stays within the current tab.**

            **Phase 4: Completion**

            11. **Stop:** Once you have successfully clicked "Done" after submitting the application for the job at `{job_link}`, and have ensured you are still in the single original tab, your task is complete for this session.

            **Error Handling (Basic):**

            *   If you cannot find the "Easy Apply" button for the job at `{job_link}`, stop the process.
            *   If an action opens a new tab (including navigating to `{job_link}` initially), **immediately close the new tab** and attempt to continue the process in the original tab. If this is not possible or happens repeatedly for a specific action, stop processing the current job.
            *   If you encounter an unexpected error or popup that you cannot resolve within the single tab, stop the process for the current job.
        """
    return task