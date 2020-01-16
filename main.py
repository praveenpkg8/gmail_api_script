from config import get_access_token, load_input_data
from database import init_db
from services.action_service import ActionService
from services.predicate_service import PredicateService


def perform_task():
    service = get_access_token()
    input_data_list = load_input_data()
    for input_data in input_data_list:
        if input_data.get('rule') == "ALL":
            mail = PredicateService.all_predicate(
                config=input_data.get('config'),
                details=input_data.get('details')
            )
            if not mail:
                continue

            ActionService.perform_action(
                service=service,
                user_id="me",
                msg_id=mail.id,
                action=input_data.get('action')
            )

        elif input_data.get('rule') == 'ANY':
            mail = PredicateService.any_predicate(
                config=input_data.get('config'),
                details=input_data.get('details')
            )
            if not mail:
                continue

            ActionService.perform_action(
                service=service,
                user_id="me",
                msg_id=mail.id,
                action=input_data.get('action')
            )


if __name__ == "__main__":
    init_db()
    perform_task()




