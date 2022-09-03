def solution(id_list, report, k):
    answer = []

    dic = {} #
    count = {} #
    bad_list = list() #
    messageMap = {}

    # 배열 초기화
    for id in id_list:
        dic[id] = set()
        count[id] = 0
        messageMap[id] = 0

    # 신고한 사람 정리: dic 만들기
    for name in report:
        good_id, bad_id = name.split(" ")
        dic[good_id].add(bad_id)

    # 신고 받은 횟수 정리: count 만들기
    for key, value in dic.items():
        for ele in value:
            count[ele] += 1

    # 정지당하는 사람 설정: bad_id 만들기
    for key, val in count.items():
        if val >= k:
            bad_list.append(key)

    # 메일 받을 횟수 구하기
    for key, value in dic.items():
        for ele in value:
            for bad in bad_list:
                if bad == ele:
                    messageMap[key] += 1

    # 리스트 만들기
    for id in id_list:
        answer.append(messageMap[id])

    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"],
             ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "apeach muzi"],
             2))
