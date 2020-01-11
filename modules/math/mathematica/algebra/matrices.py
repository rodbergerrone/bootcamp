def add_matrices(m1, m2):
    """

    :param m1: lista
    :param m2: lista
    :return: wyrzuca sume list
    """
    added_list = m1 + m2
    added_list.sort()
    return added_list

def sub_matrices(m1, m2):
    for i in m2:
        if i in m1:
            m1.remove(i)
        else:
            m1.append(i)
    m1.sort()
    return m1