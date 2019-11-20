def remove_hidden_folder(list_name):
    if '.DS_Store' in list_name:
        list_name.remove('.DS_Store')
        return list_name

    return list_name