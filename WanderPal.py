from wanderpal_mapper.agent.Agent import Agent
from wanderpal_mapper.routing.RouteFinder import RouteFinder
from wanderpal_mapper.user_interface.utils import (generate_leafmap,validation_message,generate_generic_leafmap)

from dotenv import load_dotenv
import os
from pathlib import Path
from wanderpal_mapper.user_interface.constants import VALID_MESSAGE


def load_secrets():
    load_dotenv()
    env_path = Path(".")/".env"
    load_dotenv(dotenv_path=env_path)

    open_ai_key = os.getenv("OPENAI_API_KEY")
    google_maps_key = os.getenv("GOOGLE_MAPS_API_KEY")
    google_palm_key = os.getenv("GOOGLE_PALM_API_KEY")

    return {
        "OPEN_API_KEY" : open_ai_key,
        "GOOGLE_PALM_API_KEY" : google_palm_key
    }