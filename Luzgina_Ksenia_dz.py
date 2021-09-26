with open('webf.txt', 'r', encoding='utf-8') as f:

    result = []
    line = f.readline()

    while line:
        tuple_result = []
        line = line.split(' - - ')
        remote_addr = line[0]
        print(remote_addr)
        tuple_result.append(remote_addr)
        line = line[-1]
        line = line.split('"')
        request_resource = line[1].split(' ')
        request_type = request_resource.pop(0)
        request_resource = ' '.join(request_resource)
        tuple_result.append(request_type)
        tuple_result.append(request_resource)
        tuple_result = tuple(tuple_result)
        result.append(tuple_result)
        line = f.readline()

    print(result)
