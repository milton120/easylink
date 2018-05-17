from common.enums import Status

def unique_tag_name_by_owner(self, value, model_class):
    request = self.context.get("request")
    try:
        data_id = self.instance.id
    except AttributeError:
        data_id = None

    query = model_class.objects.filter(
        entry_by=request.user,
        name=value,
        status=Status.ACTIVE
    )

    if data_id:
        query = model_class.objects.exclude(pk=data_id)

    if query.exists():
        return False
    else:
        return True
