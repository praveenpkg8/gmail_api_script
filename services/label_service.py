from apiclient import errors


class LabelService:

    @classmethod
    def get_label_list(cls, service):
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])
        label_name_list = [label.get('name') for label in labels]
        return label_name_list, labels


    @classmethod
    def create_label(cls, service, user_id, label_name):
        try:
            label_object = LabelService.make_labels(label_name=label_name)
            label = service.users().labels().create(userId=user_id,
                                                    body=label_object).execute()
            return label
        except errors.HttpError as error:
            print('An error occurred: %s' % error)

    @classmethod
    def make_labels(cls,
                    label_name,
                    msg_list_visibility='show',
                    label_list_visibility='labelShow'
                    ):
        label = {
            'messageListVisibility': msg_list_visibility,
            'name': label_name,
            'labelListVisibility': label_list_visibility
        }
        return label

    @classmethod
    def get_label_id(cls,
                     service,
                     label_name
                     ):
        result = []
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])
        for label in labels:
            if label.get('name') == label_name:
                result.append(label.get("id"))
                break

        return result



