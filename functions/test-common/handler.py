try: # Cognite Function
    from common.utils import my_helper1, my_helper2
except ModuleNotFoundError: # Local development
    import sys
    sys.path.append(f"{sys.path[0]}/..")
    from common.utils import my_helper1, my_helper2


def handle(client=None, data=None) -> None:
    print(f"Successfully imported {my_helper1}")
    my_helper2()


if __name__ == '__main__':
    import os

    from cognite.client import CogniteClient, ClientConfig
    from cognite.client.credentials import OAuthClientCredentials
    from dotenv import load_dotenv

    load_dotenv()

    client = CogniteClient(
        ClientConfig(
            client_name="My Local",
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

