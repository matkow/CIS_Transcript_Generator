
def create_attr_list(attributes):
        s_attr = str(attributes)
        s_attr = s_attr[1:-1]
        attr = []
        while s_attr.__contains__(","):
                temp = s_attr[0:s_attr.find(",")]
                attr.append(temp[1:-1])
                s_attr = s_attr[int(s_attr.find(",")) + 2:]
        attr.append(s_attr[1: -1])
        attributes = attr

        return attributes
