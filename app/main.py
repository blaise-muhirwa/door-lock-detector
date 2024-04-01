import os
import logging

from dotenv import load_dotenv
from framegrab import FrameGrabber
import yaml
import time
from groundlight import Groundlight

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


def get_grabber() -> None:
    """
    Uses framegrab to set up camera
    """

    with open("camera-config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
        config = yaml.safe_load(config["GL_CAMERAS"])

    grabbers = FrameGrabber.create_grabbers(config)

    assert len(grabbers) == 1

    return grabbers["Door Lock Camera"]


def main():
    load_and_validate_api_key()
    # os.environ["GROUNDLIGHT_API_TOKEN"] = "api_2eVbf3SRYOLt66D98190muD805c_xzUNxZpfkDmtkQGydqBr1ggjwjGT4G8wp9"
    # os.environ["GROUNDLIGHT_ENDPOINT"] = "https://api.dev.groundlight.ai"
    # gl_sdk = Groundlight()

    # detector = gl_sdk.get_or_create_detector(
    #     name="Door Lock Detector", query="Is the door locked?", confidence_threshold=0.8
    # )

    while True:
        grabber = get_grabber()
        image = grabber.grab()

        # image_query = gl_sdk.submit_image_query(detector=detector, image=image, wait=0)

        logging.info(f"<door-lock-detector> sending an IQ to Groundlight")
        time.sleep(0.5)



if __name__ == "__main__":
    main()
