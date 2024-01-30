try:
    from utils import HELLO_WORLD # Cognite Function
except:
    import sys
    sys.path.append(f"{sys.path[0]}/..")
    from common.utils import HELLO_WORLD # Local development

def handle(client, data=None) -> None:
    print(f"Successfully imported {HELLO_WORLD}")

if __name__ == '__main__':
    import os

    from cognite.client import CogniteClient, ClientConfig
    from cognite.client.config import global_config
    from cognite.client.credentials import OAuthClientCredentials
    from dotenv import load_dotenv

    load_dotenv()

    client = CogniteClient(
        ClientConfig(
            client_name="Ben SDK",
            project=os.environ.get('PROJECT'),
            base_url=os.environ.get('BASE_URL'),
            timeout=600,
            max_workers=36,
            credentials=OAuthClientCredentials(
                token_url=f"https://login.microsoftonline.com/{os.environ.get('TENANT_URL')}/oauth2/v2.0/token",
                client_id=os.environ.get('CLIENT_ID'),
                client_secret=os.environ.get('CLIENT_SECRET'),
                scopes=[f"{os.environ.get('BASE_URL')}/.default"]
            )
        )
    )

    handle(client)