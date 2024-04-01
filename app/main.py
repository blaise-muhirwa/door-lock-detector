import os
import logging 

from dotenv import load_dotenv
from framegrab import FrameGrabber
import yaml 
import time 

logging.basicConfig(level=logging.INFO)


def load_and_validate_api_key():
    """
    Loads the contents of the .env file into the environment,
    including your Groundlight API Token.
    Validates that the token is set correctly, and raises an error if not.
    """

    load_dotenv()

    api_token = os.getenv("GROUNDLIGHT_API_TOKEN")
    if not api_token or not api_token.startswith("api_"):
        raise ValueError(
            "The 'GROUNDLIGHT_API_TOKEN' is not set correctly in the .env file. "
            "It should start with 'api_'. You can create a token here: "
            "https://app.groundlight.ai/reef/my-account/api-tokens."
        )


def main() -> None:
    """
    Uses framegrab to set up camera
    """
    
    with open("camera-config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
        config = yaml.safe_load(config["GL_CAMERAS"])
        
    # grabbers = FrameGrabber.create_grabbers(config)
    logging.info(f"Camera Config: {config}")
    
    while True:
        current_time = time.time()
        logging.info(f"<{current_time}> Running door-lock detection...")
        
        time.sleep(5)   
        


if __name__=="__main__":
    main()
