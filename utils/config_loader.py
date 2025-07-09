import yaml
import os

def load_config(config_path: str = "config/config.yaml") -> dict:
    """
    Load configuration settings from a YAML file.

    Parameters:
    - config_path (str): Path to the YAML configuration file. 
                         Defaults to 'config/config.yaml'.

    Returns:
    - dict: Parsed configuration as a Python dictionary.
    """
    # Open and read the YAML file
    with open(config_path, "r") as file:
        # Safely load YAML content into a Python dictionary
        config = yaml.safe_load(file)
        # Optionally print for debugging: print(config)
    
    # Return the loaded configuration
    return config
