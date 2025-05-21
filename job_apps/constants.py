from configparser import ConfigParser


config = ConfigParser()
config.read('../config.ini')

NOTION_API_KEY = config['secrets']['api_key']
DATABASE_ID = config['databases']['database_id']
API_HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}
URL_DATABASE = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"


def generate_configfile_template(filename: str = 'config.template.ini') -> None:
    """Generate and save a config template."""
    config = ConfigParser()
    config['secrets'] = {'api_key': ''}
    config['databases'] = {'database_id': ''}
    with open(filename, 'w') as config_file:
        config.write(config_file)
    return None
