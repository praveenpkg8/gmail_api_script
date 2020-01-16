import click

from config import get_access_token
from database import init_db
from services.mail_service import MailService

service = get_access_token()


@click.command()
@click.option('--count', prompt='Enter total mail to load from Gmail',
              help='The person to greet.')
def load_mail_to_database(count):
    MailService.update_mail_in_database(
        service=service,
        user_id="me",
        total_mail=int(count)
    )
    print("Datastore has been populate with {} mail".format(count))


if __name__ == "__main__":
    init_db()
    load_mail_to_database()
