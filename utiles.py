def formatter(cursor,data):
    result = []
    for row in data:
        row_dict = {}
        for idx, column in enumerate (cursor.description):
            row_dict[column[0]]=row[idx]
    result.append(row_dict)
    return result
        
