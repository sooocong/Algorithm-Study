def solution(record):
    answer = []
    uid_dict = {}
    logs = []

    # 1단계: uid → nickname 최신값 저장
    for r in record:
        parts = r.split()
        if parts[0] == "Enter" or parts[0] == "Change":
            uid, name = parts[1], parts[2]
            uid_dict[uid] = name

    # 2단계: Enter / Leave 로그만 기록
    for r in record:
        parts = r.split()
        if parts[0] == "Enter":
            uid = parts[1]
            logs.append((uid, "Enter"))
        elif parts[0] == "Leave":
            uid = parts[1]
            logs.append((uid, "Leave"))

    # 3단계: 최종 닉네임으로 메시지 생성
    for uid, action in logs:
        name = uid_dict[uid]
        if action == "Enter":
            answer.append(f"{name}님이 들어왔습니다.")
        else:
            answer.append(f"{name}님이 나갔습니다.")

    return answer