import asyncio

import argparse

import os

import time


from dotenv import load_dotenv


load_dotenv()


from src.utils.default_config_settings import default_config

from Webui_Chrome_User_Data import run_with_stream  # Import run_with_stream


async def main():

    load_dotenv()


    parser = argparse.ArgumentParser(description="Run Browser Agent without Gradio UI")

    parser.add_argument("--task", type=str, help="Task description")

    parser.add_argument("--headless", action="store_true", help="Run in headless mode")

    args = parser.parse_args()


    config_dict = default_config()

    if args.task:

        config_dict['task'] = args.task

    if args.headless:

        config_dict['headless'] = True

    

    

    timeout_duration = 1 * 60  # 15 minutes in seconds

    start_time = time.time()

    Counter =1


    while True:

        try:

            #Iterate over the generator

            async for item in run_with_stream(

                agent_type=config_dict['agent_type'],

                llm_provider=config_dict['llm_provider'],

                llm_model_name=config_dict['llm_model_name'],

                llm_temperature=config_dict['llm_temperature'],

                llm_base_url=config_dict['llm_base_url'],

                llm_api_key=config_dict['llm_api_key'],

                use_own_browser=config_dict['use_own_browser'],

                keep_browser_open=config_dict['keep_browser_open'],

                headless=config_dict['headless'],

                disable_security=config_dict['disable_security'],

                window_w=config_dict['window_w'],

                window_h=config_dict['window_h'],

                save_recording_path=config_dict['save_recording_path'],

                save_agent_history_path=config_dict['save_agent_history_path'],

                save_trace_path=config_dict['save_trace_path'],

                enable_recording=config_dict['enable_recording'],

                task=config_dict['task'],

                add_infos="You are a virtual assitant",

                max_steps=10,

                use_vision=config_dict['use_vision'],

                max_actions_per_step=config_dict['max_actions_per_step'],

                tool_calling_method=config_dict['tool_calling_method'],

                chrome_user_data="Default" if Counter % 2==0 else "Default"

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

        Counter+=1


if __name__ == "__main__":

    asyncio.run(main())
