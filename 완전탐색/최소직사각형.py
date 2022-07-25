def solution(sizes):
    # 긴 것이 가로, 짧은 것이 세로
    # 가로중에 가장 긴 것, 세로중에 가장 긴 것
    mx_w, mx_h = max(map(max, sizes)), max(map(min, sizes))
    wallet = mx_w * mx_h  # 명함 길이
    return wallet
