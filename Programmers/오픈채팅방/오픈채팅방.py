def solution(record):
    answer = []
    logs = []
    users = {}
    
    for r in record:
        l = list(r.split())
        logs.append(l)
        if l[0] == 'Enter' or l[0] == 'Change':
            users[f'{l[1]}'] = f'{l[2]}'
    
    for log in logs:
        message = ''
        if log[0] == 'Enter':
            message = f'{users[log[1]]}님이 들어왔습니다.'
        elif log[0] == 'Leave':
            message = f'{users[log[1]]}님이 나갔습니다.'
        else: continue
        answer.append(message)
    
    return answer