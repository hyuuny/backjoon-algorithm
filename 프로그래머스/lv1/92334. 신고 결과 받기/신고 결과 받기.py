def solution(id_list, report, k):
    report_hash = {}
    result_hash = {}

    for r in report:
        user, bad = r.split()
        if user not in report_hash:
            report_hash[user] = set()
        report_hash[user].add(bad)

        if bad not in result_hash:
            result_hash[bad] = set()
        result_hash[bad].add(user)

    answer = [0 for _ in range(len(id_list))]
    for i in range(len(id_list)):
        user = id_list[i]
        if user not in report_hash:
            continue

        for bad in report_hash[user]:
            if len(result_hash[bad]) >= k:
                answer[i] += 1

    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
