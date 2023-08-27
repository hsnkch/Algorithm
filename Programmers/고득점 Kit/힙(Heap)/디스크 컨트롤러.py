import heapq
def solution(jobs):
    answer = 0
    cur_t = 0
    job_idx = 0
    heap = []

    # 요청 시간 기준 정렬
    jobs.sort()

    while job_idx < len(jobs) or heap:

        # 현재 요청이 온 작업 힙에 넣기
        while job_idx < len(jobs) and jobs[job_idx][0] <= cur_t:
            req_t, prc_t = jobs[job_idx]
            # prc_t, req_t 순서로 넣으면 계산 가능
            heapq.heappush(heap, (prc_t, req_t))
            job_idx += 1

        # 요청 O 일때 현재시간, answer 변경
        if heap:
            prc_t, req_t = heapq.heappop(heap)
            cur_t += prc_t
            answer += cur_t - req_t

        # 요청 X 일때 현재시간 변경
        else:
            cur_t = jobs[job_idx][0]


    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))