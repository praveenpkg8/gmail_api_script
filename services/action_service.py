from apiclient import errors


from services.label_service import LabelService


class ActionService:

    @classmethod
    def perform_action(cls, service, user_id, msg_id, action):

        label_name = action.get('label_name')
        action = ActionService.parse_action(action)
        try:
            msg_labels = {'removeLabelIds': [], 'addLabelIds': []}
            if action == "READ":
                msg_labels = ActionService.mark_as_read()
            elif action == "UNREAD":
                msg_labels = ActionService.mark_as_unread()
            elif action == "ARCHIVE":
                msg_labels = ActionService.archive_mail()
            elif action == "LABELS":
                msg_labels = ActionService.add_labels(service, label_name)

            message = service.users().messages().modify(userId=user_id, id=msg_id,
                                                        body=msg_labels).execute()

            label_ids = message['labelIds']

            print('Message ID: %s - With Label IDs %s' % (msg_id, label_ids))
            return message
        except errors.HttpError as error:
            print('An error occurred: %s' % error)

    @classmethod
    def add_labels(cls, service, label_name):
        label_name_list, labels = LabelService.get_label_list(service)
        if label_name in label_name_list:
            add_label_ids = [label.get('id') for label in labels if label.get('name') == label_name]
            return {'removeLabelIds': [], 'addLabelIds': add_label_ids}

        LabelService.create_label(
            service=service,
            user_id="me",
            label_name=label_name,
        )
        label = LabelService.get_label_id(service, label_name)
        return {'removeLabelIds': [], 'addLabelIds': label}

    @classmethod
    def mark_as_read(cls):
        return {'removeLabelIds': ['UNREAD'], 'addLabelIds': []}

    @classmethod
    def mark_as_unread(cls):
        return {'removeLabelIds': [], 'addLabelIds': ['UNREAD']}

    @classmethod
    def archive_mail(cls):
        return {'removeLabelIds': ['INBOX'], 'addLabelIds': []}

    @classmethod
    def parse_action(cls, action):
        if not action:
            return "READ"
        if action.get('mark_as_read'):
            return "READ"
        elif action.get('mark_as_un_read'):
            return "UNREAD"
        elif action.get('to_archive'):
            return "ARCHIVE"
        elif action.get('is_label'):
            return "LABELS"


