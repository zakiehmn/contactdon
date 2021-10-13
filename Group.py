class Group :
    def __init__(self, name, id, membersList = []):
        self._name = name
        self._membersList = membersList
        self._id = id
    
    def add_contact_group(self, idslist, contactDic):
        for id in idslist:
            self._membersList.append(contactDic[id])