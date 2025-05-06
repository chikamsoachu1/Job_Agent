def get_task_prompt(job_link):


    task=f"""Go to {job_link}

                You would see a list of jobs on the left, apply to 1 of the available jobs available




                HINTS



                USING THE FOLLOWING INSTRUCTIONS 

                APPLYING TO JOBS

                - Click each job

                -Located the easy apply button on at index in range 55-80

                -Click easy apply 

                -Use Easy Apply Instructions to Apply

                -Do not click on "upload resume" , do not try to upload resume
                -Do not click on "Resume"
               
                -For drop drown click drop down and wait 2 seconds for options and then select positive option

                EASY  APPLY INSTRUCTIONS

                -Fill out form on the dialog box

                -Ignore form questions that have an already entered input,

                -For drop drown click drop down and wait 2 seconds for options and then select positive option

                -If a question is answered indicated by an already option selected skip question.

                -If all questions on form are filled, to proceed scroll down dialog BOX until you see one of three options Next or Review or Submit Application . Click whichever is found.

                -On the review page Scroll down and find and click on the submit button.

                - After clicking submit click, on the next page find and click on the done button and move to the next job

                -Only answer form questions that are required indicated by * at the end of the question


                                                        """

    return task


