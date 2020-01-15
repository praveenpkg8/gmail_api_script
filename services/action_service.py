from apiclient import errors


from services.label_service import LabelService
class ActionService:

    @classmethod
    def perform_action(cls, service, user_id, msg_id, labels, action="READ"):

        try:
            msg_labels = {'removeLabelIds': [], 'addLabelIds': []}
            if action == "READ":
                msg_labels = ActionService.mark_as_read()
            elif action == "UNREAD":
                msg_labels = ActionService.mark_as_unread()
            elif action == "LABELS":
                msg_labels = ActionService.add_labels(service, labels)

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


