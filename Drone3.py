
import asyncio

import argparse

import os

import time


from dotenv import load_dotenv


load_dotenv()

from task_creator import get_task_prompt

from list_of_links import links


from Webui_Chrome_User_Data import run_with_stream  # Import run_with_stream


async def main():

    load_dotenv()


    parser = argparse.ArgumentParser(description="Run Browser Agent without Gradio UI")

    parser.add_argument("--task", type=str, help="Task description")

    parser.add_argument("--headless", action="store_true", help="Run in headless mode")

    args = parser.parse_args()

  

    

    if args.task:

        config_dict['task'] = args.task

    if args.headless:

        config_dict['headless'] = True

    

    

    timeout_duration = 15 * 60  # 15 minutes in seconds

    start_time = time.time()

    Counter =1


    while True:

        try:

            print("tHE COUNTER IS ")

            print(Counter)

            #Iterate over the generator

            tasks =get_task_prompt(links[Counter%2])

            print(tasks)

            chrome_user_data="app/data/chrome_data" if Counter % 2==0 else "app/data/chrome_data"

            

            async for item in run_with_stream(

                agent_type="custom",

                max_steps= 15,

                max_actions_per_step= 10,

                use_vision= True,

                tool_calling_method ="auto",

                llm_provider="google",

                llm_model_name= "gemini-2.0-flash",

                llm_temperature=1.0,

                llm_base_url= "",

                llm_api_key= "",

                use_own_browser=  True,

                keep_browser_open= False,

                headless=False,

                disable_security= True,

                enable_recording= True,

                window_w= 1280,

                window_h= 1100,

                add_infos="You are a virtual assitant",

                save_recording_path= "./tmp/record_videos",

                save_trace_path= "./tmp/traces",

                save_agent_history_path= "./tmp/agent_history",

                task= tasks,

                chrome_user_data=chrome_user_data

            ): 

                elapsed_time = time.time() - start_time

                if elapsed_time > timeout_duration:

                    print("Timeout: Execution stopped after 15 minutes.")

                    break  # Exit the loop if timeout is reached

                # Process each item yielded by run_with_stream

                html_content, final_result, errors, model_actions, model_thoughts, latest_videos, trace, history_file, stop_button, run_button = item

                print("--- New Stream Item ---")

                print(f"HTML Content: {html_content}") #Display screenshot

                print(f"Final Result: {final_result}")

                print(f"Errors: {errors}")

                # You can print other variables or process them as needed


            if time.time() - start_time <= timeout_duration:

                print("Agent run completed successfully (before timeout).")

            else:

                print("Agent exited due to timeout.")



        except Exception as e:

            print(f"An error occurred: {e}")


        """        await _global_browser_context.close()

                _global_browser_context=None

                await _global_browser.close()

                _global_browser = None"""

        Counter+=1


if __name__ == "__main__":

    asyncio.run(main())
