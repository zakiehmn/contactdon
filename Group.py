class Group :
    def __init__(self, name, id, membersList = []):
        self._name = name
        self._membersList = membersList
        self._id = id
    
    def add_contact_group(self, idslist, contactDic):
        contactsList = []
        for id in idslist:
            contactsList.append(contactDic[id])
        self._membersList = contactsList

    def __str__(self):
        return '{} {} {} members'.format(self._id, self._name, str(len(self._membersList)))